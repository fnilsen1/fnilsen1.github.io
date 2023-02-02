//["Østfold", "Akershus", "Oslo", "Hedmark", "Oppland", "Buskerud", "Vestfold", "Telemark", "Aust-Agder", "Vest-Agder", "Rogaland", "Hordaland", "Sogn og Fjordane", "Møre og Romsdal", "Trøndelag", "Nordland", "Troms", "Finnmark"]

let tjukk_l = [
  "Østfold",
  "Akershus",
  "Oslo",
  "Hedmark",
  "Oppland",
  "Buskerud",
  "Vestfold",
  "Telemark",
  "Møre og Romsdal",
  "Trøndelag",
  "Nordland",
];

let vanlig_l = [
  "Telemark",
  "Aust-Agder",
  "Vest-Agder",
  "Rogaland",
  "Hordaland",
  "Sogn og Fjordane",
  "Møre og Romsdal",
  "Nordland",
  "Troms",
  "Finnmark",
];

let palatalisering_hoved_endestavelse = [
  "Sogn og Fjordane",
  "Møre og Romsdal",
  "Trøndelag",
  "Oppland",
  "Hedmark",
];

let palatalisering_hovedstavelse = [
  "Nordland",
  "Troms",
  "Finnmark",
  "Trøndelag",
  "Hedmark",
  "Oppland",
];

let ikke_palatalisering = [
  "Østfold",
  "Akershus",
  "Oslo",
  "Hedmark",
  "Oppland",
  "Buskerud",
  "Vestfold",
  "Telemark",
  "Aust-Agder",
  "Vest-Agder",
  "Rogaland",
  "Hordaland",
  "Sogn og Fjordane",
];

let je_jæ_jæi = [
  "Hedmark",
  "Oslo",
  "Akershus",
  "Østfold",
  "Vestfold",
  "Oppland",
  "Buskerud",
  "Telemark",
  "Trøndelag",
];

let eg = [
  "Hordaland",
  "Rogaland",
  "Telemark",
  "Aust-Agder",
  "Nordland",
  "Troms",
];

let æ = ["Vest-Agder", "Trøndelag", "Troms", "Finnmark"];

let e = [
  "Oppland",
  "Sogn og Fjordane",
  "Buskedrud",
  "Aust-Agder",
  "Nordland",
  "Troms",
];

let vi = [
  "Trøndelag",
  "Nordland",
  "Troms",
  "Finnmark",
  "Hedmark",
  "Oppland",
  "Buskerud",
  "Telemark",
  "Oslo",
  "Akershus",
  "Østfold",
  "Vestfold",
  "Sogn og Fjordane",
  "Møre og Romsdal",
];

let me_mi = [
  "Hedmark",
  "Oppland",
  "Buskerud",
  "Telemark",
  "Aust-Agder",
  "Vest-Agder",
  "Rogaland",
  "Hordaland",
  "Sogn og Fjordane",
  "Møre og Romsdal",
  "Trøndelag",
];

let oss = ["Oppland", "Hedmark", "Trøndelag", "Møre og Romsdal"];

let ikkje = [
  "Oppland",
  "Buskerud",
  "Telemark",
  "Aust-Agder",
  "Vest-Agder",
  "Rogaland",
  "Hordaland",
  "Sogn og Fjordane",
  "Møre og Romsdal",
];

let ikke = ["Oslo", "Akershus", "Vestfold", "Østfold", "Finnmark", "Troms"];

let itte = ["Hedmark", "Oppland", "Buskerud", "Akershus"];

let itj = ["Trøndelag"];

let jamvekt_uapokope = [
  "Hedmark",
  "Oppland",
  "Buskerud",
  "Telemark",
  "Oslo",
  "Akershus",
  "Østfold",
  "Vestfold",
  "Møre og Romsdal",
];
let jamvekt_apokope = ["Trøndelag", "Hedmark", "Møre og Romsdal"];
let apokopemål = ["Nordland"];
let a_mål = ["Vest-Agder", "Rogaland", "Hordaland", "Sogn og Fjordane"];
let e_mål = [
  "Telemark",
  "Aust-Agder",
  "Vest-Agder",
  "Sogn og Fjordane",
  "Møre og Romsdal",
  "Finnmark",
  "Troms",
];

let bløte_konsonanter = ["Rogaland", "Vest-Agder", "Aust-Agder"];

let sterke_hunkjønnsord_a = [
  "Troms",
  "Finnmark",
  "Nordland",
  "Trøndelag",
  "Østfold",
  "Akershus",
  "Oslo",
  "Hedmark",
  "Oppland",
  "Buskerud",
  "Vestfold",
  "Telemark",
  "Aust-Agder",
  "Sogn og Fjordane",
  "Møre og Romsdal",
];
let sterke_hunkjønnsord_e = [
  "Oppland",
  "Buskerud",
  "Telemark",
  "Aust-Agder",
  "Nordland",
];
let sterke_hunkjønnsord_æ = [
  "Hordaland",
  "Telemark",
  "Aust-Agder",
  "Vest-Agder",
  "Nordland",
];
let sterke_hunkjønnsord_i = ["Telemark", "Sogn og Fjordane"];
let sterke_hunkjønnsord_å = ["Rogaland", "Vest-Agder"];
let sterke_hunkjønnsord_o = ["Rogaland", "Hordaland"];
let sterke_hunkjønnsord_ei = ["Telemark", "Sogn og Fjordane"];

let skarre_r = [
  "Aust-Agder",
  "Vest-Agder",
  "Rogaland",
  "Hordaland",
  "Sogn og Fjordane",
];

let dativ_vedsubst = [
  "Hedmark",
  "Trøndelag",
  "Oppland",
  "Buskerud",
  "Sogn og Fjordane",
  "Møre og Romsdal",
  "Hordaland",
];

function finn_fylke() {
  let arr = [];
  if (document.getElementById("l").value != "blank") {
    let l = document.getElementById("l").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  if (document.getElementById("palatalisering").value != "blank") {
    let l = document.getElementById("palatalisering").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  if (document.getElementById("jeg").value != "blank") {
    let l = document.getElementById("jeg").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  if (document.getElementById("vi").value != "blank") {
    let l = document.getElementById("vi").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  if (document.getElementById("ikke").value != "blank") {
    let l = document.getElementById("ikke").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  if (document.getElementById("jamvekt").value != "blank") {
    let l = document.getElementById("jamvekt").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  if (document.getElementById("bløte").value != "blank") {
    let l = document.getElementById("bløte").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  if (document.getElementById("hunkjønnsord").value != "blank") {
    let l = document.getElementById("hunkjønnsord").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  if (document.getElementById("r").value != "blank") {
    let l = document.getElementById("r").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  if (document.getElementById("dativ").value != "blank") {
    let l = document.getElementById("dativ").value;

    let array = eval(l);

    arr = arr.concat(array);
  }

  countStrings(arr);
}

function countStrings(strings) {
  div = document.getElementById("svar");
  div.innerHTML = "";
  // Create an object to store the count for each string
  const counts = {};

  // Loop through the array of strings
  for (const string of strings) {
    // If the string is not in the counts object, set its count to 1
    if (!counts[string]) {
      counts[string] = 1;
    } else {
      // Otherwise, increment its count by 1
      counts[string] += 1;
    }
  }

  // Create an array of [string, count] pairs, then sort it in descending order by count
  const sortedCounts = Object.entries(counts).sort((a, b) => b[1] - a[1]);

  // Log each string and its count
  let answers = [];
  for (const [string, count] of sortedCounts) {
    answers.push(`${string}: ${count}`);
  }
  //   document.getElementById("svar").innerHTML = answers.join(" ");

  for (const string of answers) {
    // Create a new element to hold each string
    const p = document.createElement("p");

    // Set the text content of the new element to the current string
    p.textContent = string;

    // Add the new element to the div

    div.appendChild(p);
  }
}
