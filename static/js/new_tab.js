$(document).ready(function() {

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
      $(showPicture).show();
      $('#camera-container').css('background-color', 'white');
    }
  };

  // send file url to backend to parse
  function createTab() {
    var newTab = {
      master_id : user_id,
      group : {},
      file_url : ''
    };
    $.post('http://app.grasscat.org/create_tab', {tab: newTab})
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

});