
// Affichage des messages
function display_messages() {
  messages.textContent = '';

  // On envoie une requête Ajax pour récupérer la liste des messages
  ajax_request('GET','/commentaires/' + site_name, function() {

    // récupération des données renvoyées par le serveur
    let data = JSON.parse(this.responseText);

    // boucle sur les messages
    data.forEach(display_message);
  });
}


// Affichage d'un message
function display_message(msg) {
  // pseudo, timestamp, message, date sont les attributs des messages

  // mise en forme du timestamp

//let d = new Date(SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSSSSS").parse(msg.timestamp))
  let d = new Date(msg.timestamp)
    , date_options = {
        day:'2-digit',
        month: '2-digit',
        year: "2-digit",
        hour:'2-digit',
        minute:'2-digit'
      }
    ,s = d.toLocaleString('fr-FR',date_options)
  ;

  // préparation des parties du message
  let html = '<header>' + s + ' <b>[&thinsp;'+msg.pseudo+'&thinsp;]</b> ';
  if ( msg.date ) html += 'a visité ce site pendant '+msg.date;
  html += '<span class="delete" title="Supprimer ce message">x</span>';
  html += '</header>';
  html += '<p>'+msg.message+'</p>';

  // affichage du message
  let article = document.createElement('article');
  article.innerHTML = html;
  article.dataset.id = msg.id;
  messages.appendChild(article);

  // touche de suppression du message
  let span = article.querySelector('.delete')
  span.addEventListener('click', function() {

    // Affichage du popup de demande de mot de passe
    enter_pwd.value = '';
    pwd_request.style.marginTop = window.scrollY + 'px';
    pwd_request.style.display='block';
    pwd_request.style.visibility='visible';

    // Poursuite de l'opération après entrée du mot de passe
    confirm_pwd.addEventListener('click', function() {

      // On cache le popup
      pwd_request.style.display='none';

      // demande de suppression du message
      ajax_request('DELETE','/commentaire/' + msg.id,
        JSON.stringify({
        pseudo: msg.pseudo,
        password: enter_pwd.value,
        }),
        { 'Content-Type': 'application/json' },
        function() {
		  
          // suppression du message
          if ( this.status == 204 ) {
            article.parentNode.removeChild(article);
            show_comments.style.visibility = n ? 'visible' : 'hidden';
          }

          // il y a eu un problème côté serveur
          else {
            alert(this.status+' '+this.statusText);
            console.log(this.status,this.statusText);
          }
		  display_messages();
      });
    },{once: true});
  });
}


// Création d'un message
function post_message() {
  let body = { site: site_name }
    , headers = { 'Content-Type': 'application/json' }
  ;
  [ 'pseudo', 'password', 'message', 'date'].forEach(k => {
        body[k] = window['input_'+k].value;
  });
  ajax_request('POST','/commentaire', JSON.stringify(body), headers, function() {
    if ( this.status == 200 ) {
      let msg = JSON.parse(this.responseText);
      message_editor.style.display='none';
      display_message(msg);
      show_comments.style.visibility = 'visible';
    }
    else {
      let errmsg = (this.statusText == "Missing 'email'") ? 'Unknown user' : this.statusText
        , status = (this.statusText == "Missing 'email'") ? 401 : this.status
      ;
      alert(status+' '+errmsg);
      console.log(status,errmsg);
    }
	display_messages();
  });
}

// Création d'un nouvel utilisateur
function post_user(){
  let headers = { 'Content-Type': 'application/json' };
  body={};
  [ 'user_pseudo', 'email', 'user_password'].forEach(k => {
        body[k] = window['input_'+k].value;
  });
  ajax_request('POST','/utilisateur', JSON.stringify(body), headers, function() {
    if ( this.status == 200 ) {
      let user = JSON.parse(this.responseText);
      user_editor.style.display='none';
    }
    else {
      let errmsg = (this.statusText == "Missing 'email'") ? 'Unknown user' : this.statusText
        , status = (this.statusText == "Ce pseudo existe déja") ? 409 : this.status
      ;
      alert(status+' '+errmsg);
      console.log(status,errmsg);
    }
 
  });
}