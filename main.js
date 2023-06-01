window.addEventListener("DOMContentLoaded", function() {
    // Apply fade-in effect once the content is loaded
    document.body.style.opacity = 1;
  });
  
  function navigateToPage(url) {
    // Apply fade-out effect before navigating to the new page
    document.body.style.opacity = 0;
    
    // Delay the navigation to allow the fade-out effect to take place
    setTimeout(function() {
      window.location.href = url;
    }, 300); // Adjust the delay duration if needed
  }
  