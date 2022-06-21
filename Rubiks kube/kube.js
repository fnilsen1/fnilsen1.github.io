let hvit = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"];
let oransje = ["🟧", "🟧", "🟧", "🟧", "🟧", "🟧", "🟧", "🟧", "🟧"];
let gronn = ["🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩"];
let rod = ["🟥", "🟥", "🟥", "🟥", "🟥", "🟥", "🟥", "🟥", "🟥"];
let bla = ["🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦"];
let gul = ["🟨", "🟨", "🟨", "🟨", "🟨", "🟨", "🟨", "🟨", "🟨"];
let scramble = [hvit, oransje, gronn, rod, bla, gul];

function R() {
  const UBR = hvit[2];
  const UR = hvit[5];
  const UFR = hvit[8];

  hvit[2] = gronn[2];
  hvit[5] = gronn[5];
  hvit[8] = gronn[8];

  gronn[2] = gul[2];
  gronn[5] = gul[5];
  console.log(gronn[5]);
  gronn[8] = gul[8];

  gul[2] = bla[6];
  gul[5] = bla[3];
  gul[8] = bla[0];

  bla[0] = UFR;
  bla[3] = UR;
  bla[6] = UBR;

  flate_med(rod);
}

function R_prime() {
  const UBR = hvit[2];
  const UR = hvit[5];
  const UFR = hvit[8];

  hvit[2] = bla[6];
  hvit[5] = bla[3];
  hvit[8] = bla[0];

  bla[0] = gul[8];
  bla[3] = gul[5];
  bla[6] = gul[2];

  gul[2] = gronn[2];
  gul[5] = gronn[5];
  gul[8] = gronn[8];

  gronn[2] = UBR;
  gronn[5] = UR;
  gronn[8] = UFR;

  flate_mot(rod);
}

function L_prime() {
  const UBL = hvit[0];
  const UL = hvit[3];
  const UFL = hvit[6];

  hvit[0] = gronn[0];
  hvit[3] = gronn[3];
  hvit[6] = gronn[6];

  gronn[0] = gul[0];
  gronn[3] = gul[3];
  gronn[6] = gul[6];

  gul[0] = bla[8];
  gul[3] = bla[5];
  gul[6] = bla[2];

  bla[2] = UFL;
  bla[5] = UL;
  bla[8] = UBL;
  flate_mot(oransje);
}

function L() {
  const UBL = hvit[0];
  const UL = hvit[3];
  const UFL = hvit[6];
  console.log(UBL, UL, UFL);

  hvit[0] = bla[8];
  hvit[3] = bla[5];
  hvit[6] = bla[2];

  bla[8] = gul[0];
  bla[5] = gul[3];
  bla[2] = gul[6];

  gul[0] = gronn[0];
  gul[3] = gronn[3];
  gul[6] = gronn[6];

  gronn[0] = UBL;
  gronn[3] = UL;
  gronn[6] = UFL;

  flate_med(oransje);
}

function U() {
  const FUL = gronn[0];
  const FU = gronn[1];
  const FUR = gronn[2];

  gronn[0] = rod[0];
  gronn[1] = rod[1];
  gronn[2] = rod[2];

  rod[0] = bla[0];
  rod[1] = bla[1];
  rod[2] = bla[2];

  bla[0] = oransje[0];
  bla[1] = oransje[1];
  bla[2] = oransje[2];

  oransje[0] = FUL;
  oransje[1] = FU;
  oransje[2] = FUR;

  flate_med(hvit);
}

function U_prime() {
  const FUL_prime = gronn[0];
  const FU_prime = gronn[1];
  const FUR_prime = gronn[2];

  gronn[0] = oransje[0];
  gronn[1] = oransje[1];
  gronn[2] = oransje[2];

  oransje[0] = bla[0];
  oransje[1] = bla[1];
  oransje[2] = bla[2];

  bla[0] = rod[0];
  bla[1] = rod[1];
  bla[2] = rod[2];

  rod[0] = FUL_prime;
  rod[1] = FU_prime;
  rod[2] = FUR_prime;

  flate_mot(hvit);
}

