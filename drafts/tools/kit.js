/* ── Dynamic maps kit (art:"kit") ───────────────────────────────────────────
   A drawn, moving map is plain data on the map, m.dyn:
     kinds:    {kind:[group, "--colour-var"]}      particle kinds (an ion, a transmitter, a vesicle…)
     groups:   [[group, "label"]]                   the "Show" chips, one per group of kinds
     switches: [{id, label, type:"toggle", on:"chip text when on", off:"…when off", def:true}
                | {id, label, type:"one", options:[[key,"label","cardid"],…]}     pick at most one option; the card
                  is what that option is about (search, and "See it move" from the question bank)
                | {id, label, type:"steps", options:[[key,"label"],…], auto:seconds}]   always one option —
                  phases of a cycle; with auto they advance by themselves while the motion plays
                  (a tap on a phase holds it there; "Step through" starts it again)
     notes:    {"<condition>":"what that change does", …, "":"the note when nothing is changed"}
     shapes:   the drawing, under everything else — each is an SVG string, or
               {svg:"…", when:[conds], unless:[conds]}  drawn only then
               {tube:"<path d>", w, cls, color:"--dk3"}   a tube: wall + lumen (the nephron's segments; a gut, an airway)
               {vessel:"<path d>", w, cls, color, mods:[{when:[conds], d:±n}]}   a vessel whose width answers the switches
               {membrane:"<path d>", w}                 a lipid bilayer along a path (a cell membrane, a synaptic cleft's walls)
               {text:"…", x, y, cls, anchor, when, unless}
     flows:    [{d:"<path>", len, speed, r, base:{kind:n}, when, unless,
                 mods:[{when:[conds], add:{kind:±n}, set:{kind:n}, speed:×factor}]}]
               particles travelling along a path (fluid in a lumen, vesicles to a terminal…)
     sites:    [{x, y, n:[nx,ny], w, t, l, s, ions:[[kind,"out"|"in",n]], c,
                 block, stop, low, boost:[conds], need:[conds], closed:"why it is shut", when, unless,
                 lx, ly, la:"start|middle|end", cross:true, reach:px, dur:s, sfx:{block,stop,low,boost}}]   (lx/ly/la place the label by hand;
               cross: particles pass right through, from the far side to the label side; reach: how far past the wall)
               a transporter / receptor / channel on a wall at (x,y); n points to the side its label sits on;
               w is the wall's width there; ions cross it (out = toward n's opposite… see below); c = card it opens
     readouts: [{l:"GFR", mods:[{when:[conds], d:-1|0|1}]}]   ↑ ↓ ↔ gauges; "–" when no switch says.
               "Predict the arrows" hides them: the reader guesses each, then checks (st.pred)
     panel:    {x, y, w}                            where the switches sit on the canvas
     src:      "source line under the note"
   A condition is a switch key: "adh" (toggle on), "!adh" (toggle off), "drug:loop" (that option chosen),
   "drug:*" (any option of that group chosen), "a&b" (both). A list matches if ANY condition holds;
   need:[…] needs ALL. Notes are keyed the same way.
   Sites: block = a drug hits it directly (✕, no particles) · stop = idles because nothing reaches it ·
   low / boost = fewer / more particles · need = open only then. The label gains " — blocked", " — idle",
   " — less active" or " — more active" (sfx overrides any of them for one site). Particles cross from the lumen centre
   ("out": toward the label side, just past the wall) or the reverse ("in").
   Tapping a site opens its card (data-plotles — the graph card link) and the map stays put (KEEP_PT).
   Motion is SVG animateMotion: Pause stops it, and it starts paused for devices that ask for less motion.
   Styles are the nf-* classes (first written for Nephron in Motion) plus a 12-colour palette --dk1…--dk12.
   The switch state rides in the address (#map/~sw:key,!toggle — dynStateStr / dynApplyStr), phones get the
   controls as a docked HTML sheet (dynSheetRender), and the build moves each drawing to resources/dyn/<map>.js,
   loaded when the map opens (dynLoad) — the page keeps only {lazy, switches} for search and links.
   m42: every map also gets a Tour (st.tour — the switches one by one, each state's note as the narration), Name it
   (st.quiz — one option is switched on in secret; the reader names it from the drawing and the results) and Compare
   (st.cmp — pin a state, change the switches, then see both side by side: dynCompare). */
