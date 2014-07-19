
$(function() {
  var FriendBlockTemplate = Handlebars.compile($('#friend_block_template').html());
  var ItemListTemplate = Handlebars.compile($('#item_list_template').html());

  $.get("friend_url", function(friends) {
    $('.friend_group_row').prepend(FriendBlockTemplate({ friends: friends }));
  });

  // $.get("tab_url", function(tab) {

  //   // Populate friends list
  //   $('.friend_group_row').prepend(FriendBlockTemplate({ friends: friends }));
  //   // Populate item list
  //   $('.item_list').html(ItemListTemplate({ items: tab.items }));
  // });
  var user_id = 10;

  var friends = {
    1: {name: 'Obama'},
    2: {name: 'Mike "sexy" Wang'}
  };

  var tab = {
    id: 100,
    user: [123, 123, 123],
    currency: '$',
    items: {
      1: {name: 'Okra', price: '14.50', assigned_to_id: 1, assigned_to_name: 'Obama'},
      2: {name: 'Okra', price: '14.50', assigned_to_id: 1, assigned_to_name: 'Obama'},
      3: {name: 'Okra', price: '14.50', assigned_to_id: 1, assigned_to_name: 'Obama'},
      4: {name: 'Okra', price: '14.50', assigned_to_id: 2, assigned_to_name: 'Mike'},
      5: {name: 'Okra', price: '14.50', assigned_to_id: 2, assigned_to_name: 'Mike'},
    },
    tax: 14.44,
    tip: 50.00
  }

  // Populate friends list
  $('.friend_group_row').prepend(FriendBlockTemplate({ friends: friends }));

  // Populate item list
  $('.item_list').html(ItemListTemplate({ items: tab.items }))


  // ---------------------- Event Bindings ----------------------

  // Submit an item select
  $('.item_list li').on('click', function(event) {
    var item_id = $(this).data('id');
    var item_assigned_to_id = $(this).data('assigned_to_id');

    if(user_id == item_assigned_to_id) {
      $.post("select_item_url", { user_id: 10, tab_id: tab.id, item_id: item_id });
    } else {
      $.post("remove_item_url", { user_id: 10, tab_id: tab.id, item_id: item_id });
    }
  });
});






