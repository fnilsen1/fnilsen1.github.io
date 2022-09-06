function cancel(alg) {
  let trekk_liste = ["R", "L", "U", "D", "F", "B"];
  let split = alg.split(" ");

  for (let i = 1; i < split.length; i++) {
    if (split[i].substring(0, 1) == split[i - 1].substring(0, 1)) {
      // trekk_liste.indexOf(split[i].substring(0,1))
      if (
        split[i].substring(1, 2) == split[i - 1].substring(1, 2) &&
        split[i].substring(1, 2) !== "2"
      ) {
        let bokstav = split[i].substring(0, 1);
        split[i] = bokstav + "2";

        split.splice(i - 1, 1);
        // console.log(split);
      } else if (
        (split[i - 1].substring(1, 2) == "" &&
          split[i].substring(1, 2) == "2") ||
        (split[i - 1].substring(1, 2) == "2" && split[i].substring(1, 2) == "")
      ) {
        let bokstav = split[i].substring(0, 1);
        split[i] = bokstav + "'";

        split.splice(i - 1, 1);
      } else if (
        split[i - 1].substring(1, 2) == "'" &&
        split[i].substring(1, 2) == "2"
      ) {
        let bokstav = split[i].substring(0, 1);
        split[i] = bokstav + "";

        split.splice(i - 1, 1);
      } else if (
        (split[i - 1].substring(1, 2) == "'" &&
          split[i].substring(1, 2) == "") ||
        (split[i - 1].substring(1, 2) == "" &&
          split[i].substring(1, 2) == "'") ||
        (split[i - 1].substring(1, 2) == "2" && split[i].substring(1, 2) == "2")
      ) {
        split.splice(i - 1, 2);
      }
    }
  }

  let ny_split = split.join(" ");
  if (alg == ny_split) {
    // console.log(tell(ny_split).split(" ").length);
    return ny_split;
  } else {
    return cancel(ny_split);
  }
}

let stort_arr = [
  ["U", "D"],
  ["R", "L"],
  ["F", "B"],
];

