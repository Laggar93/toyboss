const swiper = [
  new Swiper('.news-block .swiper', {
    loop: true,
    autoplay: {
      delay: 3000,
    },
    breakpoints: {
      // mobile + tablet - 320-990
      320: {
        slidesPerView: 1
      },
      640: {
        slidesPerView: 2
      },

      960: {
        slidesPerView: 3
      },

      1532: {
        slidesPerView: 4
      },
    },
    pagination: {
      el: '.news-block .swiper-pagination',
    },
    spaceBetween: 30,
    navigation: {
      nextEl: '.news-block .swiper-button-next',
      prevEl: '.news-block .swiper-button-prev',
    },

  }),
  new Swiper('.certificate-block .swiper', {
    loop: true,
    spaceBetween: 20,
    autoplay: {
      delay: 3000,
    },
    breakpoints: {
      // mobile + tablet - 320-990
      320: {
        slidesPerView: 1
      },
      640: {
        slidesPerView: 2
      },

      960: {
        slidesPerView: 3
      },
      1200: {
        slidesPerView: 4
      },

      1532: {
        slidesPerView: 5
      },
    },
    pagination: {
      el: '.certificate-block .swiper-pagination',
    },
    navigation: {
      nextEl: '.certificate-block .swiper-button-next',
      prevEl: '.certificate-block .swiper-button-prev',
    },

  }),

  new Swiper('.group-of-companies-block .swiper', {
    loop: true,
    spaceBetween: 4,
    autoplay: {
      delay: 3000,
    },
    breakpoints: {
      // mobile + tablet - 320-990
      320: {
        slidesPerView: 1
      },
      640: {
        slidesPerView: 2
      },

      960: {
        slidesPerView: 3
      },
      1200: {
        slidesPerView: 4
      },

      1532: {
        slidesPerView: 4
      },
    },
    pagination: {
      el: '.group-of-companies-block .swiper-pagination',
    },
    navigation: {
      nextEl: '.group-of-companies-block .swiper-button-next',
      prevEl: '.group-of-companies-block .swiper-button-prev',
    },

  }),
  new Swiper('.advantages-block.mode .swiper', {
    loop: true,
    spaceBetween: 30,
    // autoplay: {
    //     delay: 3000,
    // },
    breakpoints: {
      // mobile + tablet - 320-990
      320: {
        slidesPerView: 1
      },
      640: {
        slidesPerView: 2
      },

      960: {
        slidesPerView: 3
      },
      1200: {
        slidesPerView: 4
      },

      1532: {
        slidesPerView: 5
      },
    },
    pagination: {
      el: '.advantages-block.mode .swiper-pagination',
    },
    navigation: {
      nextEl: '.advantages-block.mode .swiper-button-next',
      prevEl: '.advantages-block.mode .swiper-button-prev',
    },

  }),

  new Swiper('.advantages-block.not-mode .swiper', {
    loop: true,
    spaceBetween: 30,
    autoplay: {
      delay: 3000,
    },
    breakpoints: {
      // mobile + tablet - 320-990
      320: {
        slidesPerView: 1
      },
      640: {
        slidesPerView: 2
      },

      960: {
        slidesPerView: 3
      },
      1200: {
        slidesPerView: 4
      },

      1532: {
        slidesPerView: 6
      },
    },
    pagination: {
      el: '.advantages-block.not-mode .swiper-pagination',
    },
    navigation: {
      nextEl: '.advantages-block.not-mode .swiper-button-next',
      prevEl: '.advantages-block.not-mode .swiper-button-prev',
    },

  }),



  new Swiper('.main-block .swiper', {
    loop: true,
    slidesPerView: 1,
    speed: 3200,
    // autoplay: {
    //   delay: 10000,
    // },
    spaceBetween: 0,
    pagination: {
      el: '.main-block .swiper-pagination',
    },
    navigation: {
      nextEl: '.main-block .swiper-button-next',
      prevEl: '.main-block .swiper-button-prev',
    },

  }),
  new Swiper('.news-detail .swiper', {
    loop: true,
    slidesPerView: 1,
    autoplay: {
      delay: 3000,
    },
    speed: 1200,
    spaceBetween: 10,
    pagination: {
      el: '.news-detail .swiper-pagination',
    },
    navigation: {
      nextEl: '.news-detail .swiper-button-next',
      prevEl: '.news-detail .swiper-button-prev',
    },

  }),
  new Swiper('.products-info-row .swiper', {
    loop: true,
    slidesPerView: 2,
    autoplay: {
      delay: 3000,
    },
    speed: 1200,
    spaceBetween: 30,
    breakpoints: {
      // mobile + tablet - 320-990
      0: {
        slidesPerView: 1,
      },
      1200: {
        slidesPerView: 2,
      },

    },
    pagination: {
      el: '.products-info-row .swiper-pagination',
    },
    navigation: {
      nextEl: '.products-info-row .swiper-button-next',
      prevEl: '.products-info-row .swiper-button-prev',
    },

  }),


]

const customSlider = new Swiper('.production-block-carousel .swiper', {
  loop: true,
  spaceBetween: 4,
  centeredSlides: true,
  speed: 1000,
  breakpoints: {
    // mobile + tablet - 320-990
    320: {
      slidesPerView: 1
    },
    960: {
      slidesPerView: 2
    },
    1532: {
      slidesPerView: 2
    },
  },
  pagination: {
    el: '.production-block-carousel .swiper-pagination',
  },
  navigation: {
    nextEl: '.production-block-carousel .swiper-button-next',
    prevEl: '.production-block-carousel .swiper-button-prev',
  },

})

// $('.production-block-carousel .swiper .swiper-slide-next').on('mouseover', function() {
//   console.log(customSlider)
//   customSlider.update()
//   customSlider.slideNext(900)
// })
$('.production-block-carousel .swiper-slide').on('mouseover', function() {
  customSlider.slideTo($(this).index());
})

const historySwiper = new Swiper('.history-block .swiper', {
  // on: {
  //   activeIndexChange: function (e) {
  //     console.log(e.realIndex);
  //     $("#tab-history").tabs({
  //       active: e.realIndex
  //     });
  //   },
  // },
  loop: false,

  speed: 2000,
  allowTouchMove: false,
  centeredSlides: true,
  scrollbar: {
    draggable: false,
  },
  breakpoints: {
    // mobile + tablet - 320-990
    320: {
      slidesPerView: 1,
      spaceBetween: 90,
    },
    960: {
      slidesPerView: 3,
      spaceBetween: 90,
    },


    1200: {
      slidesPerView: 3,
      spaceBetween: 120,
    },
    1532: {
      slidesPerView: 5,
      spaceBetween: 120,
    },

  },
  navigation: {
    nextEl: '.history-block .swiper-button-next',
    prevEl: '.history-block .swiper-button-prev',
  },

})
$('.history-block .swiper-slide').on('mouseover', function() {
  historySwiper.slideTo($(this).index());
})