$(function() {

  $('.title').text()

  function getTab() {
    return $.get("http://app.grasscat.org/get_tab?tab_id=12");
  };

  function getUser() {
    return $.get("http://app.grasscat.org/get_user?user_id=12");
  };

  




});