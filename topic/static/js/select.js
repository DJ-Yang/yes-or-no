$(document).on('click','.selection', function(e) {

    let pick = $(e.target);

    $('input[name=pick]').val(pick.attr('data'));
    $('.selection').addClass('selection-active');
    $(e.target).removeClass('selection-active');
});

$(document).ready(function() {
    let selection_count = $('.select-box').find('.selection').length;

    if (selection_count==2) {
        $('.selection').css('width','280px');
        $('.selection').css('height','280px');
    }

});