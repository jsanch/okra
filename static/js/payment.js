


  // ---------------------- Event Bindings ----------------------

  $('#make_payment_button').on('click', function(event) {
    event.preventDefault();
    $.post('http://app.grasscat.org/make_payment', { hi: 'hi'})
      .done(function(result) {
        if(result == 'success') {
          $('#payment_success').animate({'opacity': 1}, 200);
        }
      });
  });


// ---------------------- Init ----------------------

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

  getTab(_tab_id).done(function(data) {
    if(!data) return;
    _tab = data;

    setGroupUsers(_tab.group);

    updatePayView();
  });

  // Call pay view update function periodically
  clearInterval(db_poll_interval);
  db_poll_interval = setInterval(function() { updatePayView() }, POLL_DELAY);
}

// ---------------------- Functions ----------------------

function updatePayView() {
  if(!_tab_id) return;
  getTab(_tab_id).done(function(data) {
    var new_tab = data;

    var paid = parseFloat(new_tab.paid) || 0;
    // var paid = 10;
    var total = parseFloat(new_tab.total) || 0;
    $('#payment_progress_chart').val((paid/total*100).toFixed(2) || 0.00).trigger('change');
    
    var payment_amt = getPaymentAmount(new_tab);
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

    // Populate list showing which users have paid
    // if(Object.keys(_group).length != _tab.group.length) {
      $('.paid_user_list').html(PaidUserListTemplate({ users: _group, paid_users: _tab.paid_users }));
    // }

    // Update the global tab object, the group won't change here
    _tab = new_tab;
    setGroupUsers(_tab.group);
  });
}