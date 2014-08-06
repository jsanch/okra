
var FriendRowTemplate;
var FriendBlockTemplate;
var ItemListTemplate;
var ItemTemplate;
var PaidUserListTemplate;

$(function() {

  // ---------------------- Handlebars helpers ----------------------
  
  FriendRowTemplate = Handlebars.compile($('#friend_row_template').html());
  FriendBlockTemplate = Handlebars.compile($('#friend_block_template').html());
  ItemListTemplate = Handlebars.compile($('#item_list_template').html());
  ItemTemplate = Handlebars.compile($('#item_template').html());
  PaidUserListTemplate = Handlebars.compile($('#paid_user_list_template').html());

  Handlebars.registerPartial("item_template", $("#item_template").html());
  Handlebars.registerPartial("paid_user_entry_template", $("#paid_user_entry_template").html());

  Handlebars.registerHelper('get_name', function(user_id) {
    var user = friends[user_id];
    return user? user.first_name + ' ' + user.last_name : 'None';
  });

  Handlebars.registerHelper('get_pic_url', function(user_id) {
    if(_group && _group[user_id]) {
      return _group[user_id].pic_url;
    } else {
      return;
    }
  });

  Handlebars.registerHelper('user_selected', function(assigned_to) {
    return $.inArray(String(user_id), assigned_to) != -1;
  });

  Handlebars.registerHelper('check_paid', function(user_id, paid_users) {
    return $.inArray(user_id, paid_users) != -1;
  });

  Handlebars.registerHelper('format_decimal', function(val, precision) {
    return parseFloat(val).toFixed(precision);
  });

  // ---------------------- Event Bindings ----------------------

  // Submit an item select
  $(document).on('click', '.item_list .tab_item', function(event) {
    $item = $(this);
    var item_id = $item.data('id');
    var item_assigned_to = _tab.items[item_id].assigned_to;

    if($.inArray(String(user_id), item_assigned_to) == -1) {
      $.post("http://app.grasscat.org/add_user_to_item", { user_id: user_id, tab_id: _tab_id, item_id: item_id });
      $item.addClass('selected');
    } else {
      $.post("http://app.grasscat.org/remove_user_from_item", { user_id: user_id, tab_id: _tab_id, item_id: item_id });
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

  // Bind open add friends modal button
  $('#tab_open_add_friends').on('click', function() {
    openAddFriends(user_id, friends_to_add);
  });

});

// ---------------------- Init ----------------------

function initTabView(tab_id) {
  _tab_id = tab_id;

  // Initially populate page
  populatePage();

  // Update page periodically
  clearInterval(db_poll_interval);
  db_poll_interval = setInterval(function() { updateTabView() }, POLL_DELAY);
}

// ---------------------- Functions ----------------------

// Get the group users from the list of ids
function setGroupUsers(group) {
  _group = {};
  group.forEach(function(id) {
    getUser(id).done(function(data) {
      if(!data) return;
      var user = JSON.parse(data);
      _group[user._id] = user;
    });
  });

  // _group = {
  //   1: {first_name: 'Barack', last_name: 'Obama'},
  //   2: {first_name: 'Curioussssss omgomgomgomgomgomgomgogm', last_name: 'George'},
  //   3: {first_name: 'Michael', last_name: 'Vader'},
  //   4: {first_name: 'Darth', last_name: 'Vader'},
  //   5: {first_name: 'Darth', last_name: 'Vader'},
  //   6: {first_name: 'Darth', last_name: 'Vader'},
  //   7: {first_name: 'Darth', last_name: 'Vader'},
  // };
}

function populatePage() {
  getTab(_tab_id).done(function(data) {
    if(!data) return;
    _tab = data;

    // Set the group object
    setGroupUsers(_tab.group);

    // Populate friends list
    $('.friend_group_row .friend_block').remove();
    $('.friend_group_row').prepend(FriendRowTemplate({ friends: _group }));
    // Populate item list
    $('.item_list').html(ItemListTemplate({ items: _tab.items }));

    $('#title').text(_tab.title);
    $('#tax').text('$' + parseFloat(_tab.tax).toFixed(2));
    $('#tip_input').val(_tab.tip);
    $('#subtotal').text('$' + parseFloat(_tab.subtotal));
    $('#total').text('$' + parseFloat(_tab.total));

    if(user_id == _tab.master_user_id) {
      $('#finish_button').text('View Payments >');
    } else {
      $('#finish_button').text('Finish and Pay >');
    }

    getUser(user_id).done(function(data) {
      var friend = JSON.parse(data);
      $('.friend_group_row').prepend(FriendBlockTemplate(friend));
    });
    updateTabView();
  });
}

function updateTabView() {
  if(!_tab_id) return;
  getTab(_tab_id).done(function(data) {
    var new_tab = data;

    // Update friends if it has changed
    new_tab.group.forEach(function(id) {
      if($.inArray(id, _tab.group) == -1) {
        getUser(id).done(function(data) {
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
      if(!is_same(_tab.items[item_id].assigned_to, new_tab.items[item_id].assigned_to)) {
        var item = {};
        // var a = new_tab.items[item_id];
        item[item_id] = new_tab.items[item_id];
        $('.item_list .tab_item[data-id=' + item_id + ']').replaceWith(ItemListTemplate({items: item}))
          .addClass('selected');
      }
    }

    var payment_amt = getPaymentAmount(new_tab);
    $('#user_pay_amt').text('$' + payment_amt.toFixed(2));

    // Update the global tab object
    _tab = new_tab;
    setGroupUsers(_tab.group);
  });
}

function updateTip(tip_val) {
  $('#tip_input').val(tip_val.toFixed(2));
  var total_val = (parseFloat(_tab.subtotal) + parseFloat(_tab.tax) + tip_val).toFixed(2);
  $('#total').text('$' + total_val);
  _tab.total = total_val;

  $.post("http://app.grasscat.org/update_tip", { tab_id: _tab_id, tip_val: tip_val });
}

function getPaymentAmount(tab) {
  var payment_amt = 0;
  for(var item_id in tab.items) {
    var item = tab.items[item_id];
    if($.inArray(String(user_id), item.assigned_to) != -1) {
      payment_amt += parseFloat(item.price) / item.assigned_to.length;
    }
  }

  payment_amt += (parseFloat(tab.tax) + parseFloat(tab.tip)) * (payment_amt / parseFloat(tab.subtotal));
  return payment_amt;
}

// ---------------------- Prototype ----------------------

function is_same(arr1, arr2) {
  if (arr1.length != arr2.length) return false;
  for (var i = 0; i < arr2.length; i++) {
    if (arr1[i].compare) { 
      if (!arr1[i].compare(arr2[i])) return false;
    }
    if (arr1[i] !== arr2[i]) return false;
  }
  return true;
} 


// var _tab = {
//   id: 100,
//   title: "Dinner at Centerfolds",
//   group: [1, 2, 3, 4, 5, 6, 7],
//   paid_users: [],
//   currency: '$',
//   items: {
//     1: {name: 'Okra babadydoopityboopitydoo yeeeeeeeeee', price: '14.50', assigned_to: [1]},
//     2: {name: 'Okra', price: '32.45', assigned_to: [1]},
//     3: {name: 'Okra', price: '14.50', assigned_to: [4]},
//     4: {name: 'Okra', price: '14.50', assigned_to: [3, 2]},
//     5: {name: 'Okra', price: '14.50', assigned_to: [4]}
//   },
//   tax: 14.40,
//   tip: 5012.00,
//   subtotal: 96.10,
//   total: 110.50,
//   paid: 72
// }; // TEMP -- REMOVE THIS LATER




