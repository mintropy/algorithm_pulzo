const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let [N, ...pic] = input;
const dnc = (n, i, j) => {
  if (n == '1') return pic[i][j];
  let d = Math.floor(n / 2);
  let lt = dnc(d, i, j);
  let rt = dnc(d, i, j + d);
  let lb = dnc(d, i + d, j);
  let rb = dnc(d, i + d, j + d);
  if (lt.length === 1 && (lt == rt) && (lt == lb) && (lt == rb)) return lt;
  else return "(" + lt + rt + lb + rb + ")";
}
console.log(dnc(N, 0, 0));