/*
 * Shawn Potter
 * 1/26/2019
 * slider.js
 * color picker with sliders
 * TODO:
 *   - Add color hex code output for color picker
 *   - Add functionality for RGB input boxes to update sliders
*/
//create event listeners for all three sliders
document.getElementById("redSlider").addEventListener("input", updateRed);
document.getElementById("greenSlider").addEventListener("input", updateGreen);
document.getElementById("blueSlider").addEventListener("input", updateBlue);
document.getElementById("alphaSlider").addEventListener("input", updateAlpha);

//functions to update input fields for RGB values
function updateRed(){
     var num = document.getElementById("redSlider").value;
     document.getElementById("redSliderNum").setAttribute("value", num);
     updateColor();
 }
 function updateGreen(){
     var num = document.getElementById("greenSlider").value;
     document.getElementById("greenSliderNum").setAttribute("value", num);
     updateColor();
 }
 function updateBlue(){
     var num = document.getElementById("blueSlider").value;
     document.getElementById("blueSliderNum").setAttribute("value", num);
     updateColor();
 }
 function updateAlpha(){
     var num = document.getElementById("alphaSlider").value;
       document.getElementById("alphaSliderNum").setAttribute("value", num);
       updateColor();
 }
 //function to update the color preview automatically when sliders are moved
 function updateColor(){
    var red = document.getElementById("redSlider").value;
    var green = document.getElementById("greenSlider").value;
    var blue = document.getElementById("blueSlider").value;
    var alpha = document.getElementById("alphaSlider").value;
    document.getElementById("colorOutput3").style.backgroundColor = "rgba("+red+","+green+","+blue+","+alpha+")";
 }