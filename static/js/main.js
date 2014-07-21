$(document).ready(function() {
  // session variables
  var user_id = 999;
  var theTab = null;

  // start asking server for outstanding invites
  // pollForInvite();

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
  if(cookie.length == 0) return {};
  var cookie_obj = {};
  var fields = cookie.split(';');
  fields.forEach(function(string) {
    var parts = string.split('=');
    cookie_obj[parts[0].trim()] = parts[1].trim();
  });
  return cookie_obj;
}

function getTab(id) {
  return $.get('http://app.grasscat.org/get_tab?tab_id=' + id);
};

function getUser(id) {
  return $.get('http://app.grasscat.org/get_user?user_id=' + id);
};

// ---------------------- Change Views ----------------------

function openTabView() {
  clearInterval(db_poll_interval);
  db_poll_interval = setInterval(function() { updateTabView() }, 100);
  $('#tab_view').fadeIn(200);
  $('#page_title').fadeIn(200);
}
function closeTabView(back) {
  $('#add_friend_button').fadeOut(200);
  $('#tab_view').fadeOut(200, function() {
    if(back) {
      openNewTabView();
    } else {
      openPayView();
    }
  });
}

function openPayView() {
  initPayView();
  $('#pay_view').fadeIn(200);
}
function closePayView() {
  $('#add_friend_button').fadeIn(200);
  $('#pay_view').fadeOut(200, function() {
    openTabView();
  });
}

function openNewTabView() {
  $('#page_title').fadeOut(200);
  $('#new_tab_view').fadeIn(200);
}
function closeNewTabView(back) {
  $('#new_tab_view').fadeOut(200, function() {
    openTabView();
  });
}

function openMainView() {
  $('#main_view').fadeIn(200);
}
function closeMainView() {
  $('#main_view').fadeOut(200, function() {
    openNewTabView();
  });
}



$('#js-start-tab').on('click', function() {
  closeMainView()
});

$('#tab_view #finish_button').on('click', function(event) {
  closeTabView();
});
  
$('#tab_view #back_button').on('click', function(event) {
  //should clear tab

  closeTabView(true);
});

$('#pay_view #back_button').on('click', function(event) {
  closePayView();
});

$('#make_payment_button').on('click', function(){
  window.location.replace("http://app.grasscat.org/venmo_login");
});





