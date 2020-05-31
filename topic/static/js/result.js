// chart2
$(document).on('click','.chart1 ul li', function(e) {

    let target = $(e.target);

    $('.chart1 ul li').removeClass('active')
    target.addClass('active')

    reset_canvas1(target.parent().parent().parent());

    if (target.hasClass('week')) {        
        
    } else if (target.hasClass('month')) {
        
    } else if (target.hasClass('year')) {
        
    }
    
});


// chart1
$(document).on('click','.chart2 ul li', function(e) {

    let target = $(e.target);

    $('.chart2 ul li').removeClass('active')
    target.addClass('active')

    reset_canvas2(target.parent().parent().parent());

    if (target.hasClass('all')) {        
        chart_all();  
    } else if (target.hasClass('age')) {
        chart_age();
    } else if (target.hasClass('gender')) {
        chart_gender();
    }
    
});

$(document).ready(function() {
    chart_all();
    chart_date();
});


function reset_canvas2(chart) {
    let canvas = chart.children('.canvas-container2')
    canvas.empty();
    canvas.append(' <canvas width="100%" height="100%" id="chart2" class="chart2"></canvas>');
}

function reset_canvas1(chart) {
    let canvas = chart.children('.canvas-container1')
    canvas.empty();
    canvas.append(' <canvas width="100%" height="100%" id="chart1" class="chart1"></canvas>');
}