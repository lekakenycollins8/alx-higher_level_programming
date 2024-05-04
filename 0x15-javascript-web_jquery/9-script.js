$(document).ready(function() {
    let url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
    $.get(url, function(data) {
        $("#hello").text(data.hello)
    });
});
