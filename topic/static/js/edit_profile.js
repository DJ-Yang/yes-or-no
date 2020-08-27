
$(document).ready(function() {
    let data = user_data.split(',');

    // $('input[name=nickname]').val(data[0]);
    $('select[name=age_range]').val(data[1]);
    
    if (data[2] == 'male') {
        $('#id_gender_0').attr('checked','true')
        check_radio(document.getElementById('label-male'));
    } else {
        $('#id_gender_1').attr('checked','true')
        check_radio(document.getElementById('label-female'));
    }
})


$(document).on('change', 'select[name=sido]', function(e) {
    $.get("/auth/get_form/?sido="+e.target.value,function(res) {
        $('#region').html('<span class="label">지역</span> '+res);
        $('#region select').css('margin','0px 3px')
    })    
})


function check_radio(e) {
    $('.radio-container').removeClass('radio-checked');
    $(e).addClass('radio-checked');
}
