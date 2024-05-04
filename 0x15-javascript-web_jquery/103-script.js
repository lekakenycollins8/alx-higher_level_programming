$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      dataType: 'json',
      data: { lang: languageCode },
      success: function (response) {
        $('#hello').text(response.hello);
      },
      error: function (xhr, status, error) {
        console.error('Status:', status);
        console.error('Error:', error);
        $('#hello').text('Error: Failed to fetch translation');
      }
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (e) {
    if (e.which == 13) { // 13 is the ENTER key code
      fetchTranslation();
    }
  });
});
