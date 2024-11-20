/*
** Initialisation d'un popup
*/
function init_popup(container, header, show_btn, hide_btn) {
  // les popups sont draggables
  header && draggable(container, header);

  // gestionnaire pour montrer le popup
  show_btn && show_btn.addEventListener('click', popup.bind(show_btn,container));

  // gestionnaire pour cacher le popup
  hide_btn && hide_btn.addEventListener('click', hide.bind(hide_btn,container));
}


/*
** Afichage d'un popup
*/
function popup(elt) {
  let fields = elt.querySelectorAll('input, textarea');
  fields.forEach(f => f.value = '');
  elt.style.marginTop = window.scrollY + 'px';
  elt.style.display='block';
  elt.style.visibility='visible';
}


/*
** Désaffichage d'un popup
*/
function hide(elt) {
  elt.style.display='none';
}


/*
** Envoi d'une requête Ajax
*/
function ajax_request(method,url,body,headers,cb) {
  if ( arguments.length == 3 ) { cb = body, body = '', headers = {} };
  if ( arguments.length == 4 ) { cb = headers, headers = {} };
  var xhr = new XMLHttpRequest();
  xhr.onload = cb;
  xhr.open(method,url,true);
  for ( h in headers ) {
    xhr.setRequestHeader(h, headers[h]);
  }
  xhr.send(body);
}


/*
** Retire les éventuelles balises html d'un texte
*/
function sanitize_html(html) {
  let fake_div = document.createElement('div');
  fake_div.innerHTML = html;
  return fake_div.textContent;
}


/*
** Rend un élément draggable
*/
function draggable(element,handle) {
    var handle = handle || element
      , startX = 0 , startY = 0 , x = 0 , y = 0
      , startLeft, startTop, startWidth, startHeight
    ;

    //handle.css({ cursor: 'pointer' });

    handle.addEventListener('mousedown', function(event) {
      var style = window.getComputedStyle(element);

      if ( style.position == 'static' ) element.style.position = 'absolute';
      if ( ! style.zIndex ) element.style.zIndex = 500;

      // Prevent default dragging of selected content
      event.preventDefault();

      // let position be relative to initial one
      startLeft = parseFloat(style.left);
      startTop = parseFloat(style.top);

      // let dragging be relative to mousedown position
      startX = event.pageX;
      startY = event.pageY;
      document.addEventListener('mousemove', mousemove);
      document.addEventListener('mouseup', mouseup);

      // eventually call hook
      if ( element.mousedown_hook ) {
        element.mousedown_hook(startX, startY, startLeft, startTop, startWidth, startHeight);
      }
    });

    function mousemove(event) {
      if ( event.clientX > 0 && (!window.innerWidth || event.clientX < window.innerWidth)) {
        x = event.pageX - startX;
      }
      if ( event.clientY > 0 && (!window.innerHeight || event.clientY < window.innerHeight)) {
        y = event.pageY - startY;
      }
      element.style.top = (startTop + y) + 'px';
      element.style.left = (startLeft + x) + 'px';

      //eventually move handles
      if ( element.handles ) element.handles.forEach(function(h){ h.move(); });

      // eventually call hook
      if ( element.mousemove_hook ) element.mousemove_hook();
    }

    function mouseup() {
      document.removeEventListener('mousemove', mousemove);
      document.removeEventListener('mouseup', mouseup);

      // eventually call hook
      if ( element.mouseup_hook ) element.mouseup_hook();
    }
}


/*
** Permet le redimensionnement d'un container (a priori
** du type popup) via un textarea qu'il contient
*/
function resize_with_textarea(container, textarea) {
  let rect = textarea.getBoundingClientRect()
    , s = getComputedStyle(container)
    , textarea_startWidth = rect.width
    , textarea_startHeight = rect.height
    , container_startWidth = parseFloat(s.width)
    , container_startHeight = parseFloat(s.height)
  ;
  new ResizeObserver(function(entries){
    let rect = textarea.getBoundingClientRect();
    for ( let entry of entries ) {
      container.style.width = container_startWidth + (rect.width - textarea_startWidth) + 'px';
      container.style.height = container_startHeight + (rect.height - textarea_startHeight) + 'px';
    }
  }).observe(textarea);

  textarea.style.width = textarea_startWidth + 'px';
  textarea.style.height = textarea_startHeight + 'px';
};


/*
** Initialisation automatique de tous les popups
*/
window.addEventListener('load',e => {
  [...document.querySelectorAll('.popup')].forEach(p => {
    let handle = document.querySelector('#'+p.id+' .handle')
      , show_btn = document.querySelector('.show_popup[data-popup='+p.id+']')
      , hide_btn = document.querySelector('#'+p.id+' .hide_popup, .hide_popup[data-popup='+p.id+']')
    ; 
    init_popup(p, handle, show_btn, hide_btn);
  });

  [...document.querySelectorAll('.resizable')].forEach(p => {
    let textarea = document.querySelector('#'+p.id+' textarea');
    if ( textarea ) resize_with_textarea(p,textarea);
  });
});
