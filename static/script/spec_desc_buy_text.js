$('.readReview').click(function(e) {
  e.preventDefault();
  $(this).text(function(i, t) {
    return t == 'Close' ? 'Read Review' : 'Close';
  }).prev('.more-cont').slideToggle()
});