function D() {
  const FDL = gronn[6];
  const FD = gronn[7];
  const FDR = gronn[8];

  gronn[6] = oransje[6];
  gronn[7] = oransje[7];
  gronn[8] = oransje[8];

  oransje[6] = bla[6];
  oransje[7] = bla[7];
  oransje[8] = bla[8];

  bla[6] = rod[6];
  bla[7] = rod[7];
  bla[8] = rod[8];

  rod[6] = FDL;
  rod[7] = FD;
  rod[8] = FDR;

  flate_med(gul);
}

function D_prime() {
  const FDL_prime = gronn[6];
  const FD_prime = gronn[7];
  const FDR_prime = gronn[8];

  gronn[6] = rod[6];
  gronn[7] = rod[7];
  gronn[8] = rod[8];

  rod[6] = bla[6];
  rod[7] = bla[7];
  rod[8] = bla[8];

  bla[6] = oransje[6];
  bla[7] = oransje[7];
  bla[8] = oransje[8];

  oransje[6] = FDL_prime;
  oransje[7] = FD_prime;
  oransje[8] = FDR_prime;

  flate_mot(gul);
}

function F() {
  const UFL_F = hvit[6];
  const UF_F = hvit[7];
  const UFR_F = hvit[8];

  hvit[6] = oransje[8];
  hvit[7] = oransje[5];
  hvit[8] = oransje[2];

  oransje[8] = gul[2];
  oransje[5] = gul[1];
  oransje[2] = gul[0];

  gul[2] = rod[0];
  gul[1] = rod[3];
  gul[0] = rod[6];

  rod[0] = UFL_F;
  rod[3] = UF_F;
  rod[6] = UFR_F;

  flate_med(gronn);
}

function F_prime() {
  const UFL_F_prime = hvit[6];
  const UF_F_prime = hvit[7];
  const UFR_F_prime = hvit[8];

  hvit[6] = rod[0];
  hvit[7] = rod[3];
  hvit[8] = rod[6];

  rod[0] = gul[2];
  rod[3] = gul[1];
  rod[6] = gul[0];

  gul[2] = oransje[8];
  gul[1] = oransje[5];
  gul[0] = oransje[2];

  oransje[8] = UFL_F_prime;
  oransje[5] = UF_F_prime;
  oransje[2] = UFR_F_prime;

  flate_mot(gronn);
}

function B() {
  const UBL_B = hvit[0];
  const UB_B = hvit[1];
  const UBR_B = hvit[2];

  hvit[0] = rod[2];
  hvit[1] = rod[5];
  hvit[2] = rod[8];

  rod[2] = gul[8];
  rod[5] = gul[7];
  rod[8] = gul[6];

  gul[8] = oransje[6];
  gul[7] = oransje[3];
  gul[6] = oransje[0];

  oransje[6] = UBL_B;
  oransje[3] = UB_B;
  oransje[0] = UBR_B;

  flate_med(bla);
}

function B_prime() {
  const UBL_B_prime = hvit[0];
  const UB_B_prime = hvit[1];
  const UBR_B_prime = hvit[2];

  hvit[0] = oransje[6];
  hvit[1] = oransje[3];
  hvit[2] = oransje[0];

  oransje[6] = gul[8];
  oransje[3] = gul[7];
  oransje[0] = gul[6];

  gul[8] = rod[2];
  gul[7] = rod[5];
  gul[6] = rod[8];

  rod[2] = UBL_B_prime;
  rod[5] = UB_B_prime;
  rod[8] = UBR_B_prime;

  flate_mot(bla);
}

function flate_med(farge) {
  const forste = farge[1];
  farge[1] = farge[3];
  farge[3] = farge[7];
  farge[7] = farge[5];
  farge[5] = forste;

  const forste_hjorne = farge[0];
  farge[0] = farge[6];
  farge[6] = farge[8];
  farge[8] = farge[2];
  farge[2] = forste_hjorne;
}

function flate_mot(farge) {
  const forste_mot = farge[1];
  farge[1] = farge[5];
  farge[5] = farge[7];
  farge[7] = farge[3];
  farge[3] = forste_mot;

  const forste_hjorne_mot = farge[0];
  farge[0] = farge[2];
  farge[2] = farge[8];
  farge[8] = farge[6];
  farge[6] = forste_hjorne_mot;
}

