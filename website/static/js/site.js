// Add dropdowns
$('.dropdown-toggle').dropdown();

function savePost1() {
  $('#id-newPostForm :input :button').prop('disabled', true);
  data = $('#id-newPostForm').serialize();
  $.ajax({
    url: '/posts/posts/',
    method: 'post',
    data: data,
    success: function(response) {
      $('#id-newPostForm')[0].reset();
      $('#id-preparePost').modal('hide');
    }
  });
};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
