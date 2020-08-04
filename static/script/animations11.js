$(window).scroll(function () {
    $('.animation2').each(function () {
        var imagePos = $(this).offset().top;
        var imageHeight = $(this).height();
        var topOfWindow = $(window).scrollTop();

        if (imagePos < topOfWindow + imageHeight && imagePos + imageHeight > topOfWindow) {
            $(this).addClass("droneimageopacity");
        } else {
            $(this).removeClass("droneimageopacity");
            console.log(imageHeight)
        }
    });
});