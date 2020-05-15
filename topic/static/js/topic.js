(function addImageToButton() {
  var image1 = "{{ topic.selection1_image.url }}";
  var image2 = "{{ topic.selection2_image.url }}";
  var button1 = document.getElementById('button1');
  var button2 = document.getElementById('button2');

  button1.style.backgroundImage = "url(" + image1 + ")";
  button2.style.backgroundImage = "url(" + image2 + ")";
}());
