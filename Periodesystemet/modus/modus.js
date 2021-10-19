var elementName =[
    "Hydrogen","Helium","Litium","Beryllium","Bor","Karbon","Nitrogen","Oksygen","Fluor","Neon","Natrium","Magnesium","Aluminium","Silisium","Fosfor","Svovel","Klor","Argon","Kalium","Kalsium","Scandium","Titan","Vanadium","Krom","Mangan","Jern","Kobalt","Nikkel","Kobber","Sink","Gallium","Germanium","Arsen","Selen","Brom","Krypton","Rubidium","Strontium","Yttrium","Zirkonium","Niob","Molybden","Technetium","Ruthenium","Rhodium","Palladium","Sølv","Kadmium","Indium","Tinn","Antimon","Tellur","Jod","Xenon","Cesium","Barium","Lantan","Cerium","Praseodym","Neodym","Promethium","Samarium","Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutetium","Hafnium","Tantal","Wolfram","Rhenium","Osmium","Iridium","Platina","Gull","Kvikksølv","Thallium","Bly","Vismut","Polonium","Astat","Radon","Francium","Radium","Actinium","Thorium","Protactinium","Uran","Neptunium","Plutonium","Americium","Curium","Berkelium","Californium","Einsteinium","Fermium","Mendelevium","Nobelium","Lawrencium","Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium", "Darmstadtium", "Røntgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tenness", "Oganesson"
]; 

var elementSymbol = [
    "H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]; 

var riktig = -1
var grunnstoff = elementSymbol[0|(Math.random()*elementSymbol.length)]
var grunnstoff_input = ""
var svar = "Det stemmer"

window.addEventListener("keydown", enter, false);

function enter(key){
if(key.keyCode == "13"){
sjekk_grunnstoff()
}
}

window.addEventListener("keydown", skip, false);

function skip(key){
if(key.keyCode == "39"){
skip_grunnstoff()
}
}

window.addEventListener("keydown", periodesystem, false);

function periodesystem(key){
if(key.keyCode == "38"){
periodesystem1()
}
}


function sjekk_grunnstoff(){
   
// var grunnstoff_input = document.getElementById("inntasting").value
// console.log(grunnstoff_input)
grunnstoff_input =document.getElementById("inntasting").value

if(elementName.indexOf(grunnstoff_input) === elementSymbol.indexOf(grunnstoff)){
    document.getElementById("resultat").innerText=svar
    document.getElementById("feil").innerText=""
    setTimeout(function(){
        nytt_grunnstoff() 

    },1000)    
 }
    
  else {
    document.getElementById("feil").innerText="Det er feil!"
 }



}

function nytt_grunnstoff(){
document.getElementById("feil").innerText=""
document.getElementById("resultat").innerText=""
document.getElementById("inntasting").value = ""
grunnstoff = elementSymbol[0|(Math.random()*elementName.length)]
// console.log(grunnstoff)
document.getElementById("grunnstoff_Navn").innerText=grunnstoff
document.getElementById("korrekt").innerText=riktig+=1
}

function skip_grunnstoff(){
    document.getElementById("feil").innerText=""
document.getElementById("inntasting").value = ""
grunnstoff = elementSymbol[0|(Math.random()*elementName.length)]
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
