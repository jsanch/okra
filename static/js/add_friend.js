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
  // user_id = '53ccbe9d04b7747717fcdfdf'; //change
  $.get('http://app.grasscat.org/get_friends', {user_id : user_id})
    .done(function(data) {
      var data = JSON.parse(data);
      var friends_list = {};
      $.each(data, function(id, friend) {
        if(friend) {
          friends_list[id] = {name : friend['name'], pic_url : friend['pic_url']};
        }
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
      $('.js-add-friend').on('click', function(event) {
        event.preventDefault();
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
    var bg = $('.small_portrait', friend).css('background-image');
    bg = bg.replace('url(','').replace(')','');
    friends_to_add[selectedID] = {first_name: $('.js-friend', friend).html().split(' ')[0], pic_url: bg};
  }
}

// update the UI to show which friends added
function updateAdded() {
  // Populate friends list
  $('.friend_block').remove();
  $('.friend_group_row').prepend(FriendRowTemplate({ friends: friends_to_add }));

  $.post("http://app.grasscat.org/add_friends_to_tab", { tab_id: _tab_id, friends_to_add: friends_to_add });
}




