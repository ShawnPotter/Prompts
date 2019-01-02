/*
 * Shawn Potter
 * 12/29/2018
 * math.js
 * This script file holds the nessecary math required to perform calculations
 */
var totalYield = 0.0;
var moduleYield = 0;

function getOutput(mining,astrogeology,frigate,barge,expedition,exhumer,ship,module,ore){
    getModYield(module);
    getSkillBonus(moduleYield, mining, astrogeology, frigate, barge, expedition, exhumer, ship);
}

function getSkillBonus(moduleYield, mining,astrogeology,frigate,barge,expedition,exhumer,ship){
    if(ship=="venture"){
        var roleBonus = 2;
        var miningBonus = 1 + (0.05 * mining);
        var astrogeologyBonus = 1 + (0.05 * astrogeology);
        var frigateBonus = 1 + (0.05 * frigate);
        totalYield = moduleYield *
                     roleBonus *
                     miningBonus *
                     astrogeologyBonus *
                     frigateBonus;
        console.log("totalYield="+totalYield.toFixed(2)); //debug
        totalYield = totalYield.toFixed(2);
        return totalYield;
    }
}
function getModYield(module){
    if(module=="miner1"){
        moduleYield = 40;
        return moduleYield;
    }
}