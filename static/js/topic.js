(function addImageToButton() {
  var image1 = "{{ topic.selection1_image.url }}";
  var image2 = "{{ topic.selection2_image.url }}";
  var button1 = document.getElementById('button1');
  var button2 = document.getElementById('button2');

  button1.style.backgroundImage = "url(" + image1 + ")";
  button2.style.backgroundImage = "url(" + image2 + ")";
}());

function selectType(type) {
  if(!confirm('Are you sure you want to delete this?')){
    //prevent sending the request when user clicked 'Cancel'
    e.preventDefault();
  }
}