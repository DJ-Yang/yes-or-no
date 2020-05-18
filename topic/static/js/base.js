// navbar 따라다니는 기준 스크롤
$(window).scroll(function(){
    if ($(window).scrollTop() >= 100) {
       $('nav').addClass('fixed-header');
    }
    else {
       $('nav').removeClass('fixed-header');
    }
});  

// navbar 메뉴 선택시 강조옵션
$(document).on('click','nav ul li a', function(e) {   
   let menu = $(e.target);
   $('nav ul li a').removeClass('select');
   menu.addClass('select');
})