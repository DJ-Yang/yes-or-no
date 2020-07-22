$(document).on('click', '.selection', function (e) {

    let pick = $(e.target);
    if (pick.hasClass('selection-text')) {
        pick = pick.parent().parent();
    }
    $('input[name=pick]').val(pick.attr('data'));
    $('.selection').removeClass('selection-active');
    pick.addClass('selection-active');
});

$(document).ready(function () {

    resizeSelection();

});

$(window).resize(function() {
    resizeSelection();
});

function resizeSelection() {
    let selection_count = $('.select-box').find('.selection').length;
    if (selection_count == 2) {
        if (window.screen.width > 670) {
            $('.selection').css('width', '280px');
            $('.selection').css('height', '280px');
            $('.select-wrapper').css('height','600px');
            
        } else if(window.screen.width > 380 && window.screen.width < 480) {
            $('.selection').css('width', '150px');
            $('.selection').css('height', '150px');
            $('.select-wrapper').css('height','300px');
        } else if(window.screen.width > 360 && window.screen.width <= 380) {
            $('.selection').css('width', '140px');
            $('.selection').css('height', '140px');
            $('.select-wrapper').css('height','300px');
        } else if(window.screen.width <= 360) {
            $('.selection').css('width', '140px');
            $('.selection').css('height', '140px');
            $('.select-wrapper').css('height','360px');
            $('.selection-text').css('font-size','12px');
        }
    }
}

