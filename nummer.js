var elementName =[
    "Hydrogen","Helium","Litium","Beryllium","Bor","Karbon","Nitrogen","Oksygen","Fluor","Neon","Natrium","Magnesium","Aluminium","Silisium","Fosfor","Svovel","Klor","Argon","Kalium","Kalsium","Scandium","Titan","Vanadium","Krom","Mangan","Jern","Kobalt","Nikkel","Kobber","Sink","Gallium","Germanium","Arsen","Selen","Brom","Krypton","Rubidium","Strontium","Yttrium","Zirkonium","Niob","Molybden","Technetium","Ruthenium","Rhodium","Palladium","Sølv","Kadmium","Indium","Tinn","Antimon","Tellur","Jod","Xenon","Cesium","Barium","Lantan","Cerium","Praseodym","Neodym","Promethium","Samarium","Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutetium","Hafnium","Tantal","Wolfram","Rhenium","Osmium","Iridium","Platina","Gull","Kvikksølv","Thallium","Bly","Vismut","Polonium","Astat","Radon","Francium","Radium","Actinium","Thorium","Protactinium","Uran","Neptunium","Plutonium","Americium","Curium","Berkelium","Californium","Einsteinium","Fermium","Mendelevium","Nobelium","Lawrencium","Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium", "Darmstadtium", "Røntgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tenness", "Oganesson"
]; 

var elementSymbol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118 
]; 

var riktig = -1
var grunnstoff = elementName[0|(Math.random()*elementName.length)]
var grunnstoff_input = ""
var svar = "Det stemmer"

window.addEventListener("keydown", enter, false);

function enter(key){
if(key.keyCode == "13"){
sjekk_grunnstoff()
}
}

window.addEventListener("keydown", periodesystem, false);

function periodesystem(key){
if(key.keyCode == "38"){
periodesystem1()
}
}

window.addEventListener("keydown", skip, false);

function skip(key){
if(key.keyCode == "39"){
skip_grunnstoff()
}
}


function sjekk_grunnstoff(){
   
// var grunnstoff_input = document.getElementById("inntasting").value
// console.log(grunnstoff_input)
grunnstoff_input =document.getElementById("inntasting").value-1
console.log(grunnstoff_input)
console.log(elementName.indexOf(grunnstoff))
 if(grunnstoff_input == elementName.indexOf(grunnstoff)){
    document.getElementById("resultat").innerText=svar
    document.getElementById("feil").innerText=""
    setTimeout(function(){
        nytt_grunnstoff() 

    },1000)
       
   
    
 } else {
     document.getElementById("feil").innerText="Det er feil!"
 }


}

function nytt_grunnstoff(){
// var grunnstoff = elementName[0|(Math.random()*elementName.length)]
// console.log(grunnstoff)
document.getElementById("feil").innerText=""
document.getElementById("resultat").innerText=""
document.getElementById("inntasting").value = ""
grunnstoff = elementName[0|(Math.random()*elementName.length)]
document.getElementById("grunnstoff_Navn").innerText=grunnstoff
document.getElementById("korrekt").innerText=riktig+=1

}

function skip_grunnstoff(){
    document.getElementById("feil").innerText=""
document.getElementById("inntasting").value = ""
grunnstoff = elementName[0|(Math.random()*elementName.length)]
document.getElementById("grunnstoff_Navn").innerText=grunnstoff
}


var periodesystemViz = false
function periodesystem1() {
    var img = document.getElementById("periodesystem");
    console.log(img)
    if (periodesystemViz === false) {
        img.style.visibility = "visible";
        periodesystemViz = true
    }
    else {
        img.style.visibility = "hidden"
        periodesystemViz = false
    }
}

nytt_grunnstoff()

