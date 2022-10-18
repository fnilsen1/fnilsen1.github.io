function factorial(n) {
  let answer = 1;
  if (n == 0 || n == 1) {
    return answer;
  } else {
    for (var i = n; i >= 1; i--) {
      answer = answer * i;
    }
    return answer;
  }
}
function lucas(k, m) {
  sum = 0;
  for (j = 1; j < m + 1; j++) {
    v = 0;
    for (n = 1; n < k + 1; n++) {
      v += n ** (m - j);
    }
    sum +=
      (-1) ** j *
      (factorial(m + 1) / (factorial(j + 1) * factorial(m - j))) *
      v;
  }

  sum = (k ** (m + 1) - sum) / (m + 1);
  document.getElementById("absolute").value = sum;
}
// lucas(3, 2);
function svar() {
  b = parseInt(document.getElementById("m").value);
  a = parseInt(document.getElementById("k").value);

  lucas(a, b);
}
