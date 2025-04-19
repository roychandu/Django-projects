gsap.to(".navbar02", {
    top: "0%",
    borderRadius: "5vw",
    width: "85%",
    yoyo: true,
    scrollTrigger:{
        trigger: ".navbar02",
        scroller: "body",
        start: "top 0%",
        scrub: true,
    }
})

function animateActiveSlide() {
    gsap.from(".carousel-item.active .carousel-caption h1", {
      y: -100,
      duration: 0.7,
      delay: 0.5,
      opacity: 0,
      stagger: 0.5,
      ease: "power2.out"
    });
  
    gsap.from(".carousel-item.active .carousel-caption h2", {
      x: 200,
      duration: 0.8,
      delay: 1,
      opacity: 0,
      stagger: 0.5,
      ease: "power2.out"
    });
  }
  
  // Animate on initial page load
  $(document).ready(function () {
    animateActiveSlide();
  });
  
  // Animate on every slide change
  $('#carouselExampleIndicators').on('slid.bs.carousel', function () {
    animateActiveSlide();
  });
  

