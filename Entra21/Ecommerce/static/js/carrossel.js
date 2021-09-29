const $responsiveCarousel = document.querySelector(".js-carousel--responsive");

new Glider($responsiveCarousel, {
  slidesToShow: 1,
  slidesToScroll: 1,
  draggable: true,
  duration: 0.25,
  dots: ".js-carousel--responsive-dots",
  arrows: {
    prev: ".js-carousel--responsive-prev",
    next: ".js-carousel--responsive-next",
  },
  scrollLock: true,
  responsive: [
    {
      breakpoint: 750,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
      },
    },
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
      },
    },
    {
      breakpoint: 500,
      settings: {
          slidesToScroll: 1,
          slidesToShow: 1,
          dots: false,
          arrows: false,
          scrollLock: true
      }
  }
  ],
});