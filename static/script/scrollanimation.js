// scroll animation left to right

$(window).scroll(function () {
    $('.scrollanimation1').each(function () {
        var imagePos = $(this).offset().top;
        var imageHeight = $(this).height();
        var topOfWindow = $(window).scrollTop();

        if (imagePos < topOfWindow + imageHeight && imagePos + imageHeight > topOfWindow) {
            $(this).addClass("slideRight");
        } else {
            $(this).removeClass("slideRight");
        }
    });
});

//end scroll animation left to right

// scroll animation appearance1 description of drone

$(window).scroll(function () {
    $('.scrollanimation2').each(function () {
        var imagePos = $(this).offset().top;
        var imageHeight = $(this).height();
        var topOfWindow = $(window).scrollTop();

        if (imagePos < topOfWindow + imageHeight && imagePos + imageHeight > topOfWindow) {
            $(this).addClass("appearance1");
        } else {
            $(this).removeClass("appearance1");
        }
    });
});

// end scroll animation1 appearance description of drone
