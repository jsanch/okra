var AddFriendsTemplate;
var FriendRowTemplate;
var FriendBlockTemplate;

$(function() {
  AddFriendsTemplate  = Handlebars.compile($('#add_friends_template').html());
  FriendRowTemplate = Handlebars.compile($('#friend_row_template').html());
});

// get friends and populate the add friends modal
function openAddFriends(user_id, friends_to_add) {
  var friends_list;
  $.get('/get_friends', {user_id : user_id})
    .done(function(data) {
      var data = JSON.parse(data);
      var friends_list = {};
      $.each(data, function(id, friend) {
        friends_list[id] = {name : friend['name'], pic_url : friend['pic_url']};
      });
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
      $('#js-add-friends-modal').modal();
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




