$('#toggle_header').on('click', function () {
  $('header').toggleClass(function () {
    if ($(this).is('.red')) {
      $(this).removeClass('red');
      return 'green';
    } else {
      $(this).removeClass('green');
      return 'red';
    }
  });
});
