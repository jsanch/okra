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

  var cookie = parseCookie(document.cookie);
});

/**
* Continuously poll the server for any tab invitations from this user
*/
function pollForInvite(){
  setInterval(function() {
    $.get('/poll_for_invite', {user_id:user_id})
    .done(function(data) {
      // check for tab invite
      if (data['tab']) {
        showInvite(data);
      } else {
        console.log('no new tabs');
      }
    });
  }, 500);
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
  $.post('/accept', acceptedTab)
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

// Parse the cookie and return a cookie object
function parseCookie(cookie) {
  var cookie_obj = {};
  var fields = cookie.split(';');
  fields.forEach(function(string) {
    var parts = string.split('=');
    cookie_obj[parts[0].trim()] = parts[1].trim()
  });
  return cookie_obj;
}