const DYN={};
function dynSt(v){
  const d=MAPS[v].dyn;
  if(!DYN[v]){
    const st={on:{},sw:{},paused:null};
    (d.groups||[]).forEach(([g])=>{ st.on[g]=1; });
    (d.switches||[]).forEach(s=>{ st.sw[s.id]=s.type==="one"?(s.def||""):s.type==="steps"?(s.def||s.options[0][0]):(s.def!==false);
      if(s.type==="steps"&&s.auto) st.auto=s.id; });
    DYN[v]=st;
  }
  return DYN[v];
}
function dynHas(st,c){
  if(!c) return false;
  if(c.indexOf("&")>0) return c.split("&").every(q=>dynHas(st,q));
  if(c[0]==="!") return !dynHas(st,c.slice(1));
  const i=c.indexOf(":"), a=i<0?c:c.slice(0,i), b=i<0?undefined:c.slice(i+1), v=st.sw[a];
  if(b===undefined) return v===true;
  if(b==="*") return !!v&&v!==true;
  return v===b;
}
const dynAny=(st,l)=>(l||[]).some(c=>dynHas(st,c));
const dynAll=(st,l)=>(l||[]).every(c=>dynHas(st,c));
function dynPaused(st){
  if(st.paused!==null) return st.paused;
  try{ return matchMedia("(prefers-reduced-motion: reduce)").matches; }catch(e){ return false; }
}
let DYN_T=null;
function dynMotion(){
  const v=state.view, m=MAPS[v], st=m&&m.dyn?dynSt(v):null;
  try{ if(st&&dynPaused(st)) svg.pauseAnimations(); else svg.unpauseAnimations(); }catch(e){}
  if(DYN_T){ clearInterval(DYN_T); DYN_T=null; }
  if(st&&st.auto&&!dynPaused(st)&&!st.pred){
    const s=m.dyn.switches.find(q=>q.id===st.auto);
    DYN_T=setInterval(()=>{ if(state.view!==v||!DYN[v]||!DYN[v].auto){ clearInterval(DYN_T); DYN_T=null; return; } dynSet("n:"+s.id,true); },(s.auto||3)*1000);
  }
  dynSheetRender();
}
const dynColor=(d,k)=>`var(${(d.kinds[k]||["","--ink-3"])[1]})`;
const dynDot=(d,k,r,anim)=>`<circle r="${r}" fill="${dynColor(d,k)}" stroke="var(--surface)" stroke-width="1.4">${anim}</circle>`;
function kitArt(m){
  const d=m.dyn;
  if(d.lazy){ dynLoad(state.view); const P=d.panel||{x:m.w-1080};
    return `<text class="dyn-big" x="${Math.round(Math.max(600,P.x-80)/2)}" y="${Math.round(m.h/2)}" text-anchor="middle">${DYNFAIL[state.view]?"The drawing couldn’t load — check your connection, then reopen this map":"Loading the drawing…"}</text>`; }
  const st=dynSt(state.view), out=[], hide=!!(st.quiz&&!st.quiz.ans);   // naming it: a state's own captions would give it away
  /* the drawing */
  (d.shapes||[]).forEach(s=>{
    if(typeof s==="string"){ out.push(s); return; }
    if(s.when&&!dynAny(st,s.when)) return;
    if(s.unless&&dynAny(st,s.unless)) return;
    if(hide&&s.when&&s.text!==undefined) return;
    if(s.svg) out.push(hide&&s.when?s.svg.replace(/<text\b[\s\S]*?<\/text>/g,""):s.svg);
    else if(s.tube){ let w=s.w; (s.mods||[]).forEach(md=>{ if(dynAny(st,md.when)) w+=md.d; });
      out.push(`<path d="${s.tube}" class="nf-wall ${s.cls||""}" stroke-width="${w+12}"${s.color?` style="stroke:var(${s.color})"`:""}/><path d="${s.tube}" class="nf-lumen" stroke-width="${Math.max(2,w)}"/>`); }
    else if(s.vessel){ let w=s.w; (s.mods||[]).forEach(md=>{ if(dynAny(st,md.when)) w+=md.d; });
      out.push(`<path d="${s.vessel}" class="${s.cls||"nf-art"}" stroke-width="${Math.max(4,w)}"${s.color?` style="stroke:var(${s.color})"`:""}/>`); }
    else if(s.membrane){ const w=s.w||22;
      out.push(`<path d="${s.membrane}" class="dyn-mem" stroke-width="${w}"/><path d="${s.membrane}" class="dyn-mem-in" stroke-width="${Math.max(2,w-10)}"/>`); }
    else if(s.text!==undefined) out.push(`<text class="${s.cls||"nf-l2"}" x="${s.x}" y="${s.y}"${s.anchor?` text-anchor="${s.anchor}"`:""}>${esc(s.text)}</text>`);
  });
  /* particles along paths */
  (d.flows||[]).forEach(f=>{
    if(f.when&&!dynAny(st,f.when)) return;
    if(f.unless&&dynAny(st,f.unless)) return;
    const c=Object.assign({},f.base); let sp=f.speed||140;
    (f.mods||[]).forEach(md=>{ if(!dynAny(st,md.when)) return;
      Object.entries(md.add||{}).forEach(([k,n])=>{ c[k]=Math.max(0,(c[k]||0)+n); });
      Object.entries(md.set||{}).forEach(([k,n])=>{ c[k]=n; });
      if(md.speed) sp*=md.speed; });
    const parts=[]; Object.keys(c).forEach(k=>{ if(!d.groups||!d.groups.length||st.on[(d.kinds[k]||[k])[0]]) for(let i=0;i<c[k];i++) parts.push(k); });
    const dur=(f.len/sp).toFixed(1);
    parts.forEach((k,i)=>{ const b=-(dur*(i+0.5)/parts.length).toFixed(2);
      out.push(dynDot(d,k,f.r||6,`<animateMotion dur="${dur}s" begin="${b}s" repeatCount="indefinite" path="${f.d}"/>`)); });
  });
  /* transporters, receptors, channels */
  (d.sites||[]).forEach((s,si)=>{
    if(s.when&&!dynAny(st,s.when)) return;
    if(s.unless&&dynAny(st,s.unless)) return;
    const [nx,ny]=s.n||[0,1], h=s.w/2, wx=s.x+nx*(h+3), wy=s.y+ny*(h+3), tx=-ny, ty=nx, vert=!!nx;
    const blocked=dynAny(st,s.block), stopped=!blocked&&dynAny(st,s.stop), closed=!!s.need&&!dynAll(st,s.need);
    const low=!blocked&&!stopped&&!closed&&dynAny(st,s.low), boost=!blocked&&!stopped&&!closed&&dynAny(st,s.boost);
    let ic="";
    const iw=vert?16:28, ih=vert?28:16;
    if(s.t==="para") ic=`<path d="M${wx-tx*14} ${wy-ty*14} L${wx+tx*14} ${wy+ty*14}" class="nf-ic-para"/>`;
    else if(s.t==="wall") ic=`<rect x="${wx-(vert?4:30)}" y="${wy-(vert?30:4)}" width="${vert?8:60}" height="${vert?60:8}" rx="3" class="nf-ic-wall"/>`;
    else if(s.t==="md") ic=`<g class="nf-ic-md">${[-18,-6,6,18].map(o=>`<circle cx="${wx+tx*o}" cy="${wy+ty*o}" r="5"/>`).join("")}</g>`;
    else if(s.t==="rec") ic=`<rect x="${wx-iw/2}" y="${wy-ih/2}" width="${iw}" height="${ih}" rx="8" class="nf-ic nf-ic-rec${closed?" closed":""}"/>`;
    else ic=`<rect x="${wx-iw/2}" y="${wy-ih/2}" width="${iw}" height="${ih}" rx="5" class="nf-ic nf-ic-${s.t}${closed?" closed":""}"/>`;
    if(blocked) ic+=`<path d="M${wx-11} ${wy-11} L${wx+11} ${wy+11} M${wx+11} ${wy-11} L${wx-11} ${wy+11}" class="nf-x"/>`;
    let ions="";
    if(!blocked&&!stopped&&!closed) (s.ions||[]).forEach(([k,dir,n],ii)=>{
      if(d.groups&&d.groups.length&&!st.on[(d.kinds[k]||[k])[0]]) return;
      const cnt=low?1:boost?n+1:n, dur=low?4.6:(s.dur||2.6), reach=s.reach||26;
      for(let j=0;j<cnt;j++){
        const off=(ii-(s.ions.length-1)/2)*11+(j%2?5:0);
        const c0=s.cross?-(h+reach):0;   // cross: the particle goes all the way through a membrane, from the far side
        const ax=s.x+nx*c0+tx*off, ay=s.y+ny*c0+ty*off, bx=s.x+nx*(h+reach)+tx*off, by=s.y+ny*(h+reach)+ty*off;
        const p=dir==="out"?`M${ax} ${ay} L${bx} ${by}`:`M${bx} ${by} L${ax} ${ay}`;
        const b=-((dur*(j/cnt+ii*0.21+si*0.13))%dur).toFixed(2);
        ions+=dynDot(d,k,6.5,`<animateMotion dur="${dur}s" begin="${b}s" repeatCount="indefinite" path="${p}"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.15;.8;1" dur="${dur}s" begin="${b}s" repeatCount="indefinite"/>`);
      }
    });
    let lab="";
    if(s.l){
      const sx=Object.assign({block:" — blocked",stop:" — idle",low:" — less active",boost:" — more active"},s.sfx||{});
      const suf=blocked?sx.block:stopped?sx.stop:closed?` — ${s.closed||"closed"}`:low?sx.low:boost?sx.boost:"";
      if(s.lx!==undefined){ const an=s.la||"middle";
        lab=`<text class="nf-l1" x="${s.lx}" y="${s.ly}" text-anchor="${an}">${esc(s.l+suf)}</text>`+(s.s?`<text class="nf-l2" x="${s.lx}" y="${s.ly+16}" text-anchor="${an}">${esc(s.s)}</text>`:""); }
      else if(vert){ const lx=s.x+nx*(h+46), an=nx<0?"end":"start";
        lab=`<text class="nf-l1" x="${lx}" y="${s.y-3}" text-anchor="${an}">${esc(s.l+suf)}</text><text class="nf-l2" x="${lx}" y="${s.y+13}" text-anchor="${an}">${esc(s.s||"")}</text>`; }
      else { const ly=s.y+ny*(h+(ny>0?50:36));
        lab=`<text class="nf-l1" x="${s.x}" y="${ny>0?ly:ly-16}" text-anchor="middle">${esc(s.l+suf)}</text><text class="nf-l2" x="${s.x}" y="${ny>0?ly+16:ly}" text-anchor="middle">${esc(s.s||"")}</text>`; }
    }
    const name=s.c&&LES[s.c]?LES[s.c].n:"";
    out.push(`<g class="nf-site${blocked||stopped||closed?" off":""}"${s.c?` data-plotles="${s.c}"`:""} tabindex="0" role="button" aria-label="${esc((s.l?s.l+": "+(s.s||""):s.aria||"Site")+(name?" — opens "+name:""))}">${ions}${ic}${lab}</g>`);
  });
  if(st.abg&&DYN_ABG[state.view]&&!hide) out.push(abgMarks(DYN_ABG[state.view],st));
  /* the switches, readouts and note — on the canvas here; phones also get them as an HTML sheet (dynSheetRender) */
  if(!DYN_NOPANEL) out.push(`<g class="nf-ctl">${dynPanelSvg(m,d,st)}</g>`);
  return out.join("");
}
/* ── the controls as data: the canvas panel and the phone sheet draw the same thing ── */
function dynSections(d,st){
  const S=[];

  if((d.groups||[]).length) S.push({h:d.groupsLabel||"Show",chips:d.groups.map(([g,l])=>{
    const k=Object.keys(d.kinds||{}).find(q=>d.kinds[q][0]===g); return {key:"g:"+g,l,on:!!st.on[g],dot:k?d.kinds[k][1]:null}; })});
  const toggles=(d.switches||[]).filter(s=>!s.type||s.type==="toggle");
  if(toggles.length) S.push({h:d.togglesLabel||"Switches",chips:toggles.map(s=>{ const on=!!st.sw[s.id];
    return {key:"t:"+s.id,l:on?(s.on||s.label):(s.off||"No "+s.label),on}; })});
  (d.switches||[]).filter(s=>s.type==="one"||s.type==="steps").forEach(s=>{
    const Q=st.quiz;
    if(Q&&Q.s===s.id){   // naming it: this switch's chips become the choices
      const chips=Q.ch.map((k,i)=>{ const o=s.options.find(x=>x[0]===k); return {key:"q:"+k,l:(Q.ans?(k===Q.k?"✓ ":k===Q.ans?"✗ ":""):(i+1)+" · ")+o[1],on:!!Q.ans&&k===Q.k}; });
      if(Q.ans&&NMIX){ const tp=topicOf(state.view);
        chips.push(NMIX.k<NMIX.n?{key:"quiz:mix",l:"Next map ›",on:true}:{key:"quiz:mix10",l:"Another 10",on:true});
        if(tp&&mixPool(tp[0]).length>=3) chips.push({key:"quiz:scope",l:NMIX.scope?"All moving maps":"Only "+tp[1],on:false});
        chips.push({key:"quiz:end",l:"Done",on:false}); }
      else if(Q.ans) chips.push({key:"quiz:new",l:"Another one",on:false},{key:"quiz:end",l:"Done",on:false});
      S.push({h:Q.ans?"Name it — the answer":"Name it — which one is on?",chips}); return; }
    const chips=s.options.map(([k,l],i)=>({key:"o:"+s.id+":"+k,l:(s.type==="steps"&&!/^(Phase|\d)/.test(l)?(i+1)+" · ":"")+l,on:st.sw[s.id]===k}));   // "Phase 0…" labels carry their own number
    if(s.type==="steps"){ chips.push({key:"n:"+s.id,l:"Next ›",on:false});
      if(s.auto) chips.push({key:"a:"+s.id,l:st.auto===s.id?"Stepping through":"Step through",on:st.auto===s.id}); }
    S.push({h:s.label,chips}); });
  /* the last row: a tour's own buttons while touring; otherwise the motion, Reset and the ways to study the map */
  const tail=st.tour?[{key:"tour:prev",l:"‹ Back",on:false},{key:"tour:next",l:st.tour.i<dynTour(d).length-1?"Next ›":"Start again",on:true},{key:"tour:auto",l:TOUR_T?"■ Stop":"▶ Play",on:!!TOUR_T},{key:"tour:end",l:"End the tour",on:false}]:[];
  tail.push({key:"pause",l:dynPaused(st)?"Play the motion":"Pause the motion",on:false},{key:"reset",l:"Reset",on:false});
  if(!st.tour){
    if((d.readouts||[]).length) tail.push({key:"p:on",l:st.pred?"Stop predicting":"Predict the arrows",on:!!st.pred});
    if((d.switches||[]).length) tail.push({key:"tour:go",l:"Tour",on:false});
    if(!st.quiz&&dynQuizable(d).length){ const r=nameitScores()[state.view]; tail.push({key:"quiz:new",l:r?`Name it · ${r[0]}/${r[1]}`:"Name it",on:false}); }
    if(st.cmp) tail.push({key:"cmp:show",l:"Side by side",on:true},{key:"cmp:off",l:"Unpin",on:false});
    else if(!(st.quiz&&!st.quiz.ans)) tail.push({key:"cmp:pin",l:"Compare",on:false});
    if(!(st.quiz&&!st.quiz.ans)) tail.push({key:"link",l:st.copied?"✓ Link copied":"Copy link",on:!!st.copied});
    if(DYN_ABG[state.view]&&!(st.quiz&&!st.quiz.ans)){ tail.push({key:"abg:open",l:st.abg?"Blood gas: "+abgShort(st.abg):"Check a blood gas",on:!!st.abg});
      if(st.abg) tail.push({key:"abg:clear",l:"Clear it",on:false}); } }
  S.push({h:"",chips:tail});
  return S;
}
const DYN_AR={"":"–",u:"↑",d:"↓",f:"↔"};
function dynReadouts(d,st){
  return (d.readouts||[]).map((r,i)=>{ let any=false, sum=0;
    (r.mods||[]).forEach(md=>{ if(dynAny(st,md.when)){ any=true; sum+=md.d; } });
    const dir=!any?"":sum>0?"u":sum<0?"d":"f";
    return {i,l:r.l,dir,a:DYN_AR[dir],cls:{"":"",u:" up",d:" down",f:" flat"}[dir]}; });
}
/* Predict it: the arrows are hidden, the reader guesses ↑ ↓ ↔ for every readout this state moves, then checks */
function dynNotes(d,st){
  const R=dynReadouts(d,st), live=R.filter(r=>r.dir), Q=st.quiz;
  if(Q&&!Q.ans){ const s=d.switches.find(x=>x.id===Q.s);
    return [`${NMIX?`Moving-map mix${NMIX.scope?" ("+(TOPICS.find(t=>t[0]===NMIX.scope)||["",""])[1]+")":""} ${NMIX.k+1} of ${NMIX.n} · ${NMIX.ok} right so far. `:""}Name it: one choice under “${s.label}” is switched on. Read the drawing${R.length?" and the results":""}, then pick it from the ${Q.ch.length} choices.`]; }
  if(st.pred&&!st.pred.chk) return [live.length
    ?"Predict: pick ↑, ↓ or ↔ for each result, then press Check. The explanation comes back when you check."
    :"Pick a drug, disease or lesion first — then predict which way each result moves."];
  const notes=[];
  Object.keys(d.notes||{}).forEach(k=>{ if(k&&dynHas(st,k)) notes.push(d.notes[k]); });
  if(!notes.length&&d.notes&&d.notes[""]) notes.push(d.notes[""]);
  if(Q&&Q.ans){ const s=d.switches.find(x=>x.id===Q.s), o=s.options.find(x=>x[0]===Q.k), p=s.options.find(x=>x[0]===Q.ans);
    const r=nameitScores()[state.view];
    notes.unshift((Q.ans===Q.k?`Right — it’s ${o[1]}.`:`It’s ${o[1]} (you picked ${p[1]}).`)+(NMIX?` Mix: ${NMIX.ok} of ${NMIX.k} right${NMIX.k>=NMIX.n?" — done.":"."}`:` ${st.qz.ok} of ${st.qz.n} so far`+(r&&r[1]>st.qz.n?` · ${r[0]} of ${r[1]} on this map, on this device.`:"."))); }
  if(st.tour){ const T=dynTour(d); notes.unshift(`Tour ${st.tour.i+1} of ${T.length} — ${T[st.tour.i].l}.`); }
  if(st.cmp&&!st.tour&&!Q) notes.push(`Pinned for comparing: ${st.cmp.l}. Change the switches, then press Side by side.`);
  if(st.pred&&st.pred.chk){ const ok=live.filter(r=>st.pred.g[r.i]===r.dir).length;
    notes.unshift(`You got ${ok} of ${live.length} right${ok===live.length?" — nice.":"."} Pick another switch to go again.`); }
  if(st.paused===null&&dynPaused(st)) notes.push("The motion is paused because this device asks for reduced motion — Play starts it.");
  return notes;
}
function dynPanelSvg(m,d,st){
  const P=d.panel||{x:m.w-1080,y:110,w:1000}, X0=P.x, W=P.w;
  let y=P.y+16, x=X0, ctl="";
  const chip=(key,label,on,dot,cls)=>{
    const w=Math.round(label.length*7.1+(dot?40:26));
    if(x+w>X0+W){ x=X0; y+=44; }
    const g=`<g class="nf-chip${on?" on":""}${cls||""}" data-dyn="${key}" tabindex="0" role="button" aria-pressed="${on}"><rect x="${x}" y="${y-21}" width="${w}" height="30" rx="15"/>${dot?`<circle cx="${x+16}" cy="${y-6}" r="6.5" fill="var(${dot})"/>`:""}<text x="${x+(dot?30:13)}" y="${y-1}">${esc(label)}</text></g>`;
    x+=w+8; return g;
  };
  const head=t=>{ x=X0; const g=`<text class="nf-h" x="${X0}" y="${y}">${esc(t.toUpperCase())}</text>`; y+=30; return g; };
  const S=dynSections(d,st);
  S.forEach((sec,i)=>{ if(sec.h) ctl+=head(sec.h); else x=X0;
    sec.chips.forEach(c=>{ ctl+=chip(c.key,c.l,c.on,c.dot); });
    if(i<S.length-1) y+=50; });
  /* readouts — or, while predicting, a guess for each */
  const R=dynReadouts(d,st);
  if(R.length){ y+=46; x=X0;
    ctl+=`<text class="nf-h" x="${X0}" y="${y}">${st.pred&&!st.pred.chk?"PREDICT":"RESULT"}</text>`;
    let rx=X0+90;
    const room=w=>{ if(rx+w>X0+W){ rx=X0+90; y+=40; } };
    R.forEach(r=>{
      if(st.pred&&!st.pred.chk&&r.dir){
        const lw=r.l.length*8.2+10; room(lw+3*34+18);
        ctl+=`<text class="nf-l1 dyn-rl" x="${rx}" y="${y}">${esc(r.l)}</text>`;
        let cx=rx+lw;
        ["u","d","f"].forEach(dd=>{ const on=st.pred.g[r.i]===dd;
          ctl+=`<g class="nf-chip dyn-g${on?" on":""}" data-dyn="p:g:${r.i}:${dd}" tabindex="0" role="button" aria-pressed="${on}" aria-label="${esc(r.l)} ${{u:"up",d:"down",f:"no change"}[dd]}"><rect x="${cx}" y="${y-19}" width="30" height="26" rx="13"/><text x="${cx+15}" y="${y-1}" text-anchor="middle">${DYN_AR[dd]}</text></g>`;
          cx+=34; });
        rx=cx+18;
      } else if(st.pred&&st.pred.chk&&r.dir){
        const ok=st.pred.g[r.i]===r.dir, w=r.l.length*8.2+70; room(w);
        ctl+=`<g class="dyn-ro${r.cls}"><text class="nf-l1" x="${rx}" y="${y}">${esc(r.l)}</text><text class="dyn-arrow" x="${rx+r.l.length*8.2+8}" y="${y+1}">${r.a}</text><text class="${ok?"dyn-ok":"dyn-bad"}" x="${rx+r.l.length*8.2+28}" y="${y+1}">${ok?"✓":"✗"}${!ok&&st.pred.g[r.i]?" "+DYN_AR[st.pred.g[r.i]]:""}</text></g>`;
        rx+=w;
      } else {
        const w=r.l.length*8.2+46; room(w);
        ctl+=`<g class="dyn-ro${r.cls}"><text class="nf-l1" x="${rx}" y="${y}">${esc(r.l)}</text><text class="dyn-arrow" x="${rx+r.l.length*8.2+8}" y="${y+1}">${r.a}</text></g>`;
        rx+=w;
      }
    });
    if(st.pred&&!st.pred.chk&&R.some(r=>r.dir)){ room(90);
      const any=Object.values(st.pred.g).some(Boolean);
      ctl+=`<g class="nf-chip on dyn-chk${any?"":" dis"}" data-dyn="p:chk" tabindex="0" role="button"><rect x="${rx}" y="${y-21}" width="76" height="30" rx="15"/><text x="${rx+16}" y="${y-1}">Check</text></g>`; }
  }
  /* what the current switches do */
  const notes=dynNotes(d,st);
  const per=Math.floor(W/7.3), lines=[];
  notes.forEach(t=>{ let cur=""; t.split(" ").forEach(wd=>{ if((cur+" "+wd).trim().length>per){ lines.push(cur.trim()); cur=wd; } else cur+=" "+wd; }); lines.push(cur.trim()); lines.push(""); });
  lines.pop();
  y+=34;
  ctl+=`<rect class="nf-note" x="${X0}" y="${y}" width="${W}" height="${lines.length*19+30}" rx="12"/>`+lines.map((t,i)=>`<text class="nf-nt" x="${X0+16}" y="${y+26+i*19}">${esc(t)}</text>`).join("")+
    (d.src?`<text class="nf-src" x="${X0+W}" y="${y+lines.length*19+50}" text-anchor="end">${esc(d.src)}</text>`:"");
  return ctl;
}
/* ── the phone sheet (≤ 1000 px wide): the same controls in HTML, docked under the map.
   "peek" (the default) is a slim bar — what's on, the result arrows, the note's first sentence; "full" opens every
   switch; "off" leaves a Switches button. Only "off" is remembered on this device. ── */