window.addEventListener("keydown", klikk, false);

function klikk(key) {
  if (key.keyCode == "73") {
    R();
    update();
  }

  if (key.keyCode == "75") {
    R_prime();
    update();
  }

  if (key.keyCode == "68") {
    L();
    update();
  }

  if (key.keyCode == "69") {
    L_prime();
    update();
  }

  if (key.keyCode == "74") {
    U();
    update();
  }

  if (key.keyCode == "70") {
    U_prime();
    update();
  }

  if (key.keyCode == "83") {
    D();
    update();
  }

  if (key.keyCode == "76") {
    D_prime();
    update();
  }

  if (key.keyCode == "72") {
    F();
    update();
  }

  if (key.keyCode == "71") {
    F_prime();
    update();
  }

  if (key.keyCode == "87") {
    B();
    update();
  }

  if (key.keyCode == "79") {
    B_prime();
    update();
  }

  if (key.keyCode == "27") {
    hvit = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"];
    oransje = ["🟧", "🟧", "🟧", "🟧", "🟧", "🟧", "🟧", "🟧", "🟧"];
    gronn = ["🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩"];
    rod = ["🟥", "🟥", "🟥", "🟥", "🟥", "🟥", "🟥", "🟥", "🟥"];
    bla = ["🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦"];
    gul = ["🟨", "🟨", "🟨", "🟨", "🟨", "🟨", "🟨", "🟨", "🟨"];
    update();
  }
}

function update() {
  // console.log("");
  // console.log("         " + hvit[0], hvit[1], hvit[2]);
  // console.log("         " + hvit[3], hvit[4], hvit[5]);
  // console.log("         " + hvit[6], hvit[7], hvit[8]);
  // console.log(
  //   oransje[0],
  //   oransje[1],
  //   oransje[2],
  //   gronn[0],
  //   gronn[1],
  //   gronn[2],
  //   rod[0],
  //   rod[1],
  //   rod[2]
  // );
  // console.log(
  //   oransje[3],
  //   oransje[4],
  //   oransje[5],
  //   gronn[3],
  //   gronn[4],
  //   gronn[6],
  //   rod[3],
  //   rod[4],
  //   rod[5]
  // );
  // console.log(
  //   oransje[6],
  //   oransje[7],
  //   oransje[8],
  //   gronn[6],
  //   gronn[7],
  //   gronn[8],
  //   rod[6],
  //   rod[7],
  //   rod[8]
  // );
  // console.log("         " + gul[0], gul[1], gul[2]);
  // console.log("         " + gul[3], gul[4], gul[5]);
  // console.log("         " + gul[6], gul[7], gul[8]);

  document.getElementById("l1").innerHTML = hvit[0] + hvit[1] + hvit[2];
  document.getElementById("l2").innerHTML = hvit[3] + hvit[4] + hvit[5];
  document.getElementById("l3").innerHTML = hvit[6] + hvit[7] + hvit[8];
  document.getElementById("l4").innerHTML =
    oransje[0] +
    oransje[1] +
    oransje[2] +
    gronn[0] +
    gronn[1] +
    gronn[2] +
    rod[0] +
    rod[1] +
    rod[2] +
    bla[0] +
    bla[1] +
    bla[2];

  document.getElementById("l5").innerHTML =
    oransje[3] +
    oransje[4] +
    oransje[5] +
    gronn[3] +
    gronn[4] +
    gronn[5] +
    rod[3] +
    rod[4] +
    rod[5] +
    bla[3] +
    bla[4] +
    bla[5];

  document.getElementById("l6").innerHTML =
    oransje[6] +
    oransje[7] +
    oransje[8] +
    gronn[6] +
    gronn[7] +
    gronn[8] +
    rod[6] +
    rod[7] +
    rod[8] +
    bla[6] +
    bla[7] +
    bla[8];

  document.getElementById("l7").innerHTML = gul[0] + gul[1] + gul[2];
  document.getElementById("l8").innerHTML = gul[3] + gul[4] + gul[5];

  document.getElementById("l9").innerHTML = gul[6] + gul[7] + gul[8];
}

update();
