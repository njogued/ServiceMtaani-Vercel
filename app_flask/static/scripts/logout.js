$(document).ready(function() {
    $('#logout-btn').click(function() {
      // Send an AJAX request to the Flask route for logout
      $.get('/logout', function(data) {
        // Redirect to the homepage or any other desired page
        window.location.href = '/';
      });
    });
  });
  