function scramble() {
  let input = document.getElementById("cars").value;
  console.log(input);
  let a = 0 | (Math.random() * 6);
  let b = 0 | (Math.random() * 5);

  let moves = ["R", "L", "U", "D", "F", "B"];
  let double = ["R2", "L2", "U2", "D2", "F2", "B2"];
  let moves_unchanged = ["R", "L", "U", "D", "F", "B"];
  let tegn = ["'", "", "2"];
  let tegn2 = ["", "'"];
  let ny_scramble = [];
  let temp = moves[a];
  ny_scramble.push(moves[a]);
  moves.splice(a, 1);
  ny_scramble.push(moves[b]);
  moves.push(temp);

  for (i = 0; i < 10; i++) {
    let random = 0 | (Math.random() * 6);

    let nytt_trekk = moves_unchanged[random];
    if (nytt_trekk == ny_scramble[ny_scramble.length - 1]) {
      i--;
    } else if (
      nytt_trekk == ny_scramble[ny_scramble.length - 2] &&
      Math.floor(moves_unchanged.indexOf(nytt_trekk) / 2) ==
        Math.floor(
          moves_unchanged.indexOf(ny_scramble[ny_scramble.length - 1]) / 2
        )
    ) {
      i--;
    } else {
      ny_scramble.push(nytt_trekk);
    }
  }
  //   for (i = 0; i < 12; i++) {

  //   }
  console.log(ny_scramble);
  let movesunchanged = ["R", "L", "U", "D", "F", "B"];
  let c = 0 | (Math.random() * 3);
  let lagrede_trekk = [];
  for (j = 0; j < input; j++) {
    let d = 0 | (Math.random() * 2);
    let tilfeldig = 0 | (Math.random() * 2);
    let tilfeldig2 = 0 | (Math.random() * 12);

    if (
      stort_arr[c][d] == ny_scramble[tilfeldig2 - 1] ||
      stort_arr[c][d] == ny_scramble[tilfeldig2 + 1] ||
      stort_arr[c][d] == ny_scramble[tilfeldig2]
    ) {
      console.log("hei");
      j--;
    } else if (
      stort_arr[c][d] == ny_scramble[tilfeldig2 - 2] &&
      Math.floor(movesunchanged.indexOf(stort_arr[c][d]) / 2) ==
        Math.floor(
          movesunchanged.indexOf(ny_scramble[ny_scramble.length - 1]) / 2
        )
    ) {
      console.log("lmao");
      j--;
    } else if (
      stort_arr[c][d] == ny_scramble[tilfeldig2 + 2] &&
      Math.floor(movesunchanged.indexOf(stort_arr[c][d]) / 2) ==
        Math.floor(
          movesunchanged.indexOf(ny_scramble[ny_scramble.length + 1]) / 2
        )
    ) {
      console.log("lmao");
      j--;
    } else {
      ny_scramble[tilfeldig2] = stort_arr[c][d];
      //   ny_scramble[tilfeldig2] = stort_arr[c][d] + tilfeldig3 + "*";

      lagrede_trekk.push(tilfeldig2);
      console.log("yo");
      console.log(ny_scramble);
    }
  }
  console.log(lagrede_trekk);
  for (i = 0; i < ny_scramble.length; i++) {
    if (
      i == lagrede_trekk[0] ||
      i == lagrede_trekk[1] ||
      i == lagrede_trekk[2] ||
      i == lagrede_trekk[3]
    ) {
      //   i++;
    } else {
      ny_scramble[i] += 2;
      console.log(ny_scramble[i]);
    }
  }

  for (i = 0; i < ny_scramble.length; i++) {
    let tilfeldig3 = tegn2[0 | (Math.random() * 2)];
    if (ny_scramble[i].substring(1, 2) == 2) {
    } else {
      ny_scramble[i] += tilfeldig3;
    }
  }

  ny_scramble = ny_scramble.join(" ");
  document.getElementById("blanding").innerHTML =
    "Scramble: " + cancel(ny_scramble);

  console.log(cancel(ny_scramble));
}
// scramble();
function skaff_scramble() {
  let input = document.getElementById("cars").value;
  let input2 = document.getElementById("input").value;
  let input3 = document.getElementById("axis").value;

  getScrambleHTR(input2, input, parseInt(input3));
}
function getScrambleHTR(length = 20, quarterTurns = 4, qAxis = -1) {
  if (quarterTurns === 0) {
    quarterTurns = 1;
  }

  let scr = "";
  let randQ = Math.floor(Math.random() * 3);

  function makeScramble() {
    scr = "";
    let axises = [
      ["U", "D"],
      ["F", "B"],
      ["R", "L"],
    ];
    let movesAxis = [["", ""]];
    let curAxis = -1;
    let moves = [];
    for (let i = 0; i < length; i++) {
      let axis = Math.floor(Math.random() * axises.length);

      if (axis !== curAxis) {
        curAxis = axis;
        moves = movesAxis
          .map((m) => [m[0] + axises[curAxis][0] + m[1]])
          .concat(movesAxis.map((m) => [m[0] + axises[curAxis][1] + m[1]]));
      } else if (moves.length === 0) {
        i--;
        continue;
      }

      let move = moves[Math.floor(Math.random() * moves.length)];
      let moveE = "2";

      moves.splice(moves.indexOf(move), 1);

      scr += move + moveE + " ";
    }

    let qLengthArr = [
      scr.split(" ").filter((s) => {
        return s === "U2" || s === "D2";
      }).length,
      scr.split(" ").filter((s) => {
        return s === "F2" || s === "B2";
      }).length,
      scr.split(" ").filter((s) => {
        return s === "R2" || s === "L2";
      }).length,
    ];
    let qLength = qAxis === -1 ? qLengthArr[randQ] : qLengthArr[qAxis];

    if (qLength < quarterTurns) {
      makeScramble();
    }
  }

  makeScramble();

  let newScr = scr;
  while (quarterTurns > 0) {
    let nScr = [];
    for (let s of newScr.trim().split(" ")) {
      let qTurnArr = [
        s === "U2" || s === "D2",
        s === "F2" || s === "B2",
        s === "R2" || s === "L2",
      ];
      let qTurn = qAxis === -1 ? qTurnArr[randQ] : qTurnArr[qAxis];

      if (quarterTurns !== 0 && qTurn) {
        let ne = ["", "'", "2"][Math.floor(Math.random() * 3)];
        if (ne !== "2") {
          s = s.replace("2", ne);
          quarterTurns--;
        }
      }
      nScr.push(s);
    }
    newScr = nScr.join(" ");
  }

  document.getElementById("blanding").innerHTML = "Scramble: " + newScr;
}

