function menuSwitch(e) {
   if (e.id == 'close') {
      $('.side-menu').css('right','-300px'); 
   } else if (e.id == 'open') {
      $('.side-menu').css('right','0'); 
   }   
}




$(document).ready(function() {
   check_footer_postion();
  
});

$(window).resize(function (){
   check_footer_postion();
});



function check_footer_postion() {
   let container_height = $('.container').height();
   let header_height = $('header').height();   
   let screen_height = $(window).height();
   let footer_height = 110;

   

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