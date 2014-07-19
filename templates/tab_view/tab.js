
$(function() {
  var NAME_CHAR_LIMIT = 8;

  var user_id = 1;

  // ---------------------- Templates ----------------------

  var FriendRowTemplate = Handlebars.compile($('#friend_row_template').html());
  var FriendBlockTemplate = Handlebars.compile($('#friend_block_template').html());
  var ItemListTemplate = Handlebars.compile($('#item_list_template').html());
  var ItemTemplate = Handlebars.compile($('#item_template').html());

  Handlebars.registerPartial("item_template", $("#item_template").html());

  Handlebars.registerHelper('get_name', function(id) {
    var user = friends[id];
    return user? user.first_name + ' ' + user.last_name : 'None';
  });

  Handlebars.registerHelper('get_pic_url', function(id) {
    return 'face.jpeg';
  });

  Handlebars.registerHelper('user_selected', function(assigned_to) {
    return $.inArray(user_id, assigned_to) != -1;
  });

  // ---------------------- Global ----------------------

  var _tab;
  var _friends;

  // ---------------------- Init ----------------------

  // Initially populate page
  populatePage();
  // Update page periodically
  setInterval(function() { updatePage() }, 100);

  // ---------------------- Functions ----------------------

  function getTab() {
    return $.get("http://app.grasscat.org/get_tab?tab_id=12");
  };

  function getUser() {
    return $.get("http://app.grasscat.org/get_user?user_id=12");
  };

  function populatePage() {
    getTab().done(function(data) {
      if(!data) return;

      var data = JSON.parse(data);

      friends = {
        1: {first_name: 'Barack', last_name: 'Obama'},
        2: {first_name: 'Curioussssss', last_name: 'George'},
        3: {first_name: 'Michael', last_name: 'Vader'},
        4: {first_name: 'Darth', last_name: 'Vader'},
        5: {first_name: 'Darth', last_name: 'Vader'},
        6: {first_name: 'Darth', last_name: 'Vader'},
        7: {first_name: 'Darth', last_name: 'Vader'},
      };

      _tab = {
        id: 100,
        title: "Dinner at Centerfolds",
        group: [1, 2, 3, 4, 5, 6, 7],
        currency: '$',
        items: {
          1: {name: 'Okra babadydoopityboopitydoo yeeeeeeeeee', price: '14.50', assigned_to: [1]},
          2: {name: 'Okra', price: '14.50', assigned_to: []},
          3: {name: 'Okra', price: '14.50', assigned_to: [1, 2]},
          4: {name: 'Okra', price: '14.50', assigned_to: [2]},
          5: {name: 'Okra', price: '14.50', assigned_to: [2]}
        },
        tax: 14.44,
        tip: 50.00,
        total: 3234,
        subtotal: 123,
      }

      // Populate friends list
      $('.friend_group_row').prepend(FriendRowTemplate({ friends: friends }));
      // Populate item list
      $('.item_list').html(ItemListTemplate({ items: _tab.items }));

      $('#title').text(_tab.title);
      $('#tax').text(_tab.tax);
      $('#tip_input').val(_tab.tip);
      $('#subtotal').text(_tab.subtotal);
      $('#total').text(_tab.total);
    });
  }

  function updatePage() {
    if(!_tab) return;
    getTab().done(function(data) {
      var new_tab = JSON.parse(data);

      new_tab = {
        id: 100,
        title: "Dinner at Centerfolds",
        group: [1, 2, 3, 4, 5, 6, 7],
        currency: '$',
        items: {
          1: {name: 'Okra babadydoopityboopitydoo yeeeeeeeeee', price: '14.50', assigned_to: [1]},
          2: {name: 'Okra', price: '14.50', assigned_to: [1]},
          3: {name: 'Okra', price: '14.50', assigned_to: [4]},
          4: {name: 'Okra', price: '14.50', assigned_to: [3, 2]},
          5: {name: 'Okra', price: '14.50', assigned_to: [4]}
        },
        tax: 14.44,
        tip: 5012.00,
        subtotal: 1000,
        total: 3234,
      }

      // Update friends if it has changed
      new_tab.group.forEach(function(id) {
        if($.inArray(id, _tab.group) == -1) {
          getUser().done(function(data) {
            var friend = JSON.parse(data);
            $('.friend_group_row').prepend(FriendBlockTemplate(friend));
          });
        }
      });
      _tab.group.forEach(function(id) {
        if($.inArray(id, new_tab.group) == -1) {
          $('.friend_group_row .friend_block[data-id=' + id + ']').remove();
        }
      });

      // Update list items if it has changed
      for(var item_id in _tab.items) {
        var a = _tab.items[item_id].assigned_to;
        var b = new_tab.items[item_id].assigned_to;
        if(!_tab.items[item_id].assigned_to.is_same(new_tab.items[item_id].assigned_to)) {

          $('.item_list .tab_item[data-id=' + item_id + ']').replaceWith(ItemTemplate(new_tab.items[item_id]));
        }
      }

      // Update the global tab object
      _tab = new_tab;
    });
  }

  function update_tip(tip_val) {
    $('#tip_input').val(tip_val.toFixed(2));
    var total_val = (parseFloat(_tab.subtotal) + parseFloat(_tab.tax) + tip_val).toFixed(2);
    $('#total').text(total_val);
    _tab.total = total_val;
  }

  // ---------------------- Event Bindings ----------------------

  //Add a user to the group
  $('#add_friend_button').on('click', function() {
    var friends = get_friends(user_id);
    // dont prepend
    $('.friend_group_row').prepend(FriendBlockTemplate({ friends: friends }));
  });

  // Submit an item select
  $('.item_list li').on('click', function(event) {
    var item_id = $(this).data('id');
    var item_assigned_to_id = $(this).data('assigned_to_id');

    if(user_id == item_assigned_to_id) {
      $.post("select_item_url", { user_id: 10, tab_id: _tab.id, item_id: item_id });
    } else {
      $.post("remove_item_url", { user_id: 10, tab_id: _tab.id, item_id: item_id });
    }
  });

  $('.tip_button').on('click', function() {
    update_tip(parseFloat($(this).data('percentage')) * parseFloat(_tab.subtotal));
  });

  $('#tip_input').keydown(function(event) {
    if(event.which == 13) {
      event.preventDefault();
      update_tip(parseFloat($('#tip_input').val()));
    }
  });

  $('#finish_button').on('click', function(event) {
    window.location.replace("http://stackoverflow.com");
  });

});

// ---------------------- Prototype ----------------------

Array.prototype.is_same = function(other) {
  if (this.length != other.length) return false;
  for (var i = 0; i < other.length; i++) {
    if (this[i].compare) { 
      if (!this[i].compare(other[i])) return false;
    }
    if (this[i] !== other[i]) return false;
  }
  return true;
} 





