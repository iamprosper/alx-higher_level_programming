$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus, jqXHR) {
  $('div#hello').text(data.hello);
});
