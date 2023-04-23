(function ($) {
    "use strict";
    $(window).on('elementor/frontend/init', () => {
        elementorFrontend.hooks.addAction('frontend/element_ready/onilife-communities-map.default', ($scope) => {
            let $map = $(".map-data-communities", $scope);
            if ($map.length) {
                $map.each(function () {
                    initMap($(this));
                });
            }
        });
    });

    function initMap($container) {
        var svgMarkup = '<svg width="27" height="32" viewBox="0 0 27 32" fill="none" xmlns="http://www.w3.org/2000/svg">'+
            '<path d="M22.4894 3.85412C23.76 5.15294 24.72 6.60706 25.3694 8.21647C26.0188 9.82588 26.3435 11.4776 26.3435 13.1718C26.3435 14.8659 26.0188 16.5176 25.3694 18.1271C24.72 19.7365 23.76 21.1906 22.4894 22.4894L13.8494 31.1294C13.6518 31.3271 13.4259 31.4259 13.1718 31.4259C12.9176 31.4259 12.6918 31.3271 12.4941 31.1294L3.85412 22.4894C2.58353 21.2188 1.62353 19.7647 0.974118 18.1271C0.324706 16.4894 0 14.8376 0 13.1718C0 11.5059 0.324706 9.85412 0.974118 8.21647C1.62353 6.57882 2.59059 5.12471 3.87529 3.85412C5.16 2.58353 6.60706 1.62353 8.21647 0.974118C9.82588 0.324706 11.4776 0 13.1718 0C14.8659 0 16.5176 0.324706 18.1271 0.974118C19.7365 1.62353 21.1906 2.58353 22.4894 3.85412ZM16.2212 16.2212C16.6447 15.7976 16.9553 15.3176 17.1529 14.7812C17.3506 14.2447 17.4494 13.7082 17.4494 13.1718C17.4494 12.6353 17.3506 12.0988 17.1529 11.5624C16.9553 11.0259 16.6447 10.5459 16.2212 10.1224C15.7976 9.69882 15.3176 9.38824 14.7812 9.19059C14.2447 8.99294 13.7082 8.89412 13.1718 8.89412C12.6353 8.89412 12.0988 8.99294 11.5624 9.19059C11.0259 9.38824 10.5459 9.69882 10.1224 10.1224C9.69882 10.5459 9.38824 11.0259 9.19059 11.5624C8.99294 12.0988 8.88 12.6353 8.85176 13.1718C8.82353 13.7082 8.93647 14.2447 9.19059 14.7812C9.44471 15.3176 9.75529 15.7976 10.1224 16.2212C10.4894 16.6447 10.9694 16.9553 11.5624 17.1529C12.1553 17.3506 12.6918 17.4635 13.1718 17.4918C13.6518 17.52 14.1882 17.4071 14.7812 17.1529C15.3741 16.8988 15.8541 16.5882 16.2212 16.2212Z" fill="#FF4610"/>'+
            '</svg>';
        var lat = $container.attr('data-lat');
        var lng = $container.attr('data-lng');
        var zoom_value = parseInt($container.attr('data-zoom'));

        var mapOptions = {
            center: new google.maps.LatLng(lat, lng),
            zoom: zoom_value,
            styles: $container.data('color')
        };

        var map = new google.maps.Map($container.get(0), mapOptions);
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(lat, lng),
            map: map,
            icon: {
                url: 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgMarkup),
                scaledSize: {
                    height: 32,
                    width: 27
                }
            }
        });
        marker.setMap(map);
    }

})(jQuery);