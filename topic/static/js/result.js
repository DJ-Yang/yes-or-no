// chart2
$(document).on('click','.chart1 ul li', function(e) {

    let target = $(e.target);

    $('.chart1 ul li').removeClass('active')
    target.addClass('active')

    reset_canvas1(target.parent().parent().parent());


    date = target.attr('class').split(' ')[0]
    chart_date('date')
    
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
    chart_all();
    chart_date();
});


function reset_canvas2(chart, flag) {
    let canvas = chart.children('.canvas-container2')
    canvas.empty();

    if (flag == 'gender') {
        canvas.append('<canvas style="width: 180px; height: 180px; margin: 0 auto;" id="chart2-male" class="chart"></canvas><canvas style="width: 180px; height: 180px; margin: 0 auto;" id="chart2-female" class="chart"></canvas>');
    } else if (flag == 'age') {
        canvas.append('<canvas width="100%" height="100%" id="chart2" class="chart2"></canvas>');
    }
}

function reset_canvas1(chart) {
    let canvas = chart.children('.canvas-container1')
    canvas.empty();
    canvas.append(' <canvas width="100%" height="100%" id="chart1" class="chart1"></canvas>');
}