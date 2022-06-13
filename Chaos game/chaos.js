let objekt = [
  [667, 100],
  [967, 620],
  [367, 620],
];

x1 = 0;
y1 = 0;
z = 1;
function nytt_punkt() {
  y = document.getElementById("input").value;
  if (z == 1) {
    let p = 0 | (Math.random() * 3);
    console.log(p);
    let a = objekt[p];
    let b = (a[0] + 667) / 2;
    let c = (a[1] + 400) / 2;

    var html = `<circle
    cx='${b}'
    cy='${c}'
    r='1'
    stroke='black'
    stroke-width='3'
    fill='red'
  />`;
    document.getElementById("svg").innerHTML += html;

    z += 1;
    x1 = b;
    y1 = c;
  }
  for (i = 0; i < y; i++) {
    let r = 0 | (Math.random() * 3);

    let u = objekt[r];

    let q = (u[0] + x1) / 2;
    let s = (u[1] + y1) / 2;

    var smh = `<circle
        cx='${q}'
        cy='${s}'
        r='1'
        stroke='black'
        stroke-width='3'
        fill='red'
      />`;
    document.getElementById("svg").innerHTML += smh;
    x1 = q;
    y1 = s;
  }
}
// nytt_punkt();
