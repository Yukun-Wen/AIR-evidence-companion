
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
function rowHtml(p){
  return '<tr><td><a href="'+paperLink(p)+'"><b>'+esc(p.id)+'</b></a></td>'+
  '<td>'+esc(p.title)+'</td><td>'+esc(p.authors_short)+'</td><td>'+esc(p.year||'')+'</td>'+
  '<td>'+esc(p.venue)+'</td><td>'+esc((p.sections||[]).map(function(s){return s.title}).join('; '))+'</td>'+
  '<td>'+esc(p.workflow||'')+'</td><td>'+badgeHtml(p)+'</td></tr>';
}
