$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json',
  function (data, textStatus, jqXHR) {
    $('div#character').text(data.name);
  });
