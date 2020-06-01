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
    } else if (flag == 'all') {
        text = ' <div class="all-chart">                    <div class="chart-title" style="display: flex;">                        <div class="female">여자</div>                        <div class="male">남자</div>                    </div>                    <div class="chart-row">                        <div class="data" data="female-10">                            <div class="agree"></div>                        </div>                        <div class="legend">10대</div>                        <div class="data" data="male-10">                            <div class="agree"></div>                        </div>                    </div>                    <div class="chart-row">                        <div class="data" data="female-10">                            <div class="agree"></div>                        </div>                        <div class="legend">20대</div>                        <div class="data" data="male-10">                            <div class="agree"></div>                        </div>                    </div>                    <div class="chart-row">                        <div class="data" data="female-10">                            <div class="agree"></div>                        </div>                        <div class="legend">30대</div>                        <div class="data" data="male-10">                            <div class="agree"></div>                        </div>                    </div>                    <div class="chart-row">                        <div class="data" data="female-10">                            <div class="agree"></div>                        </div>                        <div class="legend">40대</div>                        <div class="data" data="male-10">                            <div class="agree"></div>                        </div>                    </div>                    <div class="chart-row">                        <div class="data" data="female-10">                            <div class="agree"></div>                        </div>                        <div class="legend">50대</div>                        <div class="data" data="male-10">                            <div class="agree"></div>                        </div>                    </div>                </div>'
        canvas.append(text);
    }
}

function reset_canvas1(chart) {
    let canvas = chart.children('.canvas-container1')
    canvas.empty();
    canvas.append(' <canvas width="100%" height="100%" id="chart1" class="chart1"></canvas>');
}