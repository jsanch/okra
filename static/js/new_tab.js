$(document).ready(function() {
  // get user_id from cookie
  var user_id = 999,
      user_name = 'Jesus',
      pro_pic = '/static/img/face.jpeg';
  var friendsToAdd = {};

  // get user profile with the id
  $.get('http://app.grasscat.org:5000/ajax/get_user', {user_id : user_id})
  .done(function(data) {
    console.log(data);
  });

  // fill in tab name
  var NewTabTemplate = Handlebars.compile($('#new_tab_template').html());
  $('#new_tab_name').html(NewTabTemplate({user_name : user_name}) + "'s Tab");

  // Bind open add friends modal button
  $('#open_add_friends').on('click', function() {
    openAddFriends(user_id, friendsToAdd);
  });

  // Bind confirm add friends button
  $('#add_friends_button').on('click', function() {
    updateAdded();
  });

  // Bind take photo button
  $('#camera').on('click', function() {
    $('#take-picture').click();
  });

  // Bind getting the picture file
  var takePicture = document.querySelector("#take-picture");
  var showPicture = document.querySelector("#show-picture");

  takePicture.onchange = function (event) {
    // Get a reference to the taken picture or chosen file
    var files = event.target.files,
        file;
    if (files && files.length > 0) {
      file = files[0];
      try {
        // Get window.URL object
        var URL = window.URL || window.webkitURL;
        // Create ObjectURL
        var imgURL = URL.createObjectURL(file);
        // Set img src to ObjectURL
        showPicture.src = imgURL;
        // For performance reasons, revoke used ObjectURLs
        URL.revokeObjectURL(imgURL);
      }
      catch(e) {
        try {
          // Fallback if createObjectURL is not supported
          var fileReader = new FileReader();
          fileReader.onload = function (event) {
              showPicture.src = event.target.result;
          };
          fileReader.readAsDataURL(file);
        }
        catch (e) {
          var error = document.querySelector("#error");
          if (error) {
              error.innerHTML = "Neither createObjectURL or FileReader are supported";
          }
        }
      }
    }
  };

  // send file url to backend to parse
  function createTab() {
    var newTab = {
      master_id : user_id,
      group : {},
      file_url : ''
    };
    $.post('http://app.grasscat.org:5000/ajax/create_tab', {tab: newTab})
    .done(function(data) {
    });
  }

  $('#uploadform').submit(function(e){
    e.preventDefault();

    $(this).ajaxSubmit({
      success: function(responseText, statusText, xhr, $form) {
        if (responseText === 'fail'){
          window.alert('Tab failed to upload. Blame Vinay.');
        } else {
          closeNewTabPage();
        }
      }
    });
  });

  $('#js-create-tab').click(function(){
    $('#uploadform').submit();
    // createTab();
  });

  // // get friends and populate the add friends modal
  // function openAddFriends(user_id) {
  //   var friends_list = getFriends(user_id);
  //   var AddFriendsTemplate = Handlebars.compile($('#add_friends_template').html());
  //   $('#add_friends_body').html(AddFriendsTemplate({friends : friends_list}));
  //   // toggle friends already added to list
  //   $('.js-add-friend').each(function() {
  //     var friend = $('.js-friend', this);
  //     if (friend.data('id') in friendsToAdd) {
  //       $('.glyphicon-ok-circle', this).toggle();
  //     }
  //   });
  //   // bind add friend action to each friend
  //   $('.js-add-friend').on('click', function() {
  //     addFriend($(this));
  //   });
  //   // show modal
  //   $('#js-add-friends-modal').modal();
  // }

  // // returns dictionary of friends with their ids and names
  // function getFriends(user_id) {
  //   return {
  //       // user_id : user_name
  //       1 : {name : 'Mikey Big Wang'},
  //       2 : {name : 'Vinay Fuck This Farias'},
  //       3 : {name : 'Steven Nuggers Han'},
  //       4 : {name : 'Jaime Hipster Sanchez'},
  //       5 : {name : 'Dan The Boss Wu'}
  //     };
  //   $.get('http://app.grasscat.org:5000/ajax/get_friends', {user_id : user_id})
  //   .done(function(data) {
  //     return data;
  //   });
  // }

  // // add the friend row to the global set or delete it if it's already in there
  // function addFriend(friend) {
  //   $('.glyphicon-ok-circle', friend).toggle();
  //   var selectedID = $('.js-friend', friend).data('id');
  //   if (selectedID in friendsToAdd) {
  //     delete friendsToAdd[selectedID];
  //   } else {
  //     friendsToAdd[selectedID] = {name: $('.js-friend', friend).html()};
  //   }
  // }

  // // update the UI to show which friends added
  // function updateAdded() {
  //   var FriendBlockTemplate = Handlebars.compile($('#friend_block_template').html());
  //   // Populate friends list
  //   $('.friend_group_row .friend_block').remove();
  //   console.log(friendsToAdd);
  //   $('.friend_group_row').prepend(FriendBlockTemplate({ friends: friendsToAdd }));
  // }

});