function dr() {
  let trigger1 = ["R U R'", "L' U' L"];
  let trigger2 = ["R U2 R'", "L' U2 L"];
  let trigger3 = ["R", "L", "U", "D", "F", "B"];
  let select = document.getElementById("dr_select").value;

  let a = 0 | (Math.random() * 6);
  let b = 0 | (Math.random() * 5);

  let moves = ["R", "L", "U", "D", "F", "B"];

  let moves_unchanged = ["R", "L", "U", "D", "F", "B"];

  let ny_scramble = [];
  let temp = moves[a];
  ny_scramble.push(moves[a]);
  moves.splice(a, 1);
  ny_scramble.push(moves[b]);
  moves.push(temp);

  for (i = 0; i < 10; i++) {
    let random = 0 | (Math.random() * 6);

    let nytt_trekk = moves_unchanged[random];
    if (nytt_trekk == ny_scramble[ny_scramble.length - 1]) {
      i--;
    } else if (
      nytt_trekk == ny_scramble[ny_scramble.length - 2] &&
      Math.floor(moves_unchanged.indexOf(nytt_trekk) / 2) ==
        Math.floor(
          moves_unchanged.indexOf(ny_scramble[ny_scramble.length - 1]) / 2
        )
    ) {
      i--;
    } else {
      ny_scramble.push(nytt_trekk);
    }
  }

  let r1 = 0;
  let dr_arr = [];

  if (select == 0) {
    console.log(0);
    dr_arr = [...trigger1];
    r1 = 0 | (Math.random() * dr_arr.length);
  } else if (select == 1) {
    console.log(1);
    dr_arr = [...trigger2];
    r1 = 0 | (Math.random() * dr_arr.length);
  } else if (select == 2) {
    console.log(2);
    dr_arr = [...trigger3];
    r1 = 0 | (Math.random() * dr_arr.length);
  }

  for (m = 0; m < ny_scramble.length; m++) {
    console.log(ny_scramble);
    let morad = dr_arr[r1].charAt(dr_arr[r1].length - 1);
    let morad1 = dr_arr[r1].charAt(dr_arr[r1].length - 2);

    if (ny_scramble[m] == morad || ny_scramble[m] == morad1) {
      ny_scramble.splice(m, 1);
      m--;
    } else if (
      morad == ny_scramble[m + 1] &&
      Math.floor(moves_unchanged.indexOf(morad) / 2) ==
        Math.floor(moves_unchanged.indexOf(ny_scramble[m]) / 2)
    ) {
      ny_scramble.splice(m, 1);

      m--;
    } else if (
      morad1 == ny_scramble[m + 1] &&
      Math.floor(moves_unchanged.indexOf(morad1) / 2) ==
        Math.floor(moves_unchanged.indexOf(ny_scramble[m]) / 2)
    ) {
      ny_scramble.splice(m, 1);

      m--;
    } else {
      for (k = 0; k < ny_scramble.length; k++) {
        ny_scramble[k] = ny_scramble[k] + 2;
      }
      let concat_trigger = dr_arr[r1].split(" ");
      let dr_blanding = concat_trigger.concat(ny_scramble);

      document.getElementById("dr_scramble").innerHTML = dr_blanding.join(" ");
      return;
    }
  }
}
dr();
skaff_scramble();
