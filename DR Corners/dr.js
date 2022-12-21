let all_algs = [
  "F2 R2",
  "R2 U R2",
  "F2 R2 F2",
  "F2 U2 R2",
  "F2 U' F2 R2",
  "R2 U' R2 U R2 ",
  "R2 U R2 U R2",
  "U R2 U2 F2 U' R2",
  "R2 U F2 U2 R2",
  "F2 U' F2 U F2 R2 ",
  "F2 R2 U R2 U F2 ",
  "R2 U y R2 U' R2 U R2",
  "R2 U' R2 U2 F2 U' R2",
  "y' R2 U' R2 U R2 U2 B2 ",
  "U R2 U2 F2 U' F2 U F2",
  "U R2 U' R2 U R2 U' R2",
  "y' U2 R2 U B2 U2 R2 U R2",
  "R2 U F2 U2 R2 U' F2",
  "F2 U R2 U2 F2 U' R2",
  "F2 U2 R2 U' R2 U2 F2",
  "U F2 U F2 U' F2 R2 U' F2",
  "F2 R2 U' F2 U R2 U' R2",
  "F2 U R2 U2 F2 U F2 U' R2",
  "F2 U R2 U R2 U2 F2 U' R2",
  "U R2 U R2 U2 F2 U' F2 U F2",
  "F2 U F2 U2 R2 U' R2 U2 F2",
  "F2 U2 R2 U R2 U2 F2 U' F2",
];

let mirrors = [
  "F2 L2",
  "L2 U' L2",
  "F2 L2 F2",
  "F2 U2 L2",
  "F2 U F2 L2",
  "L2 U L2 U' L2",
  "L2 U' L2 U' L2",
  "U' L2 U2 F2 U L2",
  "L2 U' F2 U2 L2",
  "F2 U F2 U' F2 L2",
  "F2 L2 U' L2 U' F2",
  "L2 U' y' L2 U L2 U' L2",
  "L2 U L2 U2 F2 U L2",
  "y L2 U L2 U' L2 U2 B2",
  "U' L2 U2 F2 U F2 U' F2",
  "U' L2 U L2 U' L2 U L2",
  "y U2 L2 U' B2 U2 L2 U' L2",
  "L2 U' F2 U2 L2 U F2",
  "F2 U' L2 U2 F2 U L2",
  "F2 U2 L2 U L2 U2 F2",
  "U' F2 U' F2 U F2 L2 U F2",
  "F2 L2 U F2 U' L2 U L2",
  "F2 U' L2 U2 F2 U' F2 U L2",
  "F2 U' L2 U' L2 U2 F2 U L2",
  "U' L2 U' L2 U2 F2 U F2 U' F2",
  "F2 U' F2 U2 L2 U L2 U2 F2",
  "F2 U2 L2 U' L2 U2 F2 U F2",
];

