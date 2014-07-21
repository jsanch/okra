var AddFriendsTemplate;
var FriendRowTemplate;
var FriendBlockTemplate;

$(function() {
  AddFriendsTemplate  = Handlebars.compile($('#add_friends_template').html());
  FriendRowTemplate = Handlebars.compile($('#friend_row_template').html());
});

// get friends and populate the add friends modal
function openAddFriends(user_id, friends_to_add) {
  var friends_list = getFriends(user_id);

  $('#add_friends_body').html(AddFriendsTemplate({friends : friends_list}));
  // toggle friends already added to list
  $('.js-add-friend').each(function() {
    var friend = $('.js-friend', this);
    if (friend.data('id') in friends_to_add) {
      $('.friend_add_icon', this).toggle();
    }
  });
  // bind add friend action to each friend
  $('.js-add-friend').on('click', function() {
    updateFriend($(this), friends_to_add);
  });
  // show modal
  var a = $('#js-add-friends-modal');
  $('#js-add-friends-modal').modal();
}

// returns dictionary of friends with their ids and names
function getFriends(user_id) {
  return {
      // user_id : user_name
      1 : {first_name : 'Mikey Big Wang'},
      2 : {first_name : 'Vinay Fuck This Farias'},
      3 : {first_name : 'Steven Nuggers Han'},
      4 : {first_name : 'Jaime Hipster Sanchez'},
      5 : {first_name : 'Dan The Boss Wu'}
    };
  $.get('http://app.grasscat.org:/get_friends', {user_id : user_id})
  .done(function(data) {
    return data;
  });
}

// add the friend row to the global set or delete it if it's already in there
function updateFriend(friend, friends_to_add) {
  $('.friend_add_icon', friend).toggle();
  var selectedID = $('.js-friend', friend).data('id');
  if (selectedID in friends_to_add) {
    delete friends_to_add[selectedID];
  } else {
    friends_to_add[selectedID] = {first_name: $('.js-friend', friend).html()};
  }
}

// update the UI to show which friends added
function updateAdded() {
  console.log(friendsToAdd);
  // Populate friends list
  $('.friend_block').remove();
  $('.friend_group_row').prepend(FriendRowTemplate({ friends: friendsToAdd }));
}




