function menuSwitch(e) {
   
   if (e.id == 'close') {
      $('.side-menu').css('opacity','0')
      $('.side-menu').css('height','0');
      $('.side-menu').css('z-index','-10');
      $('#close').attr('id','open');
   } else if (e.id == 'open') {
      $('.side-menu').css('opacity','1')
      $('.side-menu').css('height','fit-content');
      $('.side-menu').css('z-index','100001');
      $('#open').attr('id','close');
   }   
}

$(document).on('click','.menu-btn' ,function(e) {
   if ($(e.target).attr('id') == 'close') {
      $(e.target).attr('src','/static/img/close.png')
      $(e.target).css('width','20px');
   } else {
      $(e.target).attr('src','/static/img/menu.png')
      $(e.target).css('width','30px');
   }
   console.log();
})

$(document).ready(function() {
   change_navbar();
});

$(window).resize(function (){
   change_navbar();
});

function change_navbar() {
   let screen = window.screen.width;
   
   if (screen>1000) {
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