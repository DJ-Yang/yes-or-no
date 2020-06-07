// chart2
$(document).on('click','.chart1 ul li', function(e) {

    let target = $(e.target);

    $('.chart1 ul li').removeClass('active')
    target.addClass('active')

    reset_canvas1(target.parent().parent().parent());


    date = target.attr('class').split(' ')[0]
    get_data(date)
    
});


// chart1
$(document).on('click','.chart2 ul li', function(e) {

    let target = $(e.target);

    $('.chart2 ul li').removeClass('active')
    target.addClass('active')

    

    if (target.hasClass('all')) {        
        reset_canvas2(target.parent().parent().parent(),'all');
        chart_all();  
    } else if (target.hasClass('age')) {
        reset_canvas2(target.parent().parent().parent(),'age');
        chart_age();
    } else if (target.hasClass('gender')) {
        reset_canvas2(target.parent().parent().parent(), 'gender');
        chart_gender();
    }
    
});

$(document).ready(function() {
    get_data('week');
    chart_all();
});


let all_chat_html = $('.canvas-container2').html();
function reset_canvas2(chart, flag) {
    let canvas = chart.children('.canvas-container2')
    canvas.empty();

    if (flag == 'gender') {
        canvas.append('<div class="gender">남자</div><canvas style="width: 180px; height: 180px; margin: 0 auto;" id="chart2-male" class="chart"></canvas><div class="gender">여자</div><canvas style="width: 180px; height: 180px; margin: 0 auto;" id="chart2-female" class="chart"></canvas>');
    } else if (flag == 'age') {
        canvas.append('<div class="age-chart-wrap"><canvas width="100%" height="100%" id="chart2" class="chart-age"></canvas></div>');
    } else if (flag == 'all') {
        text = all_chat_html;
        canvas.append(text);
    }
}

function reset_canvas1(chart) {
    let canvas = chart.children('.canvas-container1')
    canvas.empty();
    canvas.append(' <canvas width="100%" height="100%" id="chart1" class="chart1"></canvas>');
}


// 날짜별 차트 데이터 갖고오는 함수 지금은 임의값
function get_data(date) {
    
    label_data = get_label(date);
    let chart_value = [];
    for( let i=0; i<label_data.length;i++) {
        chart_value.push(Math.floor(Math.random() * 10) + 1);
    }

    chart_date(date,label_data,chart_value);
}

// 날짜별 차트 라벨
function get_label(date) {
    let label_data = [];
    let now = new Date();

    if (date == 'week') {
        for(let i=1;i<=7;i++) {
        
        label_data.push(now.getDate());      
        
        now.setDate(now.getDate()-1)
        
        }
        label_data.reverse();
    } else if (date == 'month') {
        for(let i=1;i<=12;i++) {        
            text = (now.getMonth()+1);
            label_data.push(text);
            now.setMonth(now.getMonth()-1)          
            console.log(now)  
        }
        label_data.reverse()
    } else if (date == 'year') {
        for(let i=1;i<=365;i++) {
            text = now.getFullYear() + '.' + (now.getMonth()+1)+'.'+now.getDate()
            label_data.push(text);   
            now.setDate(now.getDate()-1)
            
        }
    }
    return label_data;  
}


// 전체차트 hover  이벤트
$(document).on('mouseenter','.chart-row .data div', function(e) {
    let tooltip = $('.all-chart-tooltip')
    let color = $('.all-chart-tooltip .square')
    tooltip.css('top',e.pageY);
    tooltip.css('left',e.pageX);
    tooltip.show();


    if ($(e.target).hasClass('agree')) {
        color.css('background-color','#FFDE50')
        $('.all-chart-tooltip .value').text($(e.target).parent().attr('data').split('-')[2]+'%')
    } else if ($(e.target).hasClass('disagree')) {
        color.css('background-color','#666')
        $('.all-chart-tooltip .value').text($(e.target).parent().attr('data').split('-')[3]+'%')
    }
});

// 모바일 환경 툴팁
$(document).on("touchstart",'.chart-row .data div', function(e){
    let tooltip = $('.all-chart-tooltip')
    let color = $('.all-chart-tooltip .square')
    tooltip.css('top',e.pageY);
    tooltip.css('left',e.pageX);
    tooltip.show();


    if ($(e.target).hasClass('agree')) {
        color.css('background-color','#FFDE50')
        $('.all-chart-tooltip .value').text($(e.target).parent().attr('data').split('-')[2]+'%')
    } else if ($(e.target).hasClass('disagree')) {
        color.css('background-color','#666')
        $('.all-chart-tooltip .value').text($(e.target).parent().attr('data').split('-')[3]+'%')
    }   
 });

 
$(document).on('mouseleave','.chart-row .data', function(e) {
    $('.all-chart-tooltip').hide();
});

// 전체차트 value 지정

function chart_all() {
    $.each($('.data-female'), function(k,v) {

        $(v).attr('data',chart_all_female[k]);
        let data = $(v).attr('data').split('-')
        
        let agree = data[2];
        let disagree = data[3];

        $(v).children('.agree').css('width',agree);
        $(v).children('.disagree').css('width',disagree);

    });

    $.each($('.data-male'), function(k,v) {

        $(v).attr('data',chart_all_male[k]);

        let data = $(v).attr('data').split('-')
        
        let agree = data[2];
        let disagree = data[3];

        $(v).children('.agree').css('width',agree);
        $(v).children('.disagree').css('width',disagree);
    });
}

