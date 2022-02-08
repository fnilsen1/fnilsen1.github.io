function endring() {
  var skala = document.getElementById("points").value;
  document.getElementById("skala_tall").innerText = skala;
}
//Legger til en rad
function add() {
  var fag = document.getElementById("inputfag").value;
  var oppgave = document.getElementById("oppgave").value;
  var input_uke = document.getElementById("inputdato").value;
  var skala = document.getElementById("points").value;
  console.log(skala);

  if (fag != "" && oppgave != "" && input_uke < 53) {
    console.log(input_uke);
    var table = document.getElementById("table");
    var row = document.createElement("tr");
    var img = document.createElement("img");

    img.setAttribute("src", "src/trash.png");

    var nameA = document.createElement("td");
    nameA.append(fag, img);

    var nameB = document.createElement("td");
    nameB.append(oppgave);

    var uke = document.createElement("td");
    uke.append(input_uke);

    var skalacelle = document.createElement("td");

    if (skala == 1) {
      skalacelle.id = "red";
    }
    if (skala == 2) {
      skalacelle.id = "orange";
    }

    if (skala == 3) {
      skalacelle.id = "yellow";
    }

    if (skala == 4) {
      skalacelle.id = "lime";
    }

    if (skala == 5) {
      skalacelle.id = "green";
    }

    skalacelle.append(skala);

    row.append(nameA, nameB, uke, skalacelle);
    table.append(row);

    row.id = "tableRow";
    img.id = "søppel";
    img.setAttribute("onclick", "remove(this)");
  }
}

window.addEventListener("keydown", enter, false);

function enter(key) {
  if (key.keyCode == "13") {
    add();
  }
}

function remove(me) {
  var child = me.parentNode.parentNode.rowIndex;
  var selectedChild = document.getElementById("table").children[child];

  document.getElementById("table").removeChild(selectedChild);
}

z = 1;
function sort(element) {
  var pilned =
    document.getElementsByClassName("pilned")[element.parentNode.cellIndex - 1];
  pilned.style.transform += "rotate(180deg)";

  var switched = 1;

  var table = document.getElementById("table");

  var rows = table.rows;

  if (z == 1) {
    z++;
    while (switched == 1) {
      switched = 0;

      for (i = 1; i < rows.length - 1; i++) {
        var x =
          rows[i].getElementsByTagName("TD")[element.parentNode.cellIndex];

        var y =
          rows[i + 1].getElementsByTagName("TD")[element.parentNode.cellIndex];

        if (parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
          table.insertBefore(rows[i + 1], rows[i]);

          switched = 1;
        }
      }
    }
  } else if (z == 2) {
    z--;
    while (switched == 1) {
      switched = 0;

      for (i = 1; i < rows.length - 1; i++) {
        var x =
          rows[i].getElementsByTagName("TD")[element.parentNode.cellIndex];

        var y =
          rows[i + 1].getElementsByTagName("TD")[element.parentNode.cellIndex];

        if (parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) {
          table.insertBefore(rows[i + 1], rows[i]);

          switched = 1;
        }
      }
    }
  }
}

k = 1;
function sort2(element) {
  var pilned =
    document.getElementsByClassName("pilned")[element.parentNode.cellIndex - 1];
  pilned.style.transform += "rotate(180deg)";

  var switched = 1;

  var table = document.getElementById("table");

  var rows = table.rows;

  if (k == 1) {
    k++;
    while (switched == 1) {
      switched = 0;

      for (i = 1; i < rows.length - 1; i++) {
        var x =
          rows[i].getElementsByTagName("TD")[element.parentNode.cellIndex];

        var y =
          rows[i + 1].getElementsByTagName("TD")[element.parentNode.cellIndex];

        if (parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
          table.insertBefore(rows[i + 1], rows[i]);

          switched = 1;
        }
      }
    }
  } else if (k == 2) {
    k--;
    while (switched == 1) {
      switched = 0;

      for (i = 1; i < rows.length - 1; i++) {
        var x =
          rows[i].getElementsByTagName("TD")[element.parentNode.cellIndex];

        var y =
          rows[i + 1].getElementsByTagName("TD")[element.parentNode.cellIndex];

        if (parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) {
          table.insertBefore(rows[i + 1], rows[i]);

          switched = 1;
        }
      }
    }
  }
}

t = 1;
function sort1(element) {
  var pilned =
    document.getElementsByClassName("pilned")[element.parentNode.cellIndex - 1];
  pilned.style.transform += "rotate(180deg)";

  var switched = 1;

  var table = document.getElementById("table");

  var rows = table.rows;

  if (t == 1) {
    t++;
    while (switched == 1) {
      switched = 0;

      for (i = 1; i < rows.length - 1; i++) {
        var x =
          rows[i].getElementsByTagName("TD")[element.parentNode.cellIndex];

        var y =
          rows[i + 1].getElementsByTagName("TD")[element.parentNode.cellIndex];

        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          table.insertBefore(rows[i + 1], rows[i]);

          switched = 1;
        }
      }
    }
  } else if (t == 2) {
    t--;
    while (switched == 1) {
      switched = 0;

      for (i = 1; i < rows.length - 1; i++) {
        var x =
          rows[i].getElementsByTagName("TD")[element.parentNode.cellIndex];

        var y =
          rows[i + 1].getElementsByTagName("TD")[element.parentNode.cellIndex];

        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          table.insertBefore(rows[i + 1], rows[i]);

          switched = 1;
        }
      }
    }
  }
}

var x = 0;
function darkmode() {
  console.log(x);
  if (x == 0) {
    x += 1;
    var body = document.body;
    var sol = document.getElementById("sol");

    sol.setAttribute("src", "src/måne.png");
    body.id = "dark_body";
    console.log(x);
  } else if (x == 1) {
    x -= 1;
    // console.log(x)
    var body = document.body;
    var sol = document.getElementById("sol");
    sol.setAttribute("src", "src/sol.png");

    body.id = "light_body";
  }
}

function delAll() {
  var rows = document.getElementById("table").rows;

  var orgRows = rows.length;

  for (let i = 0; i < orgRows - 1; i++) {
    table.removeChild(rows.item(1));
  }
}
