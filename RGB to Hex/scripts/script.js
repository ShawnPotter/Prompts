/*
 * Shawn Potter
 * 12/15/2018
 * script.js
 * RGB to hex code converter
 * TODO:
 * - nothing
*/

//default values for input fields
function setDefaults(){
   document.getElementById("decRed").defaultValue="0";
   document.getElementById("decGreen").defaultValue="0";
   document.getElementById("decBlue").defaultValue="0";
}
//set the defaults
setDefaults();

//when submit button on RGB to Hex is pressed
$("#submitRgb").on("click", function(){
   var red = "";
   var green = "";
   var blue = "";
   var output = "";
   
   function getColors(){
      red = parseInt(document.getElementById("decRed").value);
      green = parseInt(document.getElementById("decGreen").value);
      blue = parseInt(document.getElementById("decBlue").value);
      //console.log("rgb("+red+","+green+","+blue+")"); //debug
      
      return red, green, blue;
   }
  //convert rgb to a hex code
  function convert(red, green, blue){
      output="";
      colors = [red, green, blue];
      for(var i = 0; i <= 2; i++){
        foo = colors[i].toString(16);
        //console.log("foo="+foo);
        if(foo.length % 2){
           foo = "0"+foo;
        }
        output += foo;
      }
      output = "#" + output;
      return output;
   }
   //get rgb color values
   getColors();
   //convert rgb to hex
   convert(red, green, blue);
   
   //set the hex code output to new value
   document.getElementById("codeOutput").setAttribute("value", output);
   
   //set the color preview box to new color
   document.getElementById("colorOutput").style.backgroundColor = output;
});

//submit button for Hex to RGB converter
$("#submitHex").on("click", function(){
   var hexCode = document.getElementById("hexInput").value;
   var red = "";
   var green = "";
   var blue = "";
   
   //segment the hex code into three pieces and then convert to decimal
   function getRgb(){
      for(var i=0; i<=5; i++){
         if(i<2){
            red += hexCode[i];
            //console.log(red); //debug
         } else if(i<4){
            green += hexCode[i];
         } else{
            blue += hexCode[i];
         }
      }
      red = parseInt(red, 16);
      green = parseInt(green, 16);
      blue = parseInt(blue, 16);
      //console.log("rgb("+red+","+green+","+blue+")"); //debug
   }
   //set values for the input boxes
   function setRgb(){
      document.getElementById("hexRed").setAttribute("value", red);
      document.getElementById("hexGreen").setAttribute("value", green);
      document.getElementById("hexBlue").setAttribute("value", blue);
      document.getElementById("colorOutput2").style.backgroundColor = "rgb("+red+","+green+","+blue+")";
   }
   
   //run functions
   getRgb();
   setRgb();
});