let combined = [
  "F2 R2",
  "R2 U R2",
  "F2 R2 F2",
  "F2 U2 R2",
  "F2 U' F2 R2",
  "R2 U' R2 U R2 ",
  "R2 U R2 U R2",
  "U R2 U2 F2 U' R2",
  "R2 U F2 U2 R2",
  "F2 U' F2 U F2 R2 ",
  "F2 R2 U R2 U F2 ",
  "R2 U y R2 U' R2 U R2",
  "R2 U' R2 U2 F2 U' R2",
  "y' R2 U' R2 U R2 U2 B2 ",
  "U R2 U2 F2 U' F2 U F2",
  "U R2 U' R2 U R2 U' R2",
  "y' U2 R2 U B2 U2 R2 U R2",
  "R2 U F2 U2 R2 U' F2",
  "F2 U R2 U2 F2 U' R2",
  "F2 U2 R2 U' R2 U2 F2",
  "U F2 U F2 U' F2 R2 U' F2",
  "F2 R2 U' F2 U R2 U' R2",
  "F2 U R2 U2 F2 U F2 U' R2",
  "F2 U R2 U R2 U2 F2 U' R2",
  "U R2 U R2 U2 F2 U' F2 U F2",
  "F2 U F2 U2 R2 U' R2 U2 F2",
  "F2 U2 R2 U R2 U2 F2 U' F2",
  "F2 L2",
  "L2 U' L2",
  "F2 L2 F2",
  "F2 U2 L2",
  "F2 U F2 L2",
  "L2 U L2 U' L2",
  "L2 U' L2 U' L2",
  "U' L2 U2 F2 U L2",
  "L2 U' F2 U2 L2",
  "F2 U F2 U' F2 L2",
  "F2 L2 U' L2 U' F2",
  "L2 U' y' L2 U L2 U' L2",
  "L2 U L2 U2 F2 U L2",
  "y L2 U L2 U' L2 U2 B2",
  "U' L2 U2 F2 U F2 U' F2",
  "U' L2 U L2 U' L2 U L2",
  "y U2 L2 U' B2 U2 L2 U' L2",
  "L2 U' F2 U2 L2 U F2",
  "F2 U' L2 U2 F2 U L2",
  "F2 U2 L2 U L2 U2 F2",
  "U' F2 U' F2 U F2 L2 U F2",
  "F2 L2 U F2 U' L2 U L2",
  "F2 U' L2 U2 F2 U' F2 U L2",
  "F2 U' L2 U' L2 U2 F2 U L2",
  "U' L2 U' L2 U2 F2 U F2 U' F2",
  "F2 U' F2 U2 L2 U L2 U2 F2",
  "F2 U2 L2 U' L2 U2 F2 U F2",
];

let ultra_combined = {
  0: all_algs,
  1: mirrors,
  2: combined,
};

let righty_scrambles = [
  "R2 U2 R2 U2 F2 U2 R2 U2",
  "R2 U R2 U2 F2 U2 R2 U2 F2 R2",
  "U2 F2 U2 R2 U2 F2 U2 R2 F2 R2 F2",
  "U2 F2 U2 R2 U2",
  "R2 F2 U' F2 U2 R2 U2 F2 U2 R2 F2",
  "R2 U' R2 U' F2 U2 R2 U2 F2 U2",
  "R2 U' R2 U F2 U2 R2 U2 F2 U2",
  "R2 U F2 U2 R2 U' R2 U2 F2 U2 R2 U2 F2 U2",
  "R2 U2 F2 U F2 U2 R2 U2 F2 U2",
  "R2 F2 U' F2 U' R2 U2 F2 U2 R2 U2",
  "F2 U' R2 U' R2 U2 R2 U2 F2 U2 R2 U2",
  "y' R2 B2 U R2 U' R2 U R2 B2 U2 F2 L2 B2 L2 F2 R2 U2",
  "R2 U F2 U2 R2 U R2",
  "y R2 U2 F2 U' F2 U F2",
  "L2 B2 U B2 D F2 U2 R2 U' R2 U2 L2 U2 F2 U2 B2 R2 D2 L2 F2",
  "R2 U R2 U' R2 U R2 U'",
  "y F2 U' F2 U2 R2 U' F2 U2",
  "F2 U' F2 U2 R2 U' R2 U2 F2 U2 R2 U2 F2 R2",
  "R2 U F2 U2 R2 U' F2",
  "F2 U2 R2 U R2 U2 F2",
  "F2 U F2 U' R2 U R2 U R2 U2 R2 F2 R2 F2 R2 F2 U2 F2 R2",
  "L2 U F2 D' R2 U' R2 U2 L2 F2 L2 R2 D2 F2 U2",
  "R2 U F2 U' F2 U2 R2 U' F2",
  "R2 U' R2 U2 F2 U R2 U R2 U2 F2 U2 R2 U2",
  "F2 U' F2 U F2 U2 R2 U' R2 U'",
  "F2 U2 R2 U' F2 U2 R2 U' R2 U2 F2 U2 R2 U2",
  "F2 U F2 U2 R2 U' R2 U2 F2",
];

let lefty_scrambles = [
  "L2 D2 L2 U2 B2 D2 R2 U2",
  "L2 U' L2 D2 B2 U2 R2 D2 F2 L2",
  "U2 F2 U2 R2 U2 F2 U2 R2 F2 L2 F2",
  "D2 B2 U2 R2 D2",
  "L2 F2 U B2 U2 R2 D2 F2 D2 R2 F2",
  "L2 U L2 U' D2 B2 U2 R2 D2 F2 U2",
  "L2 U L2 U' B2 D2 R2 U2 F2 D2",
  "R2 D B2 D2 R2 U' F2 R2 U2 L2 F2 D2 R2 B2 R2 B2 U2",
  "L2 U2 F2 U' F2 D2 R2 D2 F2 U2",
  "L2 F2 U F2 U' F2",
  "F2 U L2 U L2 F2",
  "y L2 B2 U' L2 U L2 U' R2 F2 D2 F2 L2 F2 L2 F2 R2 U2",
  "R2 D B2 D2 R2 U L2 U2 L2 F2 L2 R2 D2 B2 R2 U2",
  "y' L2 U2 F2 U F2 U' F2",
  "R2 B2 U' B2 D' F2 D2 R2 U R2 U2 L2 U2 B2 U2 F2 R2 U2 R2 F2",
  "R2 D' L2 U B2 U' F2 R2 U R2 F2 L2 F2 U2 R2 U2 F2 D2 R2",
  "y' F2 U F2 D2 R2 U B2 L2 D2 U2 R2 U2",
  "F2 U F2 D2 R2 U L2 U2 B2 D2 R2 U2 F2 L2",
  "R2 D B2 D2 R2 U R2 U2 R2 B2 D2 F2 L2 D2 L2 U2 B2",
  "F2 D2 R2 U' R2 D2 F2",
  "F2 U' F2 U L2 U' L2 U' L2 U2 R2 F2 R2 B2 R2 F2 D2 B2 R2",
  "R2 D' L2 U R2 U R2 F2 D2 R2 B2 D2 B2 U2 F2 L2 R2",
  "L2 U' F2 U F2 D2 R2 U B2 L2 D2 U2 R2",
  "L2 U L2 D2 B2 U' R2 U' L2 D2 F2 U2 R2 U2",
  "R2 U L2 U F2 U' B2 D R2 U' R2 U' F2 U2 L2 F2 R2 F2 D2 R2 F2",
  "F2 U2 R2 U' F2 U2 R2 U' R2 U2 R2 U2 F2 R2 F2 D2 L2 D2 L2 U2",
  "F2 U' F2 D2 R2 U R2 D2 F2",
];

