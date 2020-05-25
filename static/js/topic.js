function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function selectType(select, id, type) {
  if(!confirm('당신은 '+ select + '을 선택하셨습니다. 맞습니까?')) {
    return null
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });
  $.ajax({
        url:'/topic/set/selection/',
        type: "POST",
        data: {
          topic_id : id,
          type : type,
        },
        success:function(response){
          alert('성공');
          console.log(response);
          location.href='result/';
        },
        complete:function(){},
        error:function (xhr, textStatus, thrownError)
        {
          console.log(xhr, textStatus, thrownError)
        }
  })
}