let DYNSHEET="peek"; try{ if(localStorage.getItem("mla-dynsheet")==="off") DYNSHEET="off"; }catch(e){}
function dynSheetRender(){
  const el=document.getElementById("dynSheet"), btn=document.getElementById("dynBtn"), wrap=document.getElementById("mapwrap");
  if(!el||!btn) return;
  const v=state.view, m=MAPS[v], kit=v!=="index"&&m&&m.art==="kit"&&m.dyn, open=kit&&DYNSHEET!=="off";
  el.hidden=!open; btn.hidden=!kit||open; if(wrap) wrap.classList.toggle("ds-open",!!open);
  if(!open) return;
  const d=m.dyn, st=dynSt(v), full=DYNSHEET==="full";
  el.classList.toggle("ds-full",full);
  let h=`<div class="ds-h"><b>${esc(m.t)}</b><span class="ds-hb"><button class="ds-x" data-dsmode="${full?"peek":"full"}" aria-expanded="${full}">${full?"Less ▾":"Switches ▴"}</button><button class="ds-x" data-dsmode="off" aria-label="Hide the switches">Hide</button></span></div>`;
  if(d.lazy){ el.innerHTML=h+`<p class="ds-note">${DYNFAIL[v]?"The drawing couldn’t load — check your connection, then reopen this map.":"Loading the drawing…"}</p>`; dynSheetSize(); return; }
  const secs=dynSections(d,st);
  if(full) secs.forEach(sec=>{
    h+=(sec.h?`<div class="ds-sh">${esc(sec.h)}</div>`:`<div class="ds-sh ds-gap"></div>`)+`<div class="ds-chips">${sec.chips.map(c=>
      `<button class="ds-chip${c.on?" on":""}" data-dyn="${c.key}" aria-pressed="${c.on}">${c.dot?`<span class="ds-dot" style="background:var(${c.dot})"></span>`:""}${esc(c.l)}</button>`).join("")}</div>`; });
  else if(st.tour||st.quiz){ const row=cs=>`<div class="ds-chips">${cs.map(c=>`<button class="ds-chip${c.on?" on":""}" data-dyn="${c.key}" aria-pressed="${c.on}">${esc(c.l)}</button>`).join("")}</div>`;
    if(st.tour) h+=row(secs[secs.length-1].chips.filter(c=>/^tour:/.test(c.key)));
    else secs.filter(sec=>/^Name it/.test(sec.h)).forEach(sec=>{ h+=`<div class="ds-sh">${esc(sec.h)}</div>`+row(sec.chips); }); }
  else { const on=[]; (d.switches||[]).forEach(s=>{ if(s.type==="one"||s.type==="steps"){ const o=s.options.find(x=>x[0]===st.sw[s.id]); if(o) on.push(o[1]); }
      else if(!!st.sw[s.id]!==(s.def!==false)) on.push(st.sw[s.id]?(s.on||s.label):(s.off||"No "+s.label)); });
    h+=`<p class="ds-now">${on.length?esc(on.join(" · ")):"Nothing switched on — tap Switches ▴ to pick a drug, disease or lesion"}</p>`;
    if(st.cmp) h+=`<div class="ds-chips"><button class="ds-chip on" data-dyn="cmp:show">Compare with: ${esc(st.cmp.l)}</button><button class="ds-chip" data-dyn="cmp:off">Unpin</button></div>`; }
  const R=dynReadouts(d,st);
  if(R.length){
    const pred=st.pred&&!st.pred.chk;
    h+=`<div class="ds-ro">`+R.map(r=>{
      if(pred&&r.dir) return `<span class="ds-r ds-p"><span class="ds-rl">${esc(r.l)}</span>${["u","d","f"].map(dd=>`<button class="ds-g${st.pred.g[r.i]===dd?" on":""}" data-dyn="p:g:${r.i}:${dd}" aria-pressed="${st.pred.g[r.i]===dd}" aria-label="${esc(r.l)} ${{u:"up",d:"down",f:"no change"}[dd]}">${DYN_AR[dd]}</button>`).join("")}</span>`;
      if(st.pred&&st.pred.chk&&r.dir){ const ok=st.pred.g[r.i]===r.dir;
        return `<span class="ds-r${r.cls}"><span class="ds-rl">${esc(r.l)}</span><b class="ds-a">${r.a}</b><span class="${ok?"ds-ok":"ds-bad"}">${ok?"✓":"✗"}</span></span>`; }
      return `<span class="ds-r${r.cls}"><span class="ds-rl">${esc(r.l)}</span><b class="ds-a">${r.a}</b></span>`; }).join("")+`</div>`;
    if(pred&&R.some(r=>r.dir)) h+=`<button class="ds-chip on ds-check" data-dyn="p:chk">Check</button>`;
  }
  const notes=dynNotes(d,st);
  if(full||st.tour||st.quiz) h+=notes.map(t=>`<p class="ds-note">${esc(t)}</p>`).join("")+(full&&d.src?`<p class="ds-src">${esc(d.src)}</p>`:"");
  else if(notes.length){ const t=notes[0], cut=t.search(/[.!?](\s|$)/), first=cut>0&&cut<t.length-1?t.slice(0,cut+1):t;
    h+=`<p class="ds-note ds-clip">${esc(first)}${first.length<t.length||notes.length>1?` <button class="ds-more" data-dsmode="full">more</button>`:""}</p>`; }
  const sc=el.scrollTop; el.innerHTML=h; el.scrollTop=sc; dynSheetSize();
}
/* the toolbar and the framing sit just above the sheet, however tall it is right now */
function dynSheetSize(){
  const el=document.getElementById("dynSheet"), wrap=document.getElementById("mapwrap"); if(!el||!wrap) return;
  wrap.style.setProperty("--ds-h",(el.hidden?0:Math.round(el.getBoundingClientRect().height))+"px");
}
function dynSheetInit(){
  const el=document.getElementById("dynSheet"), btn=document.getElementById("dynBtn");
  if(!el||!btn||el.dataset.bound) return; el.dataset.bound="1";
  el.addEventListener("click",ev=>{
    const b=ev.target.closest("[data-dyn]");
    if(b){ const key=b.dataset.dyn; if(DYNSHEET==="full"&&/^([otq]:|tour:go|quiz:new|cmp:show)/.test(key)) DYNSHEET="peek";   // pick, then see it on the map
      dynSet(key); return; }
    const md=ev.target.closest("[data-dsmode]"); if(md){ DYNSHEET=md.dataset.dsmode;
      try{ if(DYNSHEET==="off") localStorage.setItem("mla-dynsheet","off"); else localStorage.removeItem("mla-dynsheet"); }catch(e){}
      dynSheetRender(); if(DYNSHEET==="off") dynFrame(); } });
  btn.addEventListener("click",()=>{ DYNSHEET="peek"; try{ localStorage.removeItem("mla-dynsheet"); }catch(e){} dynSheetRender(); dynFrame(); });
  addEventListener("resize",()=>dynSheetSize());
}
/* On a phone a moving map opens framed on its drawing (above the sheet), not the whole canvas with the panel */
function dynFrame(){
  const m=MAPS[state.view]; if(!m||m.art!=="kit"||innerWidth>1000) return;
  const r=svg.getBoundingClientRect(); if(!r.width||!r.height) return;
  const s0=Math.min(r.width/m.w,r.height/m.h), sh=document.getElementById("dynSheet");
  const hb=sh&&!sh.hidden?sh.getBoundingClientRect().height:0, visH=Math.max(120,r.height-hb);
  const P=(m.dyn&&m.dyn.panel)||{x:m.w-1080}, x0=0, y0=0, x1=Math.max(600,P.x-40), y1=m.h;
  const z=Math.min(6,Math.max(1,Math.min(r.width/(s0*(x1-x0)),visH/(s0*(y1-y0)))));
  state.z=z; state.tx=-(r.width-s0*m.w)/(2*s0)-z*x0; state.ty=-(r.height-s0*m.h)/(2*s0)-z*y0; applyCam();
}
/* ── switch state in the address: #coagflow/~dz:hema,!adh — shareable, and how the question bank says "See it move" ── */
function dynStateStr(v){
  const m=MAPS[v]; if(!m||!m.dyn||!DYN[v]) return "";
  const st=DYN[v], t=[];
  if(st.quiz&&!st.quiz.ans) return "";   // the address must not give the answer away
  (m.dyn.switches||[]).forEach(s=>{ const val=st.sw[s.id];
    if(!s.type||s.type==="toggle"){ if(!!val!==(s.def!==false)) t.push((val?"":"!")+s.id); }
    else if(s.type==="one"){ if(val&&val!==(s.def||"")) t.push(s.id+":"+val); }
    else if(s.type==="steps"){ if(st.auto!==s.id&&val&&val!==(s.def||s.options[0][0])) t.push(s.id+":"+val); } });
  return t.join(",");
}
function dynApplyStr(v,str){
  const m=MAPS[v]; if(!m||!m.dyn) return;
  const keep=DYN[v]&&DYN[v].paused; delete DYN[v]; const st=dynSt(v); if(keep!=null) st.paused=keep;
  (str||"").split(",").filter(Boolean).forEach(tok=>{
    const neg=tok[0]==="!", t=neg?tok.slice(1):tok, i=t.indexOf(":"), a=i<0?t:t.slice(0,i), b=i<0?"":t.slice(i+1);
    const s=(m.dyn.switches||[]).find(q=>q.id===a); if(!s) return;
    if(!s.type||s.type==="toggle") st.sw[a]=!neg;
    else if(b&&s.options.some(o=>o[0]===b)){ st.sw[a]=b; if(s.type==="steps"&&st.auto===a) st.auto=null; } });
}
function dynRedraw(){
  const m=MAPS[state.view], w=svg.querySelector("#artWrap");
  if(w&&m&&m.art==="kit") w.innerHTML=kitArt(m);
  dynMotion();
}
/* ── lazy drawings: the build moves each map's drawing to resources/dyn/<map>.js and leaves {lazy, switches} here ── */
const DYNLOAD={}, DYNFAIL={};
function dynLoad(v){
  const m=MAPS[v]; if(!m||!m.dyn||!m.dyn.lazy||DYNLOAD[v]) return;
  DYNLOAD[v]=1; delete DYNFAIL[v];
  const s=document.createElement("script"); s.src="dyn/"+v+".js?v="+m.dyn.lazy; s.async=true;
  const fail=()=>{ DYNFAIL[v]=1; DYNLOAD[v]=0; s.remove(); if(state.view===v) dynRedraw(); };
  s.onload=()=>{ const D=window.DYNDATA&&window.DYNDATA[v]; if(!D) return fail();
    MAPS[v].dyn=D; const st=DYN[v]; if(st) (D.groups||[]).forEach(([g])=>{ if(!(g in st.on)) st.on[g]=1; });
    if(state.view===v) render(); };
  s.onerror=fail;
  document.head.appendChild(s);
}
/* once the first map is up, fetch the other drawings quietly so the offline copy has them all */
setTimeout(()=>{ try{
  if(!navigator.serviceWorker||!navigator.serviceWorker.controller) return;
  if(navigator.connection&&navigator.connection.saveData) return;
  Object.keys(MAPS).forEach(v=>{ const d=MAPS[v].dyn; if(d&&d.lazy) fetch("dyn/"+v+".js?v="+d.lazy).catch(()=>{}); });
}catch(e){} },8000);
/* ── search: the switches of every moving map ("hemophilia" → Coagulation Cascade with Hemophilia A on) ── */
function switchMatches(q){
  q=(q||"").trim().toLowerCase();
  if(q.length<3) return [];
  const words=q.split(/\s+/).filter(Boolean).map(w=>new RegExp("(^|[^a-z0-9])"+w.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")));
  const out=[];
  VIEWS.forEach(([v,title])=>{ const m=MAPS[v]; if(!m||m.art!=="kit"||!m.dyn) return;
    (m.dyn.switches||[]).forEach(s=>{ (s.options||[]).forEach(o=>{
      const card=o[2]&&LES[o[2]], hay=(o[1]+" "+(card?card.n+" "+(card.alias||""):"")).toLowerCase();
      if(words.every(re=>re.test(hay))) out.push({v,title,s:s.id,k:o[0],l:o[1],sl:s.label,t:words.every(re=>re.test(o[1].toLowerCase()))?1:0}); }); }); });
  return out.sort((a,b)=>b.t-a.t||(a.v===state.view?0:1)-(b.v===state.view?0:1));
}
function switchRowHtml(x,cls){
  const where=(x.v===state.view?"this map":x.title), go=x.v+"|"+x.s+":"+x.k;
  return cls==="li"?`<button class="li bx" data-dyngo="${go}" style="--c:var(--accent)"><span class="dot"></span><span><span class="nm">${esc(x.l)}</span><span class="bz">Moving map · ${esc(where)}</span></span></button>`
    :`<li><button class="idxrow" data-dyngo="${go}"><span class="t">${esc(x.l)}</span><span class="e">Moving map · ${esc(where)}</span></button></li>`;
}
function goSwitch(go){
  const [v,str]=go.split("|"); if(!MAPS[v]) return;
  if(state.view!==v) setView(v);
  dynApplyStr(v,str); dynRedraw(); writeHash();
}
function dynSet(k,timer){
  const v=state.view, m=MAPS[v]; if(!m||!m.dyn||m.dyn.lazy) return;
  const st=dynSt(v), [a,b,c,dd]=k.split(":"), sw=(m.dyn.switches||[]).find(q=>q.id===b);
  if(a==="g") st.on[b]=st.on[b]?0:1;
  else if(a==="t") st.sw[b]=!st.sw[b];
  else if(a==="o"&&sw&&sw.type==="steps"){ st.sw[b]=c; st.auto=null; }
  else if(a==="o") st.sw[b]=st.sw[b]===c?"":c;
  else if(a==="n"&&sw){ const ks=sw.options.map(o=>o[0]); st.sw[b]=ks[(ks.indexOf(st.sw[b])+1)%ks.length]; if(!timer) st.auto=null; }
  else if(a==="a"&&sw){ st.auto=st.auto===b?null:b; if(st.auto&&dynPaused(st)) st.paused=false; if(st.auto) st.pred=null; }
  else if(a==="pause") st.paused=!dynPaused(st);
  else if(a==="reset"){ delete DYN[v]; dynSt(v).paused=st.paused; }
  else if(a==="tour"){ const T=dynTour(m.dyn);
    if(b==="auto"){ if(TOUR_T) tourStop(); else tourPlay(v); }
    else if(b==="end"){ st.tour=null; tourStop(); }
    else { const i=b==="go"?0:b==="next"?((st.tour?st.tour.i:-1)+1)%T.length:Math.max(0,(st.tour?st.tour.i:0)-1);
      dynGo(v,T[i].str,{tour:{i},quiz:null}); } }
  else if(a==="quiz"){ if(b==="mix"){ nameMixNext(); return; } if(b==="mix10"){ startNameMix(NMIX&&NMIX.scope); return; }
    if(b==="scope"&&NMIX){ const tp=topicOf(v); NMIX.scope=NMIX.scope?null:tp&&tp[0]; }
    else
    if(b==="end"){ st.quiz=null; NMIX=null; } else { NMIX=null; dynQuiz(v); } }
  else if(a==="q"&&st.quiz&&!st.quiz.ans){ const ok=b===st.quiz.k; st.quiz.ans=b; st.qz.n++; if(ok) st.qz.ok++; nameitSave(v,ok,st.quiz.s+":"+st.quiz.k); if(NMIX){ NMIX.k++; if(ok) NMIX.ok++; } }
  else if(a==="link"){ writeHash(); const u=location.href;
    try{ navigator.clipboard.writeText(u).then(()=>{ const s2=DYN[v]; if(!s2) return; s2.copied=true; dynRedraw(); setTimeout(()=>{ if(DYN[v]){ DYN[v].copied=false; if(state.view===v) dynRedraw(); } },1800); },()=>{ prompt("Copy this link:",u); }); }catch(e){ prompt("Copy this link:",u); }
    return; }
  else if(a==="abg"){ if(b==="open"){ dynAbg(v); return; } st.abg=null; }
  else if(a==="cmp"){ if(b==="pin") st.cmp={str:dynStateStr(v),l:dynStateLabel(m.dyn,st)}; else if(b==="off") st.cmp=null; else if(b==="show"){ dynCompare(v); return; } }
  else if(a==="p"){
    if(b==="on"){ st.pred=st.pred?null:{g:{},chk:false}; if(st.pred) st.auto=null; }   // predicting holds the phase still
    else if(b==="g"&&st.pred&&!st.pred.chk) st.pred.g[c]=st.pred.g[c]===dd?undefined:dd;
    else if(b==="chk"&&st.pred&&!st.pred.chk&&Object.values(st.pred.g).some(Boolean)){ st.pred.chk=true;
      const live=dynReadouts(m.dyn,st).filter(r=>r.dir); predictSave(v,live.filter(r=>st.pred.g[r.i]===r.dir).length,live.length); }
  }
  if(st.pred&&(a==="t"||a==="o"||a==="n")) st.pred={g:{},chk:false};   // a new state: guess again
  if(a==="t"||a==="o"||a==="n"||a==="reset"){ const s2=DYN[v]; if(s2&&!timer){ s2.tour=null; s2.quiz=null; NMIX=null; tourStop(); } }   // a switch by hand ends a tour or a question
  const w=svg.querySelector("#artWrap"); if(!w) return;
  if((a==="tour"||a==="quiz")&&!timer) dynFrame();
  const ae=document.activeElement, fk=ae&&w.contains(ae)&&ae.dataset?ae.dataset.dyn:null;   // keep keyboard focus through a re-draw
  w.innerHTML=kitArt(m);
  if(!timer){ dynMotion(); writeHash(); } else dynSheetRender();
  const el=w.querySelector(`[data-dyn="${timer?fk:k}"]`);
  if(el){ FOCUS_QUIET=true; try{ el.focus({preventScroll:true}); }catch(e){} FOCUS_QUIET=false; }
}
/* ── m42: Tour, Name it, Compare ── */
let DYN_NOPANEL=false;
/* the tour: as it opens, then every switch in order — a toggle flipped, each option of the others */
function dynTour(d){
  const L=[{str:"",l:"As it opens"}];
  (d.switches||[]).forEach(s=>{
    if(!s.type||s.type==="toggle"){ const on=s.def!==false; L.push({str:(on?"!":"")+s.id,l:on?(s.off||"No "+s.label):(s.on||s.label)}); }
    else s.options.forEach(o=>L.push({str:s.id+":"+o[0],l:o[1]})); });
  return L;
}
/* go to a state, keeping what rides along (pause, the tour, a question, the pinned state) */
function dynGo(v,str,carry){
  const o=DYN[v]||{}; dynApplyStr(v,str); const st=DYN[v];
  ["tour","quiz","qz","cmp"].forEach(k=>{ if(o[k]!==undefined) st[k]=o[k]; });
  if(o.on) st.on=Object.assign({},o.on);
  Object.assign(st,carry||{}); st.auto=null; st.pred=null; return st;
}
/* Name it asks about a drug / disease / lesion (a "one" switch); the phases of a cycle only on a map with nothing else */
const dynQuizable=d=>{ const ok=t=>(d.switches||[]).filter(s=>s.type===t&&s.options.length>=3); const o=ok("one"); return o.length?o:ok("steps"); };
function dynQuiz(v,want){
  const d=MAPS[v].dyn, Sw=dynQuizable(d); if(!Sw.length) return;
  const all=[]; Sw.forEach(s=>s.options.forEach(o=>all.push([s,o[0]])));
  const last=DYN[v]&&DYN[v].quiz?DYN[v].quiz.k:null, pool=all.filter(x=>x[1]!==last);
  const miss=nitMissed([v]).map(([,sw,o])=>all.find(x=>x[0].id===sw&&x[1]===o)).filter(x=>x&&x[1]!==last);
  const [s,k]=(want&&all.find(x=>x[0].id===want[0]&&x[1]===want[1]))||(miss.length?miss[Math.floor(Math.random()*miss.length)]:pool[Math.floor(Math.random()*pool.length)]);
  const others=s.options.map(o=>o[0]).filter(x=>x!==k).sort(()=>Math.random()-.5).slice(0,3);
  const ch=others.concat([k]).sort(()=>Math.random()-.5);
  const qz=(DYN[v]&&DYN[v].qz)||{n:0,ok:0};
  dynGo(v,s.id+":"+k,{quiz:{s:s.id,k,ch,ans:null},qz,tour:null});
}
/* Name it and Predict, remembered per map in the atlas progress (synced with the PIN, sync.js mergeAtlas):
   PROG.nit {map: [right, asked]} · PROG.prd {map: [arrows right, arrows asked]} · PROG.nitm {"map|switch:option": misses not yet
   put right} — a missed option comes back first, until it is named right */
try{ const old=JSON.parse(localStorage.getItem("mla-nameit")||"null");   // m43–m44 kept Name-it scores on their own
  if(old&&typeof old==="object"){ Object.keys(old).forEach(v=>{ const a=PROG.nit[v]||[0,0], b=old[v]||[0,0]; PROG.nit[v]=[Math.max(a[0],b[0]),Math.max(a[1],b[1])]; });
    saveProg(); localStorage.removeItem("mla-nameit"); } }catch(e){}
const nameitScores=()=>PROG.nit;
function nameitSave(v,ok,item){ const r=(PROG.nit[v]||[0,0]).slice(); r[1]++; if(ok) r[0]++; PROG.nit[v]=r;
  const key=v+"|"+item; if(ok) delete PROG.nitm[key]; else PROG.nitm[key]=(PROG.nitm[key]||0)+1; saveProg(); }
function predictSave(v,ok,n){ const r=(PROG.prd[v]||[0,0]).slice(); r[0]+=ok; r[1]+=n; PROG.prd[v]=r; saveProg(); }
/* the options named wrong and not yet put right, on these maps: [[map, switch, option], …] */
const nitMissed=maps=>Object.keys(PROG.nitm).map(k=>{ const [v,so]=k.split("|"), [sw,o]=(so||"").split(":"); return [v,sw,o]; })
  .filter(([v,sw,o])=>maps.includes(v)&&MAPS[v]&&MAPS[v].dyn&&(MAPS[v].dyn.switches||[]).some(x=>x.id===sw&&x.options.some(y=>y[0]===o)));
/* Quiz → Moving-map mix: ten Name-it questions, each on a random moving map */
let NMIX=null;
const topicOf=v=>TOPICS.find(t=>t[2].includes(v));
const mixPool=scope=>VIEWS.map(x=>x[0]).filter(v=>MAPS[v]&&MAPS[v].art==="kit"&&MAPS[v].dyn&&dynQuizable(MAPS[v].dyn).length&&(!scope||(topicOf(v)||[])[0]===scope));
function startNameMix(scope){ NMIX={k:0,n:10,ok:0,scope:scope||null}; nameMixNext(); }
function nameMixNext(){
  if(!NMIX) return;
  let pool=mixPool(NMIX.scope).filter(v=>v!==state.view); if(!pool.length) pool=mixPool(NMIX.scope);
  const miss=nitMissed(pool), want=miss.length?miss[Math.floor(Math.random()*miss.length)]:null;
  const v=want?want[0]:pool[Math.floor(Math.random()*pool.length)], mix=NMIX;
  if(state.view!==v) setView(v);
  NMIX=mix;   // setView may end a quiz; the mix carries on
  const go=n=>{ if(state.view!==v||NMIX!==mix) return; const d=MAPS[v].dyn;
    if(d.lazy){ if(!DYNFAIL[v]&&n<100) setTimeout(()=>go(n+1),100); return; }
    dynQuiz(v,want&&[want[1],want[2]]); dynRedraw(); writeHash(); dynFrame(); };
  go(0);
}
/* the tour plays itself: the next stop every 6 s, ending on the last */
let TOUR_T=null;
function tourStop(){ if(TOUR_T){ clearInterval(TOUR_T); TOUR_T=null; } }
function tourPlay(v){ tourStop();
  TOUR_T=setInterval(()=>{ const st=DYN[v]; if(state.view!==v||!st||!st.tour){ tourStop(); return; }
    if(st.tour.i>=dynTour(MAPS[v].dyn).length-1){ tourStop(); dynRedraw(); return; }
    dynSet("tour:next",true); },6000); }
/* open a moving map straight into Name it (the Index's weakest maps) */
function goNameIt(v){ if(!MAPS[v]) return; NMIX=null; if(state.view!==v) setView(v);
  const go=n=>{ if(state.view!==v) return; if(MAPS[v].dyn.lazy){ if(!DYNFAIL[v]&&n<100) setTimeout(()=>go(n+1),100); return; } dynQuiz(v); dynRedraw(); writeHash(); dynFrame(); };
  go(0); }
/* keys on a moving map: ← → step a tour; 1–4 name it, Enter for the next question */
function dynKey(ev){
  const v=state.view, m=MAPS[v], st=m&&m.art==="kit"&&m.dyn&&!m.dyn.lazy&&DYN[v];
  if(!st||ev.metaKey||ev.ctrlKey||ev.altKey||/^(INPUT|TEXTAREA|SELECT)$/.test((document.activeElement||{}).tagName||"")) return false;
  if(st.tour&&(ev.key==="ArrowRight"||ev.key==="ArrowLeft")){ dynSet(ev.key==="ArrowRight"?"tour:next":"tour:prev"); return true; }
  if(st.quiz&&!st.quiz.ans&&/^[1-4]$/.test(ev.key)&&st.quiz.ch[+ev.key-1]){ dynSet("q:"+st.quiz.ch[+ev.key-1]); return true; }
  const k=ev.key.toLowerCase();
  if(!st.quiz||st.quiz.ans){
    if(k==="t"&&!st.tour){ dynSet("tour:go"); return true; }
    if(k==="n"&&dynQuizable(m.dyn).length){ dynSet("quiz:new"); return true; }
    if(k==="p"&&(m.dyn.readouts||[]).length&&!st.tour){ dynSet("p:on"); return true; }
    if(k==="c"&&!st.tour){ dynSet(st.cmp?"cmp:show":"cmp:pin"); return true; } }
  if(st.quiz&&st.quiz.ans&&ev.key==="Enter"){ dynSet(NMIX?(NMIX.k<NMIX.n?"quiz:mix":"quiz:mix10"):"quiz:new"); return true; }
  return false;
}
/* what is switched on, in words */
function dynStateLabel(d,st){
  const on=[]; (d.switches||[]).forEach(s=>{
    if(s.type==="one"||s.type==="steps"){ const o=s.options.find(x=>x[0]===st.sw[s.id]); if(o&&(s.type==="one"||st.auto!==s.id)) on.push(o[1]); }
    else if(!!st.sw[s.id]!==(s.def!==false)) on.push(st.sw[s.id]?(s.on||s.label):(s.off||"No "+s.label)); });
  return on.length?on.join(" · "):"As it opens";
}
/* Compare: the pinned state and the current one, side by side (stacked on a phone) */
function dynCompare(v){
  const m=MAPS[v], d=m.dyn, cur=DYN[v]; if(!cur||!cur.cmp||d.lazy) return;
  const P=d.panel||{x:m.w-1080}, W=Math.max(600,P.x-40);
  const side=(str,tag)=>{
    dynApplyStr(v,str); const s2=DYN[v]; s2.on=Object.assign({},cur.on); s2.paused=cur.paused; s2.auto=null;
    DYN_NOPANEL=true; let art=""; try{ art=kitArt(m); }finally{ DYN_NOPANEL=false; }
    const R=dynReadouts(d,s2), notes=dynNotes(d,s2).filter(t=>!/^Pinned for comparing/.test(t)), l=dynStateLabel(d,s2);
    DYN[v]=cur; return {art,R,notes,l,tag};
  };
  const A=side(cur.cmp.str,"A"), B=side(dynStateStr(v)||"","B");
  const diff=i=>A.R[i]&&B.R[i]&&A.R[i].dir!==B.R[i].dir;
  const col=X=>`<section class="dcmp-col"><h4><span class="dcmp-tag">${X.tag}</span>${esc(X.l)}</h4>
    <svg class="dcmp-art" viewBox="0 0 ${W} ${m.h}" role="img" aria-label="${esc(m.t)} — ${esc(X.l)}">${X.art}</svg>
    ${X.R.length?`<div class="ds-ro">${X.R.map((r,i)=>`<span class="ds-r${r.cls}${diff(i)?" dcmp-diff":""}"><span class="ds-rl">${esc(r.l)}</span><b class="ds-a">${r.a}</b></span>`).join("")}</div>`:""}
    ${X.notes.map(t=>`<p class="ds-note">${esc(t)}</p>`).join("")}</section>`;
  const old=document.getElementById("dynCmp"); if(old) old.remove();
  const el=document.createElement("div"); el.id="dynCmp"; el.className="dcmp"; el.setAttribute("role","dialog"); el.setAttribute("aria-modal","true");
  el.setAttribute("aria-label","Compare two states of "+m.t);
  el.innerHTML=`<div class="dcmp-box"><div class="dcmp-h"><b>${esc(m.t)} — compare</b><span class="ds-hb"><button class="ds-x" data-cmpb title="Pin B, then change the switches for a new comparison">Pin B instead</button><button class="ds-x" data-cmpx>Close</button></span></div>
    ${A.R.some((r,i)=>diff(i))?`<p class="dcmp-sub">Results that differ are underlined.</p>`:""}<div class="dcmp-cols">${col(A)}${col(B)}</div></div>`;
  document.body.appendChild(el);
  const back=document.activeElement;
  const close=()=>{ el.remove(); removeEventListener("keydown",key,true); try{ back&&back.focus({preventScroll:true}); }catch(e){} };
  const key=e=>{ if(e.key==="Escape"){ e.preventDefault(); e.stopPropagation(); close(); } };
  addEventListener("keydown",key,true);
  el.addEventListener("click",e=>{
    if(e.target.closest("[data-cmpb]")){ cur.cmp={str:dynStateStr(v),l:dynStateLabel(d,cur)}; close(); dynRedraw(); return; }
    if(e.target===el||e.target.closest("[data-cmpx]")) close(); });
  el.querySelectorAll("svg").forEach(s=>{ try{ if(dynPaused(cur)) s.pauseAnimations(); }catch(e){} });
  const x=el.querySelector("[data-cmpx]"); if(x) x.focus();
}
/* ── ABG calculator (drafts, 2026-10): type a blood gas on a map that lists itself in DYN_ABG — the disorder, the
   expected compensation, and the values marked on the map's own graphs at the current time step. The rules are the
   ones the acid–base timeline (abtime) draws: Winters; PaCO₂ +0.6 per HCO₃⁻ in metabolic alkalosis; HCO₃⁻ +1/+3 per
   10 mm Hg in respiratory acidosis and −2/−4 in respiratory alkalosis (acute/chronic). Keep the two in step.
   plots: [key, x0, x1, top, height, low, high] in canvas px and units; cols: the time step's column centres. ── */
const DYN_ABG={
  abtime:{plots:{ph:[420,2320,1180,220,7.0,7.7],pco2:[420,2320,1460,220,20,70],hco3:[420,2320,1740,220,8,40]},
          step:"time",cols:{sec:657,min:1132,day:1607,days:2082},dz:"dz",
          go:{ma:"ma",malk:"malk",ara:"ara",cra:"cra",aralk:"aralk",cralk:"cralk",mxra:"mxra"},
          time:{ma:"day",malk:"day",ara:"min",cra:"days",aralk:"min",cralk:"days",mxra:"day"}}
};
// UNVERIFIED: the normal ranges (pH 7.35–7.45, PaCO₂ 35–45, HCO₃⁻ 22–26) — standard values, not yet checked against First Aid
const ABG_N={ph:[7.35,7.45],pco2:[35,45],hco3:[22,26]};
const abgShort=g=>`${g.ph.toFixed(2)} / ${Math.round(g.pco2)} / ${Math.round(g.hco3)}`;
const r1=x=>Math.round(x*10)/10;
/* reads a blood gas: {lines:[…], go:map key of the matching disorder or ""} */
function abgRead(ph,pco2,hco3){
  const L=[], hh=6.1+Math.log10(hco3/(0.03*pco2));
  if(Math.abs(hh-ph)>0.05) L.push(`Check the numbers: from PaCO₂ and HCO₃⁻, Henderson–Hasselbalch gives pH ${hh.toFixed(2)}, not ${ph.toFixed(2)}.`);
  const acid=ph<ABG_N.ph[0], alk=ph>ABG_N.ph[1], hiC=pco2>ABG_N.pco2[1], loC=pco2<ABG_N.pco2[0], loB=hco3<ABG_N.hco3[0], hiB=hco3>ABG_N.hco3[1];
  let go="";
  const off=(meas,exp,tol,hi,lo)=>meas>exp+tol?hi:meas<exp-tol?lo:"";
  if(acid&&loB){
    const e=1.5*hco3+8; go="ma";
    L.push(`Acidemia with a low HCO₃⁻: metabolic acidosis.`,`Winters: expected PaCO₂ = 1.5 × ${r1(hco3)} + 8 = ${r1(e)} ± 2; measured ${r1(pco2)}.`);
    const x=off(pco2,e,2,"PaCO₂ is above the expected range — a respiratory acidosis as well.","PaCO₂ is below the expected range — a respiratory alkalosis as well.");
    L.push(x||"Within the range: an appropriately compensated metabolic acidosis."); if(x&&pco2>e) go="mxra";
  } else if(acid&&hiC){
    const a=24+0.1*(pco2-40), c=24+0.3*(pco2-40); go="ara";
    L.push(`Acidemia with a high PaCO₂: respiratory acidosis.`,`Expected HCO₃⁻: acute ${r1(a)}, chronic ${r1(c)}; measured ${r1(hco3)}.`);
    if(hco3<a-2) L.push("HCO₃⁻ is below even the acute value — a metabolic acidosis as well.");
    else if(hco3>c+2) L.push("HCO₃⁻ is above even the chronic value — a metabolic alkalosis as well.");
    else if(hco3>=c-1){ go="cra"; L.push("Near the chronic value: the kidneys have compensated (chronic)."); }
    else if(hco3<=a+1) L.push("Near the acute value: the kidneys have not yet acted (acute).");
    else L.push("Between the two: acute-on-chronic, or the kidneys partway there.");
  } else if(alk&&hiB){
    const e=40+0.6*(hco3-24); go="malk";
    L.push(`Alkalemia with a high HCO₃⁻: metabolic alkalosis.`,`Expected PaCO₂ ≈ 40 + 0.6 × ${r1(hco3-24)} = ${r1(e)}; measured ${r1(pco2)}.`);
    // UNVERIFIED: the ± 2 tolerance here is a display choice (the rule gives a point, not a range)
    L.push(off(pco2,e,2,"PaCO₂ is well above that — a respiratory acidosis as well.","PaCO₂ is well below that — a respiratory alkalosis as well.")||"Close to it: an appropriately compensated metabolic alkalosis.");
  } else if(alk&&loC){
    const a=24-0.2*(40-pco2), c=24-0.4*(40-pco2); go="aralk";
    L.push(`Alkalemia with a low PaCO₂: respiratory alkalosis.`,`Expected HCO₃⁻: acute ${r1(a)}, chronic ${r1(c)}; measured ${r1(hco3)}.`);
    if(hco3>a+2) L.push("HCO₃⁻ is above even the acute value — a metabolic alkalosis as well.");
    else if(hco3<c-2) L.push("HCO₃⁻ is below even the chronic value — a metabolic acidosis as well.");
    else if(hco3<=c+1){ go="cralk"; L.push("Near the chronic value: the kidneys have compensated (chronic)."); }
    else if(hco3>=a-1) L.push("Near the acute value: the kidneys have not yet acted (acute).");
    else L.push("Between the two: the kidneys partway there.");
  } else if(acid||alk){
    L.push(`${acid?"Acidemia":"Alkalemia"}, but neither PaCO₂ nor HCO₃⁻ moves the way that explains it — recheck the numbers.`);
  } else if((hiC&&hiB)||(loC&&loB)){
    L.push("pH in the normal range, but PaCO₂ and HCO₃⁻ have both moved: two disorders pulling pH opposite ways (e.g., salicylate overdose), or a fully compensated one — compensation rarely brings pH all the way back.");
  } else if(hiC||loC||loB||hiB) L.push("pH in the normal range with one value off — look again, or think of a mild or mixed disorder.");
  else L.push("All three in the normal range.");
  return {lines:L,go};
}
function abgMarks(cfg,st){
  const g=st.abg, x=cfg.cols[st.sw[cfg.step]]||cfg.plots.ph[1]-60; let s="";
  [["ph",g.ph,v=>v.toFixed(2)],["pco2",g.pco2,v=>Math.round(v)],["hco3",g.hco3,v=>Math.round(v)]].forEach(([k,v,f])=>{
    const [,,top,h,lo,hi]=cfg.plots[k], c=Math.max(lo,Math.min(hi,v)), y=Math.round(top+h-(c-lo)/(hi-lo)*h), out=v!==c;
    s+=`<path d="M${x} ${y-15} L${x+15} ${y} L${x} ${y+15} L${x-15} ${y} Z" style="fill:var(--bad);stroke:var(--surface);stroke-width:3"/>`+
       `<text class="nf-l1" x="${x-22}" y="${y+5}" text-anchor="end">patient ${f(v)}${out?(v>hi?" ▲":" ▼"):""}</text>`; });
  return s;
}
function dynAbg(v){
  const m=MAPS[v], st=DYN[v]||dynSt(v), cfg=DYN_ABG[v]; if(!cfg) return;
  const g=st.abg||{ph:7.27,pco2:26,hco3:12};
  const old=document.getElementById("dynAbg"); if(old) old.remove();
  const el=document.createElement("div"); el.id="dynAbg"; el.className="dcmp"; el.setAttribute("role","dialog"); el.setAttribute("aria-modal","true");
  el.setAttribute("aria-label","Check a blood gas");
  const inp=(k,l,step,val)=>`<label class="abg-f"><span>${l}</span><input type="number" inputmode="decimal" step="${step}" data-abg="${k}" value="${val}"></label>`;
  el.innerHTML=`<div class="dcmp-box abg-box"><div class="dcmp-h"><b>Check a blood gas</b><span class="ds-hb"><button class="ds-x" data-abgx>Close</button></span></div>
    <div class="abg-row">${inp("ph","pH","0.01",g.ph)}${inp("pco2","PaCO₂ (mm Hg)","1",g.pco2)}${inp("hco3","HCO₃⁻ (mEq/L)","1",g.hco3)}</div>
    <div class="abg-out" aria-live="polite"></div>
    <div class="abg-row"><button class="ds-x abg-go" data-abggo>Show it on the graphs</button></div>
    <p class="dcmp-sub">Uses the rules this map draws. A study aid, not for patient care.</p></div>`;
  document.body.appendChild(el);
  const val=()=>{ const o={}; el.querySelectorAll("[data-abg]").forEach(i=>{ o[i.dataset.abg]=parseFloat(i.value); }); return o; };
  const ok=o=>o.ph>=6.8&&o.ph<=7.8&&o.pco2>=10&&o.pco2<=130&&o.hco3>=2&&o.hco3<=60;
  const out=el.querySelector(".abg-out"), go=el.querySelector("[data-abggo]");
  const upd=()=>{ const o=val(); if(!ok(o)){ out.innerHTML=`<p class="ds-note">Enter pH 6.8–7.8, PaCO₂ 10–130 and HCO₃⁻ 2–60.</p>`; go.disabled=true; return; }
    go.disabled=false; out.innerHTML=abgRead(o.ph,o.pco2,o.hco3).lines.map(t=>`<p class="ds-note">${esc(t)}</p>`).join(""); };
  el.addEventListener("input",upd); upd();
  const back=document.activeElement;
  const close=()=>{ el.remove(); removeEventListener("keydown",key,true); try{ back&&back.focus({preventScroll:true}); }catch(e){} };
  const key=e=>{ if(e.key==="Escape"){ e.preventDefault(); e.stopPropagation(); close(); } };
  addEventListener("keydown",key,true);
  el.addEventListener("click",e=>{
    if(e.target.closest("[data-abggo]")){ const o=val(); if(!ok(o)) return; const r=abgRead(o.ph,o.pco2,o.hco3), s2=DYN[v]||dynSt(v);
      if(r.go&&cfg.go[r.go]){ s2.sw[cfg.dz]=cfg.go[r.go]; if(cfg.time[r.go]) s2.sw[cfg.step]=cfg.time[r.go]; s2.auto=null; }
      s2.abg=o; s2.tour=null; s2.quiz=null; s2.pred=null; close(); dynRedraw(); return; }
    if(e.target===el||e.target.closest("[data-abgx]")) close(); });
  const f=el.querySelector("[data-abg]"); if(f) f.focus();
}
const ART={ kit:kitArt };
