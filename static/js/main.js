// ---------------------- Global ----------------------

var friendsToAdd = {},
    POLL_DELAY = 5000, // ms
    _tab = {},
    _group = {},
    db_poll_interval;

var user_id = $.cookie('user_id');

var _tab_id = '53cca6cdd2a57d3208d1bd8c';

var user = {
  id: user_id,
  first_name : $.cookie('first_name'),
  last_name : $.cookie('last_name')
}

$(document).ready(function() {
  // start asking server for outstanding invites
  pollForInvite();

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
    $.get('/poll_for_invite', {user_id:user_id})
    .done(function(data) {
      if (data) {
        showInvite(JSON.parse(data));
      } else {
        console.log('no new tabs');
      }
    });
  }, POLL_DELAY);
}

/**
* create modal with the tab request
*/
function showInvite(tab) {

  // {
  //   "paid_users": [],
  //   "_id": "53ccd703d2a57d6ec8ebded6",
  //   "group": [],
  //   "title": "Michael's tab",
  //   "tip": 0.0,
  //   "tax": 0.63,
  //   "paid": false,
  //   "master_user_id": "53ccbe9d04b7747717fcdfdf",
  //   "items": {"0": {"price": 8.99,
  //   "name": "1 summer big bowl",
  //   "assigned_to": ["53ccbe9d04b7747717fcdfdf"]}},
  //   "total": 9.62,
  //   "subtotal": 8.99
  // }
  $('.modal-body').text('You have been invited to ' + tab['title']);
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

function getTab(id) {
  return $.get('http://app.grasscat.org/get_tab?tab_id=' + id);
};

function getUser(id) {
  return $.get('http://app.grasscat.org/get_user?user_id=' + id);
};

// ---------------------- Change Views ----------------------

function openTabView() {
  clearInterval(db_poll_interval);
  db_poll_interval = setInterval(function() { updateTabView() }, POLL_DELAY);
  $('#tab_view').fadeIn(200);
  $('#page_title_view').fadeIn(200);
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
  $('#page_title_view').fadeOut(200);
  $('#new_tab_view').fadeIn(200);
}
function closeNewTabView(tab_id, back) {
  $('#new_tab_view').fadeOut(200, function() {
    if(back) {
      openMainView();
    } else {
      initTabView(tab_id);
      openTabView();
    }
  });
}

function openMainView() {
  $('#main_view').fadeIn(200);
  _tab = {};
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

$('#new_tab_view #back_button').on('click', function(event) {
  closeNewTabView(null, true);
});





