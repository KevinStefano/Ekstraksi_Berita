const spawn = require("child_process").spawn;

const process = spawn("python",["./regex.py"]);
var idx = 0;
var j = 0;
playfoto();
var person = prompt("Please enter your name", "Harry Potter");
document.getElementById("click").onclick = function() {mainFunction()}

function mainFunction() {
    //DO inputFOLDER()
}

function inputFolder() {
    document.getElementById("folder").value
}

function inputKeyword() {
    document.getElementById("keyword").value
}

function inputAlgo() {
    document.getElementById("algo").value
}

function playfoto() {
    var i;
    var slide = document.getElementsByClassName("foto");
    for (i = 0; i <= slide.length-1; i++) {
        slide[i].style.display = "none";
    }
    idx=(idx%2+1);
    slide[idx-1].style.display = "flex";
    setTimeout(playfoto, 2000);

}
