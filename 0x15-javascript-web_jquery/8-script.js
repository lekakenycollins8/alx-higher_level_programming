$(document).ready(function() {
    let url = "https://swapi-api.alx-tools.com/api/films/?format=json";
    $.get(url, function(data) {
        $.each(data.results, function(index, movie) {
            $("#list_movies").append("<li>" + movie.title + "</li>");
        });
    });
});
