// JavaScript Document

function mouseOver() {
  document.getElementById("neutral").style.display = "none";
  document.getElementById("affirm").style.display = "block";
  document.getElementById("response1").style.display = "block";
}
function mouseOut() {
  document.getElementById("affirm").style.display = "none";
  document.getElementById("neutral").style.display = "block";
  document.getElementById("response1").style.display = "none";
}
