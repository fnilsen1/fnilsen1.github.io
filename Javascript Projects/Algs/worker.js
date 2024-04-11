// Copy the moves array to the worker file
let moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"];
// let moves = ["R","R'","R2","U","U'","U2", "F","F'","F2"]
let index_arr = [];
let start_arr = [];
let algs_arr = [];

function generate_algs(length) {
  for (let j = 0; j < length; j++) {
    index_arr[j]++;
    index_arr[j] %= 18;

    if (index_arr[j] !== 0)
      break;
  }

  for (let k = 0; k < length - 1; k++) {
    if (Math.floor(index_arr[k] / 3) === Math.floor(index_arr[k + 1] / 3))
      return;
  }

  for (let l = 0; l < length - 2; l++) {
    if (Math.floor(index_arr[l] / 6) === Math.floor(index_arr[l + 1] / 6) && Math.floor(index_arr[l] / 3) === Math.floor(index_arr[l + 2] / 3))
      return;
  }

  let copy = [...index_arr];
  for (let m = 0; m < length; m++) {
    copy[m] = moves[index_arr[m]];
  }

  copy = copy.join(" ");
  algs_arr.push(copy);
}

function generate(n) {
  for (let i = 0; i < n; i++) {
    index_arr.push(0);
  }
  start_arr = [...index_arr];
  generate_algs(n);

  while (index_arr.join(",") !== start_arr.join(",")) {
    generate_algs(n);
  }
}

function generate_upto(n) {
  for (let i = 1; i < n + 1; i++) {
    index_arr = [];
    generate(i);
  }
console.log(algs_arr);
console.log(algs_arr.length);
}
generate_upto(6)


