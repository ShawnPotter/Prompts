/*
 * Shawn Potter
 * 12/11/2018
 * script.js
 * Get month, day and year information and then return the day of the week to the user
 */

//array of months
var monthsList = ["January","February","March","April","May","June",
                  "July","August","September","October","November",
                  "December"];
var daysList = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

//get the current date so that the select boxes can be set to curren date
var today = new Date();
var monthNow = today.getMonth();
var dayNow = today.getDate();
var yearNow = today.getFullYear();

//create vars to assign values to when submit button is hit
var month;
var day;
var year;

/*
 * following three functions add all the options to the
 * select fields decreasing the size of the HTML document.
*/
//add month options to the month select
function addMonths(){
    for(var i = 0; i <= monthsList.length-1;i++){
        $("#month").append("<option value='"+i+"'>" + monthsList[i] + "</option>");
    }
    $("#month").val(monthNow);
    console.log("added months");
}

//add day options to the day select
function addDays(){
    for(var i = 1; i <= 31; i++){
        $("#day").append("<option>" + i + "</option>");
    }
    $("#day").val(dayNow);
    console.log("added days");
}

//add years to the year select
function addYears(){
    for(var i = 1901; i <= 2020; i++){
        $("#year").append("<option>" + i + "</option>");
    }
    $("#year").val(yearNow);
    console.log("added years");
}

//add all options to select fields
$(document).ready(function(){
    addMonths();
    addDays();
    addYears();
});


//get values of select fields and then get the day of the week
$("#submit").on("click", function(){
    console.log("button clicked");
    //pull values
    month = document.getElementById("month").value;
    day = document.getElementById("day").value;
    year = document.getElementById("year").value;
    
    //make sure right values are pulled
    console.log("Month:" + month + " Day:" + day + " Year:" + year);
    
    //create a date variable to pull a day from
    var tempDate = new Date();
    tempDate.setMonth(month);
    tempDate.setDate(day-1);
    tempDate.setFullYear(year);
    
    $("#output").html("<p>" + daysList[tempDate.getDay()] + "</p>");
});