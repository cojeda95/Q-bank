/* Lesion Atlas data check — run by build-atlas.py, never by hand.

   build-atlas.py concatenates the atlas's data section (PATHS, MK, LES, MAPS,
   VIEWS) in front of this file and runs the result under JavaScriptCore, the
   engine macOS ships with (no Node on this Mac). Evaluating the real objects
   catches what a regex over the source cannot: an edge naming a node that does
   not exist, a duplicate node id, a pathway key with no colour, a ghost node
   pointing at a missing map, unbalanced <b> tags that bleed bold down a card.

   Prints one JSON line: {errors, warnings, cards}. `cards` carries each card's
   first home, which build-atlas.py compares with tools/atlas-homes.json and
   uses to write resources/atlas-terms.js for the question bank. */

(function(){
  const errors=[], warnings=[];
  const err=m=>errors.push(m), warn=m=>warnings.push(m);
  const has=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);

  /* ── views ─────────────────────────────────────────── */
  const viewIds=VIEWS.map(v=>v[0]);
  const seenView=new Set();
  viewIds.forEach(v=>{ if(seenView.has(v)) err(`VIEWS lists "${v}" twice`); seenView.add(v); });
  Object.keys(MAPS).forEach(v=>{ if(!viewIds.includes(v)) err(`map "${v}" is defined but has no tab in VIEWS — unreachable`); });
  viewIds.forEach(v=>{ if(v!=="index"&&!has(MAPS,v)) err(`VIEWS has a "${v}" tab but no MAPS.${v}`); });
  Object.keys(LES).forEach(id=>{ if(viewIds.includes(id)) err(`card id "${id}" is also a view id — #${id} links would be ambiguous`); });
  /* the top bar groups views into topics; each view must sit in exactly one */
  if(typeof TOPICS!=="undefined"){
    const inTopic={};
    TOPICS.forEach(([t,l,vs])=>vs.forEach(v=>{
      if(!viewIds.includes(v)) err(`topic "${t}" lists "${v}", which is not a view`);
      if(inTopic[v]) err(`view "${v}" is in two topics ("${inTopic[v]}" and "${t}")`);
      inTopic[v]=t;
    }));
    viewIds.forEach(v=>{ if(!inTopic[v]) err(`view "${v}" is in no topic — it has no button in the top bar`); });
  }

  /* ── cards ─────────────────────────────────────────── */
  const TAGS=["b","i","em","strong","sup","sub"];
  function htmlProblems(txt){
    const out=[];
    TAGS.forEach(t=>{
      const open=(txt.match(new RegExp("<"+t+"(\\s[^>]*)?>","g"))||[]).length;
      const close=(txt.match(new RegExp("</"+t+">","g"))||[]).length;
      if(open!==close) out.push(`<${t}> opened ${open}× but closed ${close}×`);
    });
    const stray=txt.match(/<(?!\/?(?:b|i|em|strong|sup|sub|br)\b)[A-Za-z!\/]/g);
    if(stray) out.push(`raw "<" starts what the browser will read as a tag (${stray.join(" ")}) — write &lt;`);
    return out;
  }
  Object.entries(LES).forEach(([id,L])=>{
    if(!/^[a-z0-9_]+$/.test(id)) err(`${id}: card ids must be lowercase letters, digits or _ (they go in URLs)`);
    if(typeof L.n!=="string"||!L.n.trim()) err(`${id}: missing name (n)`);
    if(!has(MK,L.k)) err(`${id}: marker kind "${L.k}" is not one of ${Object.keys(MK).join(", ")}`);
    if(!has(PATHS,L.p)) err(`${id}: pathway "${L.p}" is not in PATHS — no colour, no filter`);
    if(typeof L.mech!=="string"||!L.mech.trim()) err(`${id}: missing mechanism (mech)`);
    ["find","labs","buzz","tx"].forEach(f=>{
      if(L[f]===undefined) return;
      if(!Array.isArray(L[f])) err(`${id}: ${f} must be an array`);
      else L[f].forEach((x,i)=>{ if(typeof x!=="string") err(`${id}: ${f}[${i}] is not a string`); });
    });
    ["mech","find","labs","tx"].forEach(f=>{
      const txt=[].concat(L[f]||[]).join(" ‖ ");
      htmlProblems(txt).forEach(p=>err(`${id}: ${f} — ${p}`));
    });
    if(!(L.find&&L.find.length)&&!(L.labs&&L.labs.length)) warn(`${id}: no find or labs — the pin quiz has no clue to show`);
  });

  /* ── maps ──────────────────────────────────────────── */
  const ARROWS=[undefined,"one","both","none","inhib"];
  const nodeBox=n=>{ const cw=n.k==="ghost"?6.7:7.45;
    const w=n.w||Math.max(82,n.l.length*cw+26,n.s?n.s.length*5.9+26:0);
    return {w,h:n.s?46:34,x:n.x-w/2,y:n.y-(n.s?23:17)}; };
  const pinned={};
  Object.entries(MAPS).forEach(([v,m])=>{
    const where=`MAPS.${v}`;
    if(!(m.w>0&&m.h>0)) err(`${where}: needs a positive w and h`);
    if(!Array.isArray(m.nodes)||!Array.isArray(m.edges)){ err(`${where}: nodes and edges must be arrays`); return; }
    const ids=new Set();
    m.nodes.forEach(n=>{
      if(ids.has(n.id)) err(`${where}: node id "${n.id}" is used twice — edges will attach to the wrong one`);
      ids.add(n.id);
      if(!has(PATHS,n.p)) err(`${where}: node "${n.id}" has pathway "${n.p}", which is not in PATHS`);
      if(n.k!==undefined&&n.k!=="hub"&&n.k!=="ghost") err(`${where}: node "${n.id}" has unknown kind "${n.k}"`);
      if(n.go!==undefined&&!has(MAPS,n.go)) err(`${where}: ghost node "${n.id}" links to missing map "${n.go}"`);
      if(typeof n.l!=="string"||!n.l) err(`${where}: node "${n.id}" has no label`);
      else{ const b=nodeBox(n);
        if(b.x<0||b.y<0||b.x+b.w>m.w||b.y+b.h>m.h) err(`${where}: node "${n.id}" sits partly off the canvas (${Math.round(b.x)},${Math.round(b.y)} ${Math.round(b.w)}×${b.h} on ${m.w}×${m.h})`); }
    });
    m.nodes.forEach(n=>{ if(n.hl!==undefined&&!ids.has(n.hl)) err(`${where}: node "${n.id}" highlights missing node "${n.hl}"`); });
    const keys=new Set();
    m.edges.forEach(e=>{
      const k=e.a+">"+e.b;
      if(!ids.has(e.a)) err(`${where}: edge ${k} starts at missing node "${e.a}"`);
      if(!ids.has(e.b)) err(`${where}: edge ${k} ends at missing node "${e.b}"`);
      if(keys.has(k)) err(`${where}: edge ${k} is defined twice — its chip, quiz reveal and audit collide`);
      keys.add(k);
      if(!has(PATHS,e.p)) err(`${where}: edge ${k} has pathway "${e.p}", which is not in PATHS`);
      if(!ARROWS.includes(e.arrow)) err(`${where}: edge ${k} has unknown arrow "${e.arrow}"`);
      if(e.m&&e.m.length&&!e.e&&e.m.length>1) warn(`${where}: edge ${k} has ${e.m.length} pins but no chip label`);
    });
    [...(m.comps||[]),...(m.panels||[])].forEach(c=>{
      if(c.x<0||c.y<0||c.x+c.w>m.w||c.y+c.h>m.h) err(`${where}: box "${(c.l||c.t||"").slice(0,40)}" runs off the ${m.w}×${m.h} canvas`);
    });
    const pin=(arr,owner)=>{ const seen=new Set();
      (arr||[]).forEach(id=>{
        if(!has(LES,id)) err(`${where}: ${owner} pins "${id}", but no such card exists`);
        if(seen.has(id)) err(`${where}: ${owner} pins "${id}" twice`);
        seen.add(id); (pinned[id]=pinned[id]||[]).push(v);
      }); };
    m.nodes.forEach(n=>pin(n.m,`node "${n.id}"`));
    m.edges.forEach(e=>pin(e.m,`edge ${e.a}>${e.b}`));
  });
  Object.keys(LES).forEach(id=>{ if(!pinned[id]) err(`${id}: card is pinned to no map — it only shows in the Index`); });

  /* first home = first map (in MAPS definition order) that pins the card; the
     Index and bare #card links go there */
  const cards=Object.entries(LES).map(([id,L])=>({id,n:L.n,alias:L.alias||"",k:L.k,p:L.p,home:(pinned[id]||[])[0]||null}));
  print(JSON.stringify({errors,warnings,cards}));
})();
