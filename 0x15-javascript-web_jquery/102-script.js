$(function () {
  $('input#btn_translate').on('click', function () {
    const code = $('input#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
    $.get(url, function (data) {
      $('div#hello').html(data.hello);
    });
  });
});
