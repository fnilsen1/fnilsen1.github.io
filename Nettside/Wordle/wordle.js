var ord = [
  "cigar",
  "rebut",
  "sissy",
  "humph",
  "awake",
  "blush",
  "focal",
  "evade",
  "naval",
  "serve",
  "heath",
  "dwarf",
  "model",
  "karma",
  "stink",
  "grade",
  "quiet",
  "bench",
  "abate",
  "feign",
  "major",
  "death",
  "fresh",
  "crust",
  "stool",
  "colon",
  "abase",
  "marry",
  "react",
  "batty",
  "pride",
  "floss",
  "helix",
  "croak",
  "staff",
  "paper",
  "unfed",
  "whelp",
  "trawl",
  "outdo",
  "adobe",
  "crazy",
  "sower",
  "repay",
  "digit",
  "crate",
  "cluck",
  "spike",
  "mimic",
  "pound",
  "maxim",
  "linen",
  "unmet",
  "flesh",
  "booby",
  "forth",
  "first",
  "stand",
  "belly",
  "ivory",
  "seedy",
  "print",
  "yearn",
  "drain",
  "bribe",
  "stout",
  "panel",
  "crass",
  "flume",
  "offal",
  "agree",
  "error",
  "swirl",
  "argue",
  "bleed",
  "delta",
];
var spes_ord = ord[0 | (Math.random() * ord.length)];
console.log(spes_ord);

function check() {
  var input = document.getElementById("gjett").value;
  console.log(input);
  var container = document.getElementById("container");

  //   console.log(input.substring(0));
  //   console.log(spes_ord.substring(0, 1));

  if (input.substring(0, 1) == spes_ord.substring(0, 1)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(0, 1);
    nameA.id = "green";
    nameA.setAttribute("class", "flex");
    container.append(nameA);
  } else if (input.substring(0, 1) != spes_ord.substring(0, 1)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(0, 1);
    nameA.setAttribute("class", "flex");

    if (
      input.substring(0, 1) == spes_ord.substring(1, 2) ||
      input.substring(0, 1) == spes_ord.substring(2, 3) ||
      input.substring(0, 1) == spes_ord.substring(3, 4) ||
      input.substring(0, 1) == spes_ord.substring(4, 5)
    ) {
      nameA.id = "yellow";
      container.append(nameA);
    } else {
      container.append(nameA);
    }
  }

  if (input.substring(1, 2) == spes_ord.substring(1, 2)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(1, 2);
    nameA.id = "green";
    nameA.setAttribute("class", "flex");
    container.append(nameA);
  } else if (input.substring(1, 2) != spes_ord.substring(1, 2)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(1, 2);
    nameA.setAttribute("class", "flex");

    if (
      input.substring(1, 2) == spes_ord.substring(0, 1) ||
      input.substring(1, 2) == spes_ord.substring(2, 3) ||
      input.substring(1, 2) == spes_ord.substring(3, 4) ||
      input.substring(1, 2) == spes_ord.substring(4, 5)
    ) {
      nameA.id = "yellow";
      container.append(nameA);
    } else {
      container.append(nameA);
    }
  }

  if (input.substring(2, 3) == spes_ord.substring(2, 3)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(2, 3);
    nameA.id = "green";
    nameA.setAttribute("class", "flex");
    container.append(nameA);
  } else if (input.substring(2, 3) != spes_ord.substring(2, 3)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(2, 3);
    nameA.setAttribute("class", "flex");

    if (
      input.substring(2, 3) == spes_ord.substring(0, 1) ||
      input.substring(2, 3) == spes_ord.substring(1, 2) ||
      input.substring(2, 3) == spes_ord.substring(3, 4) ||
      input.substring(2, 3) == spes_ord.substring(4, 5)
    ) {
      nameA.id = "yellow";
      container.append(nameA);
    } else {
      container.append(nameA);
    }
  }

  if (input.substring(3, 4) == spes_ord.substring(3, 4)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(3, 4);
    nameA.id = "green";
    nameA.setAttribute("class", "flex");
    container.append(nameA);
  } else if (input.substring(3, 4) != spes_ord.substring(3, 4)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(3, 4);
    nameA.setAttribute("class", "flex");

    if (
      input.substring(3, 4) == spes_ord.substring(0, 1) ||
      input.substring(3, 4) == spes_ord.substring(1, 2) ||
      input.substring(3, 4) == spes_ord.substring(4, 5) ||
      input.substring(3, 4) == spes_ord.substring(3, 4)
    ) {
      nameA.id = "yellow";
      container.append(nameA);
    } else {
      container.append(nameA);
    }
  }

  if (input.substring(4, 5) == spes_ord.substring(4, 5)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(4, 5);
    nameA.id = "green";
    nameA.setAttribute("class", "flex");
    container.append(nameA);
  } else if (input.substring(4, 5) != spes_ord.substring(4, 5)) {
    var nameA = document.createElement("div");
    nameA.innerHTML = input.substring(4, 5);
    nameA.setAttribute("class", "flex");

    if (
      input.substring(4, 5) == spes_ord.substring(0, 1) ||
      input.substring(4, 5) == spes_ord.substring(1, 2) ||
      input.substring(4, 5) == spes_ord.substring(2, 3) ||
      input.substring(4, 5) == spes_ord.substring(3, 4)
    ) {
      nameA.id = "yellow";
      container.append(nameA);
    } else {
      container.append(nameA);
    }
  }
}
