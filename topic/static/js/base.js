function menuSwitch(e) {
   if (e.id == 'close') {
      $('.side-menu').css('right','-300px'); 
   } else if (e.id == 'open') {
      $('.side-menu').css('right','0'); 
   }   
}

$(document).ready(function() {
   change_navbar();
});

$(window).resize(function (){
   change_navbar();
});

function change_navbar() {
   let screen = window.screen.width;
   
   if (screen>768) {
      $('.menu-btn').addClass('hide');
      $('.menu-box').removeClass('hide'); 
   } else {
      $('.menu-btn').removeClass('hide');
      $('.menu-box').addClass('hide'); 
   }
}

function logout() {
   if(confirm('정말 로그아웃 하시겠습니까?'))
      location.href = '/auth/accounts/logout/'
}