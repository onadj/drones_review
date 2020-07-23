$('.readMore').click(function(e) {
  e.preventDefault();
  $(this).text(function(i, t) {
    return t == 'Read Less' ? 'Read More' : 'Read Less';
  }).prev('.more-cont').slideToggle()
});