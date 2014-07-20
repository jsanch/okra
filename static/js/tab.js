// ---------------------- Global ----------------------

var _tab;
var _friends;
var _group;

var db_poll_interval;

var user_id = 1;  // get from session
var _tab_id = '53cc34f9d2a57d636d082146';

$(function() {

  // ---------------------- Templating ----------------------

  var FriendRowTemplate = Handlebars.compile($('#friend_row_template').html());
  var FriendBlockTemplate = Handlebars.compile($('#friend_block_template').html());
  var ItemListTemplate = Handlebars.compile($('#item_list_template').html());
  var ItemTemplate = Handlebars.compile($('#item_template').html());
  var PaidUserListTemplate = Handlebars.compile($('#paid_user_list_template').html());

  Handlebars.registerPartial("item_template", $("#item_template").html());
  Handlebars.registerPartial("paid_user_entry_template", $("#paid_user_entry_template").html());

  Handlebars.registerHelper('get_name', function(user_id) {
    var user = friends[user_id];
    return user? user.first_name + ' ' + user.last_name : 'None';
  });

  Handlebars.registerHelper('get_pic_url', function(user_id) {
    return '../static/img/face.jpeg';
  });

  Handlebars.registerHelper('user_selected', function(assigned_to) {
    return $.inArray(user_id, assigned_to) != -1;
  });

  Handlebars.registerHelper('check_paid', function(user_id, paid_users) {
    return $.inArray(user_id, paid_users) != -1;
  });

  // ---------------------- Init ----------------------

  initTabView();

  function initTabView() {
    // Initially populate page
    populatePage();
    // Update page periodically
    db_poll_interval = setInterval(function() { updateTabView() }, 1000);
  }

  // Initialize the pay view
  function initPayView() {
   // Initialize payment progress knob
    var payment_progress = $('#payment_progress_chart');
    payment_progress.knob(
      {
        'fgColor': 'white',
        'inputColor': 'white',
        'bgColor': 'transparent',
        'readOnly': true,
      }
    );

    // getTab(_tab_id).done(function(data) {
    //   if(!data) return;
    //   _tab = JSON.parse(data);

      var _tab = {
        id: 100,
        title: "Dinner at Centerfolds",
        group: [1, 2, 3, 4, 5, 6, 7],
        paid_users: [],
        currency: '$',
        items: {
          1: {name: 'Okra babadydoopityboopitydoo yeeeeeeeeee', price: '14.50', assigned_to: [1]},
          2: {name: 'Okra', price: '32.45', assigned_to: [1]},
          3: {name: 'Okra', price: '14.50', assigned_to: [4]},
          4: {name: 'Okra', price: '14.50', assigned_to: [3, 2]},
          5: {name: 'Okra', price: '14.50', assigned_to: [4]}
        },
        tax: 14.40,
        tip: 5012.00,
        subtotal: 96.10,
        total: 110.50,
        paid: 72
      }; // TEMP -- REMOVE THIS LATER

      setGroupUsers(_tab.group);

      // Populate list showing which users have paid
      $('.paid_user_list').html(PaidUserListTemplate({ users: _group, paid_users: _tab.paid_users }));
    // });

    // Call pay view update function periodically
    clearInterval(db_poll_interval);
    db_poll_interval = setInterval(function() { updatePayView() }, 100);
  }

  // ---------------------- Functions ----------------------

  function getTab(id) {
    return $.get('http://app.grasscat.org/get_tab?tab_id=' + id);
  };

  function getUser(id) {
    return $.get('http://app.grasscat.org/get_user?user_id=' + id);
  };

  // Get the group users from the list of ids
  function setGroupUsers(group) {
    _group = {};
    // group.forEach(function(id) {
    //   getUser(id).done(function(data) {
    //     if(!data) return;
    //     var user = JSON.parse(data);
    //     _group[user.id] = user;
    //   });
    // });

    _group = {
      1: {first_name: 'Barack', last_name: 'Obama'},
      2: {first_name: 'Curioussssss omgomgomgomgomgomgomgogm', last_name: 'George'},
      3: {first_name: 'Michael', last_name: 'Vader'},
      4: {first_name: 'Darth', last_name: 'Vader'},
      5: {first_name: 'Darth', last_name: 'Vader'},
      6: {first_name: 'Darth', last_name: 'Vader'},
      7: {first_name: 'Darth', last_name: 'Vader'},
    };
  }

  function populatePage() {
    getTab(_tab_id).done(function(data) {
      if(!data) return;

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

      setGroupUsers(_tab.group);
    });
  }

  function updateTabView() {
    if(!_tab) return;
    getTab(_tab_id).done(function(data) {

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
      setGroupUsers(_tab.group);
    });
  }

  function updatePayView() {
    // if(!_tab) return;
    // getTab(_tab_id).done(function(data) {
      // var new_tab = JSON.parse(data);
      var _tab = {
        id: 100,
        title: "Dinner at Centerfolds",
        group: [1, 2, 3, 4, 5, 6, 7],
        paid_users: [],
        currency: '$',
        items: {
          1: {name: 'Okra babadydoopityboopitydoo yeeeeeeeeee', price: '14.50', assigned_to: [1]},
          2: {name: 'Okra', price: '32.45', assigned_to: [1]},
          3: {name: 'Okra', price: '14.50', assigned_to: [4]},
          4: {name: 'Okra', price: '14.50', assigned_to: [3, 2]},
          5: {name: 'Okra', price: '14.50', assigned_to: [4]}
        },
        tax: 14.40,
        tip: 5012.00,
        subtotal: 96.10,
        total: 110.50,
        paid: 72
      }; // TEMP -- REMOVE THIS LATER

      var new_tab = {
        id: 100,
        title: "Dinner at Centerfolds",
        group: [1, 2, 3, 4, 5, 6, 7],
        paid_users: [2, 3, 4],
        currency: '$',
        items: {
          1: {name: 'Okra babadydoopityboopitydoo yeeeeeeeeee', price: '14.50', assigned_to: [1]},
          2: {name: 'Okra', price: '32.45', assigned_to: [1]},
          3: {name: 'Okra', price: '14.50', assigned_to: [4]},
          4: {name: 'Okra', price: '14.50', assigned_to: [3, 2]},
          5: {name: 'Okra', price: '14.50', assigned_to: [4]}
        },
        tax: 14.40,
        tip: 5012.00,
        subtotal: 96.10,
        total: 110.50,
        paid: 72
      }; // TEMP -- REMOVE THIS LATER

      var paid = parseFloat(new_tab.paid);
      var total = parseFloat(new_tab.total);
      $('#payment_progress_chart').val((paid/total*100).toFixed(2)).trigger('change');
      
      var payment_amt = 0;
      for(var item_id in new_tab.items) {
        var item = new_tab.items[item_id];
        if($.inArray(user_id, item.assigned_to) != -1) {
          payment_amt += parseFloat(item.price) / item.assigned_to.length;
        }
      }

      $('#payment_amount').text(payment_amt.toFixed(2));
      $('#payment_rem_amt').text('$' + (total - paid).toFixed(2));
      $('#payment_rem_tot').text('/$' + total.toFixed(2));

      new_tab.paid_users.forEach(function(id) {
        if($.inArray(id, _tab.paid_users) == -1) {
          var $user_entry = $('.paid_user_list .user_entry[data-id=' + id + ']');
          $user_entry.find('.paid_text').text('Paid');
          $user_entry.find('.paid_text').removeClass('text_red').addClass('text_green');
          $user_entry.find('.paid_icon').removeClass('fa-circle-o text_red').addClass('fa-check text_green');
          $user_entry.find('.paid_user_name').text(_group[id].name);
        }
      });

      // Update the global tab object, the group won't change here
      _tab = new_tab;
      setGroupUsers(_tab.group);
    // });
  }

  function updateTip(tip_val) {
    $('#tip_input').val(tip_val.toFixed(2));
    var total_val = (parseFloat(_tab.subtotal) + parseFloat(_tab.tax) + tip_val).toFixed(2);
    $('#total').text(total_val);
    _tab.total = total_val;
  }

  // ---------------------- Event Bindings ----------------------

  //Add a user to the group
  $('#add_friend_button').on('click', function() {
    var friends = get_friends(user_id);
    //activate modal 

    // dont prepend
    $('.friend_group_row').prepend(FriendBlockTemplate({ friends: friends }));
  });

  // Submit an item select
  $('.item_list li').on('click', function(event) {
    $item = $(this);
    var item_id = $item.data('id');
    var item_assigned_to_id = $item.data('assigned_to_id');

    if(user_id == item_assigned_to_id) {
      $.post("select_item_url", { user_id: 10, tab_id: _tab.id, item_id: item_id });
      $item.addClass('selected');
    } else {
      $.post("remove_item_url", { user_id: 10, tab_id: _tab.id, item_id: item_id });
      $item.removeClass('selected');
    }
  });

  $('.tip_button').on('click', function() {
    updateTip(parseFloat($(this).data('percentage')) * parseFloat(_tab.subtotal));
  });

  $('#tip_input').keydown(function(event) {
    if(event.which == 13) {
      event.preventDefault();
      updateTip(parseFloat($('#tip_input').val()));
    }
  });

  $('#make_payment_button').on('click', function(event) {
    $.post('http://app.grasscat.org/get_tab?tab_id=' + user_id, function(result) {

    });
  });

  // Bind open add friends modal button
  $('#tab_open_add_friends').on('click', function() {
    openAddFriends(user_id, _group);
  });

   // Bind confirm add friends button
  $('#tab_add_friends_button').on('click', function() {
    updateAdded();
  });

  // ---------------------- Change Views ----------------------

  $('#tab_view #finish_button').on('click', function(event) {
    // window.location.replace("http://stackoverflow.com");
    $('#add_friend_button').fadeOut(200);
    $('#tab_view').fadeOut(200, function() {
      initPayView();
      $('#pay_view').fadeIn(200);
    });
  });
  
  $('#tab_view #back_button').on('click', function(event) {
    // window.location.replace("http://stackoverflow.com");

  });

  $('#pay_view #back_button').on('click', function(event) {
    // window.location.replace("http://stackoverflow.com");
    $('#add_friend_button').fadeIn(200);
    $('#pay_view').fadeOut(200, function() {
      clearInterval(db_poll_interval);
      db_poll_interval = setInterval(function() { updateTabView() }, 100);
      $('#tab_view').fadeIn(200);
    });
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





