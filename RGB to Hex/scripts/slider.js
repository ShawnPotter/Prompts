/*
 * Shawn Potter
 * 1/26/2019
 * slider.js
 * color picker with sliders
 * TODO:
 *   - Add color hex code output for color picker
 *   - Add functionality for RGB input boxes to update sliders
*/
$(document).ready(function(){
    //create event listeners for all three sliders
    document.getElementById("redSlider").addEventListener("input", updateRed);
    document.getElementById("greenSlider").addEventListener("input", updateGreen);
    document.getElementById("blueSlider").addEventListener("input", updateBlue);
    
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
     function updateColor(){
        var red = document.getElementById("redSlider").value;
        var green = document.getElementById("greenSlider").value;
        var blue = document.getElementById("blueSlider").value;
        document.getElementById("colorOutput3").style.backgroundColor = "rgb("+red+","+green+","+blue+")";
     }
});