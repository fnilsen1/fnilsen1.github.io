



async function getAksje(){
const api_url = 'https://api.twelvedata.com/time_series?apikey=54d0fe24f62d4bd1af7b7e8af88e17b7&interval=1min&symbol=BTC/USD&outputsize=1';
const response = await fetch(api_url);
const data = await response.json();
console.log(data);
var bitcoin = (data.values[0].open);

document.getElementById("bitc").textContent=Math.floor(bitcoin)+" USD";
console.log("hey");
getethereum()
ticker()
}

async function getethereum(){
    const ethereum = 'https://api.twelvedata.com/time_series?apikey=54d0fe24f62d4bd1af7b7e8af88e17b7&interval=1min&symbol=ETH/USD&outputsize=1';
    const response = await fetch(ethereum);
    const data = await response.json();

    var bitcoin = parseFloat(data.values[0].open);
   
    document.getElementById("ether").textContent=Math.floor(bitcoin)+" USD";

    }
   
async function ticker(){
    var input = document.getElementById("inntast").value;   
const ticker = 'https://api.twelvedata.com/time_series?apikey=54d0fe24f62d4bd1af7b7e8af88e17b7&interval=1min&symbol='+input+'&outputsize=1';
console.log(ticker);
const response = await fetch(ticker);
const data = await response.json();

var bitcoin = (data.meta.symbol);




console.log(data);
document.getElementById("resultat").innerHTML=bitcoin;
document.getElementById("resultat").innerHTML+= " "+data.meta.interval;
document.getElementById("resultat").innerHTML+= " "+data.meta.currency;
document.getElementById("resultat").innerHTML+= " "+data.meta.exchange_timezone;
document.getElementById("resultat").innerHTML+= " "+data.meta.exchange;

document.getElementById("resultat").innerHTML+= '<br></br>';
document.getElementById("resultat").innerHTML+= data.values[0].open + " USD";
}

function interval(){
setInterval(getAksje, 30000);
}

window.addEventListener("keydown", enter, false);

function enter(key){
if(key.keyCode == "13"){
getAksje()
}
}


getAksje();
getethereum()

