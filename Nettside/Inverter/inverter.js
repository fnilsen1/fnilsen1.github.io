function invert() {
  var text = document.getElementById("input").value + " ";
  text = text.replace(/R /g, "'R ");
  text = text.replace(/R'/g, "R");
  text = text.replace(/L /g, "'L ");
  text = text.replace(/L'/g, "L");
  text = text.replace(/U /g, "'U ");
  text = text.replace(/U'/g, "U");
  text = text.replace(/D /g, "'D ");
  text = text.replace(/D'/g, "D");
  text = text.replace(/F /g, "'F ");
  text = text.replace(/F'/g, "F");
  text = text.replace(/B /g, "'B ");
  text = text.replace(/B'/g, "B");
  text = text.replace(/B2 /g, "2B ");
  text = text.replace(/F2 /g, "2F ");
  text = text.replace(/R2 /g, "2R ");
  text = text.replace(/L2 /g, "2L ");
  text = text.replace(/U2 /g, "2U ");
  text = text.replace(/D2 /g, "2D ");
  text = text.split("").reverse().join("");

  var resultat = document.getElementById("resultat");
  resultat.innerHTML = text;
}
