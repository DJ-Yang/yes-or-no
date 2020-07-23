$(document).ready(function() {
    set_chart_data();   
});


$('.analysis-title-row div').on('click', function(e) {
    if ($(e.target).hasClass('category')) {
        $('.date').removeClass('chart-active');
        $('.category').addClass('chart-active');
        $('.category img').attr('src','/static/img/chart_active.png');
        $('.date img').attr('src','/static/img/date.png');


    } else if ($(e.target).hasClass('date')) {
        alert('데이터 수집중입니다.');
        // $('.date').addClass('chart-active');
        // $('.category').removeClass('chart-active');
        // $('.category img').attr('src','/static/img/chart.png');
        // $('.date img').attr('src','/static/img/date_active.png');
    }
})

$('.share-btn').on('click', function(e) {
    console.log(location.href.split('result')[0])
    $('#modal').css('display','block');
    let copy_text = location.href.split('result')[0] + 'check/'
    $('input[name=share_link]').val(copy_text);
});

$('.modal-content .close').on('click', function(e) {
    $('#modal').css('display','none');
})

$('.modal').on('click', function(e) {
    if (e.target == modal) {
        $('#modal').css('display','none');
    }
});

$('.fa-external-link').on('click', function() {
    var tempElem = document.createElement('textarea');
    tempElem.value = copy_data = $('input[name=share_link]').val();
    document.body.appendChild(tempElem);
  
    tempElem.select();
    document.execCommand("copy");
    document.body.removeChild(tempElem);
    alert('클립보드에 복사되었습니다.')
})