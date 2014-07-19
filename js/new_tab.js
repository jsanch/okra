$(document).ready(function() {
  var user_id = 999;
  // set to hold friends to add to tab
  var friendsToAdd = {};

  // Bind open add friends modal button
  $('#open_add_friends').on('click', function() {
    openAddFriends(user_id);
  });

  // Bind confirm add friends button
  $('#add_friends_button').on('click', function() {
    updateAdded();
  });

  // get friends and populate the add friends modal
  function openAddFriends(user_id) {
    var friends_list = getFriends(user_id);
    var AddFriendsTemplate = Handlebars.compile($('#add_friends_template').html());
    $('#add_friends_body').html(AddFriendsTemplate({friends : friends_list}));
    // toggle friends already added to list
    $('.js-add-friend').each(function() {
      var friend = $('.js-friend', this);
      if (friend.data('id') in friendsToAdd) {
        $('.glyphicon-ok-circle', this).toggle();
      }
    });
    // bind add friend action to each friend
    $('.js-add-friend').on('click', function() {
      addFriend($(this));
    });
    // show modal
    $('#js-add-friends-modal').modal();
  }

  // returns dictionary of friends with their ids and names
  function getFriends(user_id) {
    return {
        // user_id : user_name
        1 : {name : 'Mikey Big Wang'},
        2 : {name : 'Vinay Fuck This Farias'},
        3 : {name : 'Steven Nuggers Han'},
        4 : {name : 'Jaime Hipster Sanchez'},
        5 : {name : 'Dan The Boss Wu'}
      };
    $.get('http://app.grasscat.org:5000/ajax/get_friends', {user_id : user_id})
    .done(function(data) {
      return data;
    });
  }

  // add the friend row to the global set or delete it if it's already in there
  function addFriend(friend) {
    $('.glyphicon-ok-circle', friend).toggle();
    var selectedID = $('.js-friend', friend).data('id');
    if (selectedID in friendsToAdd) {
      delete friendsToAdd[selectedID];
    } else {
      friendsToAdd[selectedID] = {name: $('.js-friend', friend).html()};
    }
  }

  // update the UI to show which friends added
  function updateAdded() {
    var FriendBlockTemplate = Handlebars.compile($('#friend_block_template').html());
    // Populate friends list
    $('.friend_group_row .friend_block').remove();
    console.log(friendsToAdd);
    $('.friend_group_row').prepend(FriendBlockTemplate({ friends: friendsToAdd }));
  }
});