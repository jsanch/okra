$(document).ready(function() {

  // fill in tab name
  var NewTabTemplate = Handlebars.compile($('#new_tab_template').html());
  var context = {
    first_name : $.cookie('first_name'),
    last_name : $.cookie('last_name')
  }
  $('#new_tab_name').html(NewTabTemplate(context));

  // Bind open add friends modal button
  $('#open_add_friends').on('click', function() {
    openAddFriends($.cookie('user_id'), friends_to_add);
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
      $(showPicture).show();
      $('#camera-container').css('background-color', 'white');
    }
  };

  // Uploading the picture on clikcing create tab
  $('#js-create-tab').click(function(){
    $('#uploadform').submit();
  });

  $('#uploadform').submit(function(e) {
    e.preventDefault();
    var tab = {
      title : $.cookie('first_name') + "'s Tab",
      file_url : showPicture.src
    };
    var group = Object.keys(friends_to_add);
    if (!(typeof group !== 'undefined' && group.length > 0)) {
      window.alert('Please add friends to tab.');
      //return;
    }
    $(this).ajaxSubmit({
      success: function(responseText, statusText, xhr, $form) {
        if (responseText === 'fail') {
          window.alert('Tab failed to upload. Blame Vinay.');
        } else {
          console.log(group);
          // Send the other info like group, maste id, etc.
          $.post('/create_invites', {group: group, tab_id : responseText.tab_id})
          .done(function() {
            closeNewTabView(responseText.tab_id, false);
          });
        }
      }
    });
              // closeNewTabView(_tab_id, false);

  });

});
