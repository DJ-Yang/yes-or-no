$(document).on('change', 'select[name=sido]', function(e) {
    $.get("/auth/get_form/?sido="+e.target.value,function(res) {
        console.log(res);
        $('#region').html(res);
        $('#region select').css('margin','10px 3px')
    })    
})

