// Add dropdowns
$('.dropdown-toggle').dropdown();

function savePost() {
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
