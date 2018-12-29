/*
 * Shawn Potter
 * 12/29/2018
 * script.js
 */

//set globals
var submit = document.getElementById("submit");
var miningSkill = 0;
var astrogeologySkill = 0;
var miningFrigateSkill = 0;
var miningBargeSkill = 0;
var expeditionFrigateSkill = 0;
var exhumerSkill = 0;
var ship = "";
var module = "";
var ore = "";

//button executes getData
submit.onclick = getData;

//getData executes four getters
function getData(){
    getSkills();
    getShip();
    getModule();
    getOre();
    
    //debug
    console.log("miningSkill="+ miningSkill +
                ", astrogeologySkill="+ astrogeologySkill +
                ", miningFrigateSkill="+ miningFrigateSkill +
                ", miningBargeSkill="+ miningBargeSkill +
                ", expeditionFrigateSkill="+ expeditionFrigateSkill +
                ", exhumerSkill"+ exhumerSkill +
                ", ship="+ ship +
                ", module="+ module +
                ", ore="+ ore);
}

//get skills
function getSkills(){
    miningSkill = document.getElementById("mining").value;
    astrogeologySkill = document.getElementById("astrogeology").value;
    miningFrigateSkill = document.getElementById("miningFrigate").value;
    expeditionFrigateSkill = document.getElementById("expeditionFrigate").value;
    miningBargeSkill = document.getElementById("miningBarge").value;
    exhumerSkill = document.getElementById("exhumer").value;
    return miningSkill, astrogeologySkill,
            miningFrigateSkill, expeditionFrigateSkill,
            miningBargeSkill, exhumerSkill;
}

//get ship
function getShip(){
    ship = document.getElementById("ship").value;
    return ship;
}

//get module
function getModule(){
    module = document.getElementById("module").value;
    return module;
}

//get ore
function getOre(){
    ore = document.getElementById("ore").value;
    return ore;
}
