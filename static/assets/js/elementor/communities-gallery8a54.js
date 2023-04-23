(function ($) {
    "use strict";
    $(window).on('elementor/frontend/init', () => {
        elementorFrontend.hooks.addAction('frontend/element_ready/onilife-communities-gallery.default', ($scope) => {
            let $check = $('.communities-slideshow', $scope);
            if ($check.length > 0) {
                let $carousel = $('.onilife-carousel', $scope);
                if ($carousel.length > 0) {
                    let rtl = $('body').hasClass('rtl');
                    $carousel.slick({
                        rtl: rtl,
                        arrows: true,
                        dots: false,
                        infinite: true,
                        speed: 500,
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        autoplay: true,
                        autoplaySpeed: 5000,
                        lazyLoad: 'ondemand',
                        centerMode: true,
                        centerPadding: '0px',
                    });
                }
            }
        });
    });

})(jQuery);



