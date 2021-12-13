$(document).ready(function () {
    var yPosition;
    var scrolled = 0;
    var $parallaxElements = $(".icons-for-parallax img");
    $(window).scroll(function () {
      scrolled = $(window).scrollTop();
      for (var i = 0; i < $parallaxElements.length; i++) {
        yPosition = scrolled * 0.13 * (i + 0.3);
        $parallaxElements.eq(i).css({ top: yPosition });
      }
    });
  
    var yPosition_main;
    var scrolled_main = 30;
    var $parallax_main = $(".main-img");
    $(window).scroll(function () {
        scrolled_main = $(window).scrollTop();
        yPosition_main = scrolled_main * 0.7;
        $parallax_main.css({ top: yPosition_main });
    });
  });