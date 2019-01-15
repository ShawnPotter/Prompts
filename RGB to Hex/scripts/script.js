/*
 * Shawn Potter
 * 12/15/2018
 * script.js
 * RGB to hex code converter
 * TODO:
 *   - Create Hex to RGB converter
*/

function setDefaults(){
   document.getElementById("decRed").defaultValue="0";
   document.getElementById("decGreen").defaultValue="0";
   document.getElementById("decBlue").defaultValue="0";
}

setDefaults();

$("#submitRgb").on("click", function(){
   var red = "";
   var green = "";
   var blue = "";
   var output = "";
   
   function getColors(){
      red = parseInt(document.getElementById("decRed").value);
      green = parseInt(document.getElementById("decGreen").value);
      blue = parseInt(document.getElementById("decBlue").value);
      console.log("rgb("+red+","+green+","+blue+")"); //debug
      
      return red, green, blue;
   }
  
  function convert(red, green, blue){
      output="";
      colors = [red, green, blue];
      for(var i = 0; i <= 2; i++){
        foo = colors[i].toString(16);
        console.log("foo="+foo);
        if(foo.length % 2){
           foo = "0"+foo;
        }
        output += foo;
      }
      output = "#" + output;
      return output;
   }
   
   getColors();
   convert(red, green, blue);
   document.getElementById("codeOutput").setAttribute("value", output);
   document.getElementById("colorOutput").style.backgroundColor = output;
});

$("#submitHex").on("click", function(){
   var hexCode = document.getElementById("hexInput").value;
   var red = "";
   var green = "";
   var blue = "";
   function getRgb(){
      for(var i=0; i<=5; i++){
         if(i<2){
            red += hexCode[i];
            console.log(red);
         } else if(i<4){
            green += hexCode[i];
         } else{
            blue += hexCode[i];
         }
      }
      red = parseInt(red, 16);
      green = parseInt(green, 16);
      blue = parseInt(blue, 16);
      console.log("rgb("+red+","+green+","+blue+")"); //debug
   }
   function setRgb(){
      document.getElementById("hexRed").setAttribute("value", red);
      document.getElementById("hexGreen").setAttribute("value", green);
      document.getElementById("hexBlue").setAttribute("value", blue);
      document.getElementById("colorOutput2").style.backgroundColor = "rgb("+red+","+green+","+blue+")";
   }
   getRgb();
   setRgb();
});