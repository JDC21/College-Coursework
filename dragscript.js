var real1 = 'bull dropBox3';
var real2 = 'engulf dropBox4';
var real3 = 'bear dropBox2';
var real4 = 'reverse dropBox1';
var div = ev.target.id;
var element = ev.dataTransfer.getData('text', ev.target.id);

function insert(id, visible)
{
  document.getElementById('correct').style.visibility = "hidden";
  document.getElementById('incorrect').style.visibility = "hidden";
  document.getElementById('affirm').style.visibility = "hidden";
  document.getElementById('sad').style.visibility = "hidden";
  const imgDestination = document.querySelector('pictures');
  var values = ['bull','engulf','bear','reverse'];
  for (const x of values) {
    document.getElementById(x).style.display = 'none';
  }
  valueToUse = values[Math.floor(Math.random() * values.length)];
  img = document.getElementById(valueToUse);
  document.getElementById('pictures').appendChild(img);
  img.style.display = 'block';
}

function allowDrop(event) {
  event.preventDefault();
}

function drag(event) {
  event.dataTransfer.setData("text", event.target.id);
}

function drop(ev, target) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  if ( event.target.nodeName !== "IMG" ) {
    event.target.appendChild(document.getElementById(data));
    div = ev.target.id;
    element = ev.dataTransfer.getData('text', ev.target.id);
    test = element + " " + div;
  }
}
function answer() {
  if ((test==real1)||(test==real2)||(test==real3)||(test==real4)){
    document.getElementById('correct').style.visibility = "visible";
    document.getElementById('affirm').style.visibility = "visible";
  }
  else if ((test==pictures)||(test==pictures)||(test==pictures)||(test==pictures)) {
    document.getElementById('incorrect').style.visibility = "visible";
    document.getElementById('sad').style.visibility = "visible";
  }
  else {
    document.getElementById('incorrect').style.visibility = "visible";
    document.getElementById('sad').style.visibility = "visible";
  }
}
