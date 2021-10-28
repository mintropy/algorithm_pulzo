const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim();
// funcking "\n"
input = input.replace("\n", "");
const sol = () => {
  let includeL = false;
  let underBar = [];
  let vowels = ["A", "E", "I", "O", "U"];
  let res = 0;
  let data = [4, 4];
  data.push(...input.split('').map((e, i) => {
    if (e == "L") {
      includeL = true;
      return 1;
    }
    else if (e == "_") {
      underBar.push(i + 2);
      return 0;
    }
    else if (vowels.indexOf(e) != -1) return 2;
    else return 1;
  }));
  data.push(4, 4);
  for (let i = 2; i < data.length - 4; i++) {
    if (data[i] == data[i + 1] && data[i] == data[i + 2] && data[i] != 0) {
      return 0;
    }
  }
  if (underBar.length == 0) return 1;
  const check = (data, i, k) => {
    if (!((data[i - 2] == data[i - 1]) && (data[i - 2] == k)) && 
    !((data[i - 1] == data[i + 1]) && (data[i - 1] == k)) &&
    !((data[i + 1] == data[i + 2]) && (data[i + 1] == k))) {
      return true;
    }
    else return false;
  }
  const DFS = (idx, L, n) => {
    if (idx >= underBar.length) {
      if (L == true) res += n;
      return;
    }
    let i = underBar[idx];
    if (check(data, i, 1) === true) {
      data[i] = 1;
      DFS(idx + 1, L, n * 20);
      DFS(idx + 1, true, n);
      data[i] = 0;
    }
    if (check(data, i, 2) === true) {
      data[i] = 2;
      DFS(idx + 1, L, n * 5);
      data[i] = 0;
    }
  }
  DFS(0, includeL, 1);
  return res;
}
console.log(sol());