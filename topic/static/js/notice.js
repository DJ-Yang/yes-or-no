$(document).ready(function() {
    check_footer_postion();
});

function check_footer_postion() {
    let container_height = $('.container').height();
    let header_height = $('header').height();   
    let screen_height = $(window).height();
    let footer_height = 200;
 
    let check = (container_height+header_height)-screen_height;
 
 
    if (check<0) {
       if (check+footer_height>0) {
          $('footer').css('display','block')
          $('footer').css('position','relative');
       } else {
          $('footer').css('display','block')
          $('footer').css('position','absolute');
          $('footer').css('bottom','0')
       }
       
    } else {
       $('footer').css('display','block')
       $('footer').css('position','relative');
    }
 
 }
