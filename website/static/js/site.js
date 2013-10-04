// Add dropdowns
$('.dropdown-toggle').dropdown();

function savePost() {
  data = $('#id-newPostForm').serialize();
  $.ajax({
    url: '/posts/posts/',
    method: 'post',
    data: data,
    success: function(response) {
      alert(response);
      $('#id-preparePost').modal('hide');
    }
  });
};
