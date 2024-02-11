$(document).ready(function () {
  // Start NProgress when document is ready
  NProgress.start();

  // Bind to window load event to complete NProgress
  $(window).on('load', function () {
    NProgress.done();
  });

  // Handle AJAX requests or other asynchronous loads
  $(document).ajaxStart(function() {
    NProgress.start();
  }).ajaxStop(function() {
    NProgress.done();
  });

  // For single-page applications or dynamic content loading
  // Adjust this part to your specific case
  // function updateContent() {
  //   NProgress.start();
  //   // load content
  //   // ...
  //   NProgress.done();
  // }

  // Error handling for failed content loading
  // $(document).ajaxError(function() {
  //   NProgress.done();
  //   // Optionally show an error message
  // });

  // Bind NProgress to start on link click
  $(document).on('click', 'a', function () {
    NProgress.start();
    // Add a reasonable timeout to ensure 'done' is called
    setTimeout(function() {
      NProgress.done();
    }, 1000); // Adjust based on your needs
  });
});
