function kopier() {
  let a = document.getElementById("inp1").value;
  let b = document.getElementById("inp2").value;
  let c = document.getElementById("inp3").value;
  let d = document.getElementById("inp4").value;
  let e = document.getElementById("inp5").value;
  let f = document.getElementById("inp6").value;
  let kilde =
    a + " (" + b + ") " + c + ". Hentet " + d + " fra " + e + ": " + "\n" + f;
  navigator.clipboard.writeText(kilde);
  alert("Du kopierte " + "\n" + kilde);
  document.getElementById("resultat").innerHTML = kilde;
}
window.addEventListener("keydown", enter, false);

function enter(key) {
  if (key.keyCode == "13") {
    kopier();
  }
}
