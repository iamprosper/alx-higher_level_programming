$(function () {
  $('input#btn_translate').on('click', function () {
    displayHello();
  });

  $('input#language_code').bind('enterKey', function (e) {
    displayHello();
  });

  $('input#language_code').keyup(function (e) {
    if (e.keyCode === 13) $(this).trigger('enterKey');
  });

  function displayHello () {
    const code = $('input#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
    $.get(url, function (data) {
      $('div#hello').html(data.hello);
    });
  }
});
