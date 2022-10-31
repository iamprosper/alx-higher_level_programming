$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json',
  function (data, textStatus, jqXHR) {
    const movies = data.results;
    movies.forEach(extractTitle);
    function extractTitle (value, index, array) {
      $('#list_movies').append('<li>' + value.title + '</li>');
    }
  });
