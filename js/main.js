$(document).ready(function() {
  // session variables
  var user_id = 999;
  var theTab = null;

  // start asking server for outstanding invites
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
  setInterval(function() {
    $.get('http://app.grasscat.org:5000/ajax/poll_for_invite', {user_id:user_id})
    .done(function(data) {
      // check for tab invite
      if (data['tab']) {
        showInvite(data);
      } else {
        console.log('no new tabs');
      }
    });
  }, 5000);
}

/**
* create modal with the tab request
*/
function showInvite(tab) {
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