let combined_scrambles = [
  "R2 U2 R2 U2 F2 U2 R2 U2",
  "R2 U R2 U2 F2 U2 R2 U2 F2 R2",
  "U2 F2 U2 R2 U2 F2 U2 R2 F2 R2 F2",
  "U2 F2 U2 R2 U2",
  "R2 F2 U' F2 U2 R2 U2 F2 U2 R2 F2",
  "R2 U' R2 U' F2 U2 R2 U2 F2 U2",
  "R2 U' R2 U F2 U2 R2 U2 F2 U2",
  "R2 U F2 U2 R2 U' R2 U2 F2 U2 R2 U2 F2 U2",
  "R2 U2 F2 U F2 U2 R2 U2 F2 U2",
  "R2 F2 U' F2 U' R2 U2 F2 U2 R2 U2",
  "F2 U' R2 U' R2 U2 R2 U2 F2 U2 R2 U2",
  "y' R2 B2 U R2 U' R2 U R2 B2 U2 F2 L2 B2 L2 F2 R2 U2",
  "R2 U F2 U2 R2 U R2",
  "y R2 U2 F2 U' F2 U F2",
  "L2 B2 U B2 D F2 U2 R2 U' R2 U2 L2 U2 F2 U2 B2 R2 D2 L2 F2",
  "R2 U R2 U' R2 U R2 U'",
  "y F2 U' F2 U2 R2 U' F2 U2",
  "F2 U' F2 U2 R2 U' R2 U2 F2 U2 R2 U2 F2 R2",
  "R2 U F2 U2 R2 U' F2",
  "F2 U2 R2 U R2 U2 F2",
  "F2 U F2 U' R2 U R2 U R2 U2 R2 F2 R2 F2 R2 F2 U2 F2 R2",
  "L2 U F2 D' R2 U' R2 U2 L2 F2 L2 R2 D2 F2 U2",
  "R2 U F2 U' F2 U2 R2 U' F2",
  "R2 U' R2 U2 F2 U R2 U R2 U2 F2 U2 R2 U2",
  "F2 U' F2 U F2 U2 R2 U' R2 U'",
  "F2 U2 R2 U' F2 U2 R2 U' R2 U2 F2 U2 R2 U2",
  "F2 U F2 U2 R2 U' R2 U2 F2",
  "L2 D2 L2 U2 B2 D2 R2 U2",
  "L2 U' L2 D2 B2 U2 R2 D2 F2 L2",
  "U2 F2 U2 R2 U2 F2 U2 R2 F2 L2 F2",
  "D2 B2 U2 R2 D2",
  "L2 F2 U B2 U2 R2 D2 F2 D2 R2 F2",
  "L2 U L2 U' D2 B2 U2 R2 D2 F2 U2",
  "L2 U L2 U' B2 D2 R2 U2 F2 D2",
  "R2 D B2 D2 R2 U' F2 R2 U2 L2 F2 D2 R2 B2 R2 B2 U2",
  "L2 U2 F2 U' F2 D2 R2 D2 F2 U2",
  "L2 F2 U F2 U' F2",
  "F2 U L2 U L2 F2",
  "y L2 B2 U' L2 U L2 U' R2 F2 D2 F2 L2 F2 L2 F2 R2 U2",
  "R2 D B2 D2 R2 U L2 U2 L2 F2 L2 R2 D2 B2 R2 U2",
  "y' L2 U2 F2 U F2 U' F2",
  "R2 B2 U' B2 D' F2 D2 R2 U R2 U2 L2 U2 B2 U2 F2 R2 U2 R2 F2",
  "R2 D' L2 U B2 U' F2 R2 U R2 F2 L2 F2 U2 R2 U2 F2 D2 R2",
  "y' F2 U F2 D2 R2 U B2 L2 D2 U2 R2 U2",
  "F2 U F2 D2 R2 U L2 U2 B2 D2 R2 U2 F2 L2",
  "R2 D B2 D2 R2 U R2 U2 R2 B2 D2 F2 L2 D2 L2 U2 B2",
  "F2 D2 R2 U' R2 D2 F2",
  "F2 U' F2 U L2 U' L2 U' L2 U2 R2 F2 R2 B2 R2 F2 D2 B2 R2",
  "R2 D' L2 U R2 U R2 F2 D2 R2 B2 D2 B2 U2 F2 L2 R2",
  "L2 U' F2 U F2 D2 R2 U B2 L2 D2 U2 R2",
  "L2 U L2 D2 B2 U' R2 U' L2 D2 F2 U2 R2 U2",
  "R2 U L2 U F2 U' B2 D R2 U' R2 U' F2 U2 L2 F2 R2 F2 D2 R2 F2",
  "F2 U2 R2 U' F2 U2 R2 U' R2 U2 R2 U2 F2 R2 F2 D2 L2 D2 L2 U2",
  "F2 U' F2 D2 R2 U R2 D2 F2",
];

let ultra_combined_scrambles = {
  0: righty_scrambles,
  1: lefty_scrambles,
  2: combined_scrambles,
};

let index;
let select;

function next_alg() {
  document.getElementById("solution").innerHTML = "Solution";
  select = document.getElementById("select").value;

  index = Math.floor(Math.random() * ultra_combined_scrambles[select].length);
  let scramble = ultra_combined_scrambles[select][index];
  document.getElementById("scramble").innerHTML = scramble;
  document.getElementById("einar_cube").setAttribute("scramble", scramble);
}

function display_solution() {
  console.log(select);
  console.log(index);

  let solution = ultra_combined[select][index];
  document.getElementById("solution").innerHTML = solution;
}

window.addEventListener("keydown", space, false);

function space(key) {
  if (key.keyCode == "32") {
    display_solution();
  }
}

window.addEventListener("keydown", right, false);

function right(key) {
  if (key.keyCode == "39") {
    next_alg();
  }
}

next_alg();
