$(document).ready(function() {
  var theTab = null;

  // pollForInvite();

  // bind create tab event
  $('#js-start-tab').on('click', function() {
    console.log('dsds');
  });

  // bind accept tab event
  $('#js-accept-tab').on('click', function() {
    acceptInvite()
  });
});

/**
* Continuously poll the server for any tab invitations from this user
*/
function pollForInvite(){
    $.get('http://app.grasscat.org:5000/ajax/pollforinvite', {user_id : 999})
    .done(function(data) {
      // check for tab invite
      if (data['tab']) {
        showInvite(data);
      } else { console.log('no new tabs'); }
    })
    .always(function() {
      setTimeout(pollForInvite,5000);
    });
}

/**
* create modal with the tab request
*/
function showInvite(tab) {
  console.log(tab);
  theTab = tab['tab'];
  $('.modal-body').text(theTab['user_id'] + ' has invited you to ' + theTab['tab_name']);
  $('#js-invite-modal').modal();
}

/**
* Accept the tab invite and redirect to new tab page
*/
function acceptInvite() {
  // global tab object must be set
  if (!theTab) {
    window.alert('Sorry there is no tab available to accept.');
  }
  var acceptedTab = {
    user_id : 999,
    tab_id : theTab['tab_id']
  }
  // post to server that tab was accepted
  $.post('http://app.grasscat.org:5000/ajax/accepttab', acceptedTab)
    .done(function(data) {
        if (data.redirect) {
          // data.redirect contains the string URL to redirect to the accepted tab page
          window.location.href = data.redirect;
        } else {
          // data.form contains the HTML for the replacement form
          $("#myform").replaceWith(data.form);
        }
    });
}
