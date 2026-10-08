
function esc(s){return String(s==null?'':s).replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
function badgeHtml(p){
  var b=[];
  b.push('<span class="badge '+(p.role=='core'?'core':'ctx')+'">'+(p.role=='core'?'Core report':'Contextual')+'</span>');
  (p.contrast_ids||[]).forEach(function(c){b.push('<span class="badge contrast">'+c+'</span>')});
  var st=p.pdf?p.pdf.status:'';
  if(st=='local_copy'||st=='downloaded_oa'||st=='exists') b.push('<span class="badge">PDF</span>'); else b.push('<span class="badge pending">no PDF</span>');
  return b.join(' ');
}
function paperLink(p){var r=(document.body.dataset.root||'');return r+'papers/'+p.primary.folder+'/'+p.id+'/card.html'}
function renderInteractive(targetId){
  var el=document.getElementById(targetId); if(!el||!window.PAPERS)return;
  var P=window.PAPERS, wfs=[], cols={};
  P.forEach(function(p){var g=p.workflow||'Contextual'; if(wfs.indexOf(g)<0)wfs.push(g)});
  var PAL=['#5b7d95','#7a8b6f','#c08a5f','#8b7fa3','#7fa8a0','#a8604e','#c9a86b','#8fa3b8','#aeb9b3'];
  wfs.forEach(function(g,i){cols[g]=PAL[i%PAL.length]});
  var secs={}; P.forEach(function(p){var sf=p.primary?p.primary.folder:'';
    if(!secs[sf])secs[sf]={title:p.primary?p.primary.title:sf,total:0,groups:{}};
    var g=p.workflow||'Contextual';secs[sf].groups[g]=(secs[sf].groups[g]||0)+1;secs[sf].total++;});
  var rows=Object.keys(secs).map(function(k){return {folder:k,title:secs[k].title,total:secs[k].total,groups:secs[k].groups}});
  rows.sort(function(a,b){return b.total-a.total});
  var W=880,H=rows.length*32+36,L=200,BW=W-L-30;
  var maxT=Math.max.apply(null,rows.map(function(r){return r.total}))||1;
  var s='<svg width="100%" viewBox="0 0 '+W+' '+H+'" font-family="sans-serif">';
  s+='<text x="'+L+'" y="16" font-size="11" fill="#75808a">hover a segment for count - click to open filtered catalog</text>';
  rows.forEach(function(r,i){var y=26+i*32,x=L;
    s+='<text x="'+(L-8)+'" y="'+(y+16)+'" font-size="10" fill="#3a4340" text-anchor="end">'+r.folder.split('_')[0]+' '+esc(r.title.slice(0,26))+'</text>';
    wfs.forEach(function(g){var v=r.groups[g]||0;if(!v)return;var w=v/maxT*BW;
      s+='<rect class="seg" data-sec="'+esc(r.title)+'" data-wf="'+esc(g)+'" x="'+x+'" y="'+y+'" width="'+w+'" height="24" fill="'+cols[g]+'" rx="1.5"><title>'+esc(r.title)+' - '+esc(g)+': '+v+'</title></rect>';x+=w;});
    s+='<text x="'+(x+5)+'" y="'+(y+16)+'" font-size="10" fill="#2e3735">'+r.total+'</text>';});
  var lx=L,ly=H-10;
  wfs.forEach(function(g){var any=rows.some(function(r){return r.groups[g]});if(!any)return;
    s+='<rect x="'+lx+'" y="'+(ly-9)+'" width="10" height="10" fill="'+cols[g]+'" rx="2"/><text x="'+(lx+13)+'" y="'+ly+'" font-size="9" fill="#5a6b6b">'+esc(g)+'</text>';
    lx+=g.length*6.3+56;});
  s+='</svg>'; el.innerHTML=s;
  el.querySelectorAll('.seg').forEach(function(sg){
    sg.style.cursor='pointer';
    sg.onmouseenter=function(){sg.setAttribute('opacity','0.82')};
    sg.onmouseleave=function(){sg.setAttribute('opacity','1')};
    sg.onclick=function(){location.href='catalog.html?sec='+encodeURIComponent(sg.dataset.sec)+'&wf='+encodeURIComponent(sg.dataset.wf)};
  });}

var SORT={key:null,asc:true};
function sortBy(k){SORT.key=k;SORT.asc=!SORT.asc;if(typeof render==='function')render()}
function bibtex(p){var nl=String.fromCharCode(10);var key=p.id+"_"+p.year;var authors=(p.authors_full||p.authors_short||"").split(",").map(function(a){return a.trim()}).join(" and ");  return "@article{"+key+","+nl+"  author={"+authors+"},"+nl+"  title={"+p.title+"},"+nl+"  journal={"+p.venue+"},"+nl+"  year={"+p.year+"}"+(p.doi?","+nl+"  doi={"+p.doi+"}":"")+nl+"}";}function copyBib(id,e){var p=(window.PAPERS||[]).find(function(x){return x.id==id});if(!p)return;var t=bibtex(p);if(navigator.clipboard)navigator.clipboard.writeText(t);e.textContent="copied";setTimeout(function(){e.textContent="BibTeX"},1200)}function rowHtml(p){
  return '<tr><td><a href="'+paperLink(p)+'"><b>'+esc(p.id)+'</b></a></td>'+
  '<td>'+esc(p.title)+'</td><td>'+esc(p.authors_short)+'</td><td>'+esc(p.year||'')+'</td>'+
  '<td>'+esc(p.venue)+'</td><td>'+esc((p.sections||[]).map(function(s){return s.title}).join('; '))+'</td>'+
  '<td>'+esc(p.workflow||'')+'</td><td>'+badgeHtml(p)+'</td><td><button class="bib" data-id="'+p.id+'" onclick="copyBib(this.dataset.id,this)">BibTeX</button></td></tr>';
}
