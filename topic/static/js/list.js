$(document).ready(function() {
    let now = new Date()
   
    $.each($('.topic-list .default-topic .topic'), function(k,v) {
        let temp = $(v).attr('date').split(',');
        let created_at = new Date(temp[0],temp[1]-1,temp[2],temp[3],temp[4],temp[5])
        
        if (check_new(created_at,now)) {
            $(v).children('.topic-badge').show();
        }

        // image_resize($(v));
    })

});


function check_new(creatd_at, now) {

    let minute = 60*1000
    let hour = 60*minute;
    let day = 24*hour;
    let month = day*30;
    let year = 12*month;


    let diff = now.getTime()-creatd_at.getTime()


    if (diff/hour <= 24) {
        return true;
    } else {
        return false;
    }
    
}

// function image_resize(e) {
//     let box = e.children().children().children('.topic-thumb');

//     let box_width = box.width();
//     let box_height = box.height();

//     let img = e.children().children().children('.topic-thumb').children();
//     let size = img.attr('size').split(',');
    

//     if (size[0]<box_width) {
//         img.css('width',size[0])
//     }
//     if (size[1]<box_height) {
//         img.css('height',size[1])
//     }


//     console.log(size, box_width, box_height)

// }