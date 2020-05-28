$(document).ready(function() {
    let now = new Date()

    let year = String(now.getFullYear());
    let month = String(now.getMonth()+1);
    let date = String(now.getDate());
    
    let ymd_text = parseInt(year+month+date);
    
    
    $.each($('.topic-list .default-topic .topic'), function(k,v) {
        let topic_ymd = parseInt($(v).attr('date'));
        if (ymd_text - topic_ymd < 1) {
            $(v).children('.topic-badge').show();
        } else {
            $(v).children('.topic-badge').hide();
        }
    })

});
