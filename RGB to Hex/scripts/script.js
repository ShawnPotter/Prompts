/*
 * Shawn Potter
 * 12/15/2018
 * script.js
 * RGB to hex code converter
*/

//Define Globals
var red = "";
var green = "";
var blue = "";
var output = "";

function setDefaults(){
   document.getElementById("decRed").defaultValue="0";
   document.getElementById("decGreen").defaultValue="0";
   document.getElementById("decBlue").defaultValue="0";
}

setDefaults();

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

$("#submit").on("click", function(){
   getColors();
   convert(red, green, blue);
   document.getElementById("codeOutput").innerHTML = "<p>"+output+"</p>";
   document.getElementById("colorOutput").style.backgroundColor = output;
});