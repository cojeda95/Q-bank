/* Lesion Atlas layout auditor. Serve the repo root (python3 -m http.server), open
   /resources/metabolic-atlas.html and load it from the console with:
     (0,eval)(await (await fetch('/tools/atlas-audit.js')).text()); __auditAll()
   Rooted on #svg (the map) — NOT document.querySelector('svg'), which is a toolbar icon. */
window.__boxes = function(view){
  setView(view);
  const svg=document.getElementById('svg'), cam=svg.querySelector('#cam'), inv=cam.getCTM().inverse();
  const box=el=>{const b=el.getBBox(), m=inv.multiply(el.getCTM());
    const pts=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>{const p=svg.createSVGPoint();p.x=x;p.y=y;return p.matrixTransform(m);});
    const xs=pts.map(p=>p.x),ys=pts.map(p=>p.y);
    return {x:Math.min(...xs),y:Math.min(...ys),w:Math.max(...xs)-Math.min(...xs),h:Math.max(...ys)-Math.min(...ys)};};
  const items=[];
  svg.querySelectorAll('.node').forEach(g=>items.push({t:'node',id:g.dataset.node,b:box(g.querySelector(':scope > rect')),g}));
  svg.querySelectorAll('.chip').forEach(g=>items.push({t:'chip',id:g.dataset.chip,b:box(g.querySelector('rect.bg'))}));
  svg.querySelectorAll('.panel-c').forEach((g,i)=>items.push({t:'panel',id:'panel'+i,b:box(g.querySelector('rect'))}));
  svg.querySelectorAll('.pin').forEach(g=>items.push({t:'pin',id:g.dataset.les,b:box(g.querySelector('.pshape')),owner:g.closest('.node'),chipOwner:g.closest('.chipwrap')}));
  svg.querySelectorAll('.comp-badge').forEach((r,i)=>items.push({t:'badge',id:'badge'+i,b:box(r)}));
  return {svg,box,items};
};
window.__audit = function(view){
  const {svg,box,items}=__boxes(view);
  const ov=(a,b,pad)=>{const x=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x), y=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y); return (x>pad&&y>pad)?[+x.toFixed(1),+y.toFixed(1)]:null;};
  const nodeCount=items.filter(i=>i.t==='node').length;
  if(!nodeCount) return {view, ERROR:'zero nodes — auditor is rooted on the wrong element'};
  const out={view,nodes:nodeCount,overlaps:[],overflow:[],buried:[],foreign:[],pinfill:[],offcanvas:[]};
  for(let i=0;i<items.length;i++)for(let j=i+1;j<items.length;j++){
    const A=items[i],B=items[j];
    if(A.t==='node'&&B.t==='pin'&&B.owner===A.g) continue;   // a node's own pin hangs on its corner by design
    if(B.t==='node'&&A.t==='pin'&&A.owner===B.g) continue;
    const o=ov(A.b,B.b,A.t==='pin'&&B.t==='pin'?1:0.5); if(o) out.overlaps.push({a:`${A.t} ${A.id}`,b:`${B.t} ${B.id}`,px:o});
  }
  svg.querySelectorAll('.node').forEach(g=>{const r=box(g.querySelector(':scope > rect'));g.querySelectorAll(':scope > text').forEach(t=>{const w=textW(t);if(w>r.w-8)out.overflow.push(`node ${g.dataset.node}`);});});
  svg.querySelectorAll('.chip').forEach(g=>{const r=box(g.querySelector('rect.bg'));g.querySelectorAll('text').forEach(t=>{if(textW(t)>r.w-6)out.overflow.push(`chip ${g.dataset.chip}`);});});
  svg.querySelectorAll('.panel-c').forEach(g=>{const r=box(g.querySelector('rect'));g.querySelectorAll('text').forEach(t=>{const b=box(t);if(b.x+b.w>r.x+r.w-4||b.y+b.h>r.y+r.h-2)out.overflow.push(`panel text: ${t.textContent.slice(0,30)}`);});});
  svg.querySelectorAll('.comp-tag').forEach(g=>{const r=box(g.querySelector('rect')),t=g.querySelector('text');if(textW(t)>r.w-10)out.overflow.push(`badge ${t.textContent.slice(0,30)}`);});
  const m=MAPS[view];
  const tipsOf=m.edges.filter(e=>(e.arrow||"one")!=="none").map(e=>({k:e.a+'>'+e.b,g:geom(m,e)}));
  const labelBoxes=items.filter(i=>i.t==='chip'||i.t==='panel');
  svg.querySelectorAll('.tip-layer path').forEach(p=>{
    const d=p.getAttribute('d').match(/M([\d.-]+) ([\d.-]+) L([\d.-]+) ([\d.-]+)/); if(!d) return;
    const [sx,sy,fx,fy]=d.slice(1).map(Number), L=Math.hypot(fx-sx,fy-sy), win=Math.min(18,L);
    const inside=(x,y)=>labelBoxes.filter(b=>x>b.b.x+1&&x<b.b.x+b.b.w-1&&y>b.b.y+1&&y<b.b.y+b.b.h-1);
    const tip=inside(fx,fy); let n=0; const ids=new Set();
    for(let k=0;k<6;k++){const f=k/5,x=fx-(fx-sx)/L*win*f,y=fy-(fy-sy)/L*win*f;const h=inside(x,y);if(h.length){n++;h.forEach(b=>ids.add(b.id));}}
    if(tip.length||n>=2){
      const owner=tipsOf.find(t=>Math.hypot(t.g.p2.x-fx,t.g.p2.y-fy)<1.5||Math.hypot(t.g.p1.x-fx,t.g.p1.y-fy)<1.5);
      out.buried.push({arrowOf:owner?owner.k:'?',tip:[+fx.toFixed(0),+fy.toFixed(0)],under:[...new Set([...ids,...tip.map(b=>b.id)])],samplesInside:n});
    }
  });
  const edges=m.edges.map(e=>({k:e.a+'>'+e.b,e,g:geom(m,e)}));
  const dist=(g,x,y)=>{let best=1e9;for(let k=0;k<=60;k++){const t=k/60,px=(1-t)*(1-t)*g.p1.x+2*(1-t)*t*g.cx+t*t*g.p2.x,py=(1-t)*(1-t)*g.p1.y+2*(1-t)*t*g.cy+t*t*g.p2.y;best=Math.min(best,Math.hypot(px-x,py-y));}return best;};
  svg.querySelectorAll('.chipwrap').forEach(w=>{const k=w.querySelector('.chip').dataset.chip,cx=+w.dataset.cx,cy=+w.dataset.cy;const own=edges.find(e=>e.k===k);if(!own)return;const dO=dist(own.g,cx,cy);
    edges.forEach(e=>{if(e.k===k)return;const d=dist(e.g,cx,cy);if(d<dO-4&&d<40)out.foreign.push({chip:k,nearer:e.k,dOwn:+dO.toFixed(1),dForeign:+d.toFixed(1),lx:own.e.lx||0,ly:own.e.ly||0});});});
  svg.querySelectorAll('.pin').forEach(p=>{const L=LES[p.dataset.les];const tmp=document.createElement('div');tmp.style.color=getComputedStyle(document.documentElement).getPropertyValue(MK[L.k].v).trim();document.body.appendChild(tmp);const want=getComputedStyle(tmp).color;tmp.remove();if(want!==getComputedStyle(p.querySelector('.pshape')).fill)out.pinfill.push(p.dataset.les);});
  items.forEach(i=>{if(i.b.x<0||i.b.y<0||i.b.x+i.b.w>m.w||i.b.y+i.b.h>m.h)out.offcanvas.push(`${i.t} ${i.id}`);});
  return out;
};
window.__count = a => a.ERROR ? 1 : a.overlaps.length+a.overflow.length+a.buried.length+a.foreign.length+a.pinfill.length+a.offcanvas.length;
window.__auditAll = function(){
  const res={};
  for(const theme of ['light','dark']){
    document.documentElement.setAttribute('data-theme',theme);
    const bad={}; let n=0;
    for(const [v] of VIEWS){ if(v==='index') continue; const a=__audit(v); const c=__count(a); n+=c; if(c) bad[v]=a; }
    res[theme]={mapsAudited:VIEWS.length-1,totalFindings:n,maps:bad};
  }
  document.documentElement.setAttribute('data-theme','light');
  return res;
};
'auditor loaded';
