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
$(document).on('click','nav .nav-menu ul li a', function(e) {   
   let menu = $(e.target);
   $('nav ul li a').removeClass('select');
   menu.addClass('select');
})

// 모바일 메뉴 숨기기 기능
$(document).on('click', function(e) {
   if ($(e.target).hasClass('close') == true || $(e.target).hasClass('mobile-close') == true) {
      $('.mobile-menu').animate({right:'-250px'}, 150);
      $('.mobile-close').removeClass('on');
   }
})
// 모바일 메뉴 펼치기
$('.toggle img').on('click', function(e) {
   $('.mobile-menu').animate({right:'0'}, 150);
   $('.mobile-close').addClass('on');
});

$('.login').on('click', function(e) {
   if($('.popmenu-wrap').hasClass('hide')) {
      $('.popmenu-wrap').removeClass('hide');
   } else {
      $('.popmenu-wrap').addClass('hide');
   }
});


$(document).ready(function() {

   let container_height = $('.container').height();
   let header_height = $('header').height();   
   let screen_height = $(window).height();

   

   let check = (container_height+header_height+100)-screen_height;

   // console.log(container_height, header_height, screen_height);
   // console.log(check);

   if (check<0) {
      $('footer').css('display','block')
      $('footer').css('position','absolute');
      $('footer').css('bottom','0')
   } else {
      $('footer').css('display','block')
      $('footer').css('position','relative');
   }

});