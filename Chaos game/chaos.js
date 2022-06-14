let objekt = [
  [667, 100],
  [967, 620],
  [367, 620],
];

x1 = 0;
y1 = 0;
z = 1;
v = 1;
n = 0;
function nytt_punkt() {
  y = document.getElementById("input").value;
  if (z == 1) {
    let p = 0 | (Math.random() * 3);
    console.log(p);
    let a = objekt[p];
    let b = (a[0] + 667) / 2;
    let c = (a[1] + 400) / 2;

    let point = document.createElementNS("http://www.w3.org/2000/svg", "path");
    point.setAttribute("cx", b);
    point.setAttribute("cy", c);
    point.setAttribute("r", "1");
    point.setAttribute("stroke", "black");
    point.setAttribute("stroke-width", "3");
    point.setAttribute("fill", "red");

    document.getElementById("svg").append(point);

    z += 1;
    x1 = b;
    y1 = c;
  }
  for (i = 0; i < y; i++) {
    let r = 0 | (Math.random() * 3);

    let u = objekt[r];

    let q = (u[0] + x1) / 2;
    let s = (u[1] + y1) / 2;

    // var smh = `<circle
    //     cx='${q}'
    //     cy='${s}'
    //     r='1'
    //     stroke='black'
    //     stroke-width='3'
    //     fill='red'
    //   />`;

    // document.getElementById("svg").innerHTML += smh;

    let point = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "circle"
    );
    point.setAttribute("cx", q);
    point.setAttribute("cy", s);
    point.setAttribute("r", "1");
    point.setAttribute("stroke", "black");
    point.setAttribute("stroke-width", "3");
    point.setAttribute("fill", "red");

    document.getElementById("svg").append(point);
    x1 = q;
    y1 = s;
  }
}

function animasjon() {
  let r = 0 | (Math.random() * 3);

  let u = objekt[r];

  let q = (u[0] + x1) / 2;
  let s = (u[1] + y1) / 2;
  let point = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  point.setAttribute("cx", q);
  point.setAttribute("cy", s);
  point.setAttribute("r", "1");
  point.setAttribute("stroke", "black");
  point.setAttribute("stroke-width", "3");
  point.setAttribute("fill", "red");

  document.getElementById("svg").append(point);
  x1 = q;
  y1 = s;
  let morad = document.getElementById("input").value;

  n++;

  console.log(n);
  if (n > morad) {
    clearInterval(intervall);
  }
}

function interval() {
  globalThis.intervall = setInterval(animasjon, 10);
}

function slett() {
  n = 0;
  document.getElementById("svg").innerHTML = "";
  document.getElementById(
    "svg"
  ).innerHTML += `<polygon points="667,100 967,620 367,620" class="triangle" />
      <circle
        cx="667"
        cy="400"
        r="1"
        stroke="black"
        stroke-width="3"
        fill="red"
      />

      <circle
        cx="667"
        cy="100"
        r="1"
        stroke="black"
        stroke-width="3"
        fill="red"
      />

      <circle
        cx="967"
        cy="620"
        r="1"
        stroke="black"
        stroke-width="3"
        fill="red"
      />

      <circle
        cx="367"
        cy="620"
        r="1"
        stroke="black"
        stroke-width="3"
        fill="red"
      />`;
}
