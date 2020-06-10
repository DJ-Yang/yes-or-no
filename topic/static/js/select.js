// $(document).ready(function() {
    
//     let sel1_top = $('#sel1').offset().top;
//     let sel2_top = $('#sel2').offset().top;
//     let sel1 = $('#sel1').height();
//     let sel2 = $('#sel2').height();
//     let vs_height;
//     console.log(sel1, sel2);
//     console.log(sel1_top, sel2_top);

//     if (sel1>sel2) {
//         vs_height = sel2_top-sel2 + (sel2/2)
//     } else {
//         vs_height = sel1_top-sel1 + (sel1/2)
//     }
   
//     $('.vs').css('top',sel2_top+10);
//     $('.vs').css('display','inline-block')    
// });


$(document).on('click','.selection img', function(e) {

    if (this.id == 'sel1') {
        $('#sel2').parent().parent().addClass('selected');
        $('#sel1').parent().parent().removeClass('selected');
        $('.sel2-des').css('background-color','#333333');
        // $('.sel1-des').css('background-color','#FFDE50');
    } else {
        $('#sel1').parent().parent().addClass('selected');
        $('#sel2').parent().parent().removeClass('selected');
        $('.sel1-des').css('background-color','#333333');
        // $('.sel2-des').css('background-color','f0ff20');
    }

    $('.submit').attr('id',this.id)
})