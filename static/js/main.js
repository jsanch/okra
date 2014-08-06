// ---------------------- Global ----------------------

var POLL_DELAY = 2000, // ms
    _current_page = 'MAIN' // start on MAIN page
    _tab = {},
    _tab_id,
    _group = {},
    db_poll_interval,
    friends_to_add = {};

var user_id = $.cookie('user_id');
var user = {
  id: user_id,
  first_name : $.cookie('first_name'),
  last_name : $.cookie('last_name')
}

var invitePoll;

$(document).ready(function() {
  // start asking server for outstanding invites
  invitePoll = pollForInvite();

  // bind accept tab event
  $('#js-accept-tab').on('click', function() {
    acceptInvite();
  });
  // bind reject tab event
  $('#js-reject-tab').on('click', function() {
    rejectInvite();
  });
});

/**
* Continuously poll the server for any tab invitations from this user
*/
function pollForInvite(){
  return setInterval(function() {
    $.get('/poll_for_invite', {user_id:user_id})
    .done(function(data) {
      if (data === 'fail') {
        console.log('no new tabs');
      } else {
        console.log(data);
        showInvite(JSON.parse(data));
      }
    });
  }, POLL_DELAY);
}

/**
* create modal with the tab request
*/
function showInvite(tab) {
  console.log(tab);
  _tab = tab;
  $('#js-invite-modal .modal-title').text('New Tab Invite');
  $('#js-invite-modal .modal-body').text('You have been invited to ' + tab['title']);
  $('#js-invite-modal').modal();
}

/**
* Accept the tab invite and redirect to new tab page
*/
function acceptInvite() {
  // global tab object must be set
  if (!_tab) {
    window.alert('Sorry there is no tab available to accept.');
  }
  // post to server that tab was accepted
  $.post('/accept_invite', {tab_id : _tab['_id']})
    .done(function(data) {
        if (data === 'success') {
          // kill polling
          clearInterval(invitePoll);
          // do mike's switch thing
          $('#modal').modal('toggle');
          closeMainView(_tab['_id']);
        } else {
          window.alert('Could not enter the tab');
        }
    });
}

function rejectInvite() {
  $.post('/reject_invite', {tab_id : _tab['_id']})
    .done(function(data) {
      _tab = {};
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
  _current_page = 'TAB';
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
  _current_page = 'PAY';
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
  _current_page = 'NEW_TAB'
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
  _current_page = 'MAIN'
  $('#main_view').fadeIn(200);
  _tab = {};
}
function closeMainView(tab_id) {
  $('#main_view').fadeOut(200, function() {
    if (tab_id) {
      initTabView(tab_id);
      openTabView();
    } else {
      openNewTabView();
    }
  });
}

$('#js-start-tab').on('click', function() {
  closeMainView();
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





