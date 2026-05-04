
// Homepage Slide

  var slides = document.getElementsByClassName("slide");
  var currentSlide = 0;

  function showSlide() {
    slides[currentSlide].style.display = "none";
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].style.display = "block";
  }

  // Change slide every 2 seconds
  setInterval(showSlide, 2000);

  // Show the first slide initially
  slides[0].style.display = "block";

// End of Homepage Slide  
