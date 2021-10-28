const fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().replace("\n", "") - 0;
let min = 100;
let max = 0;
const sol = (num, sum) => {
  if (num < 10) {
    if (num % 2) sum++;
    if (max < sum) max = sum;
    if (min > sum) min = sum;
    return;
  }
  else if (num < 100) {
    sol(num % 10 + Math.floor(num / 10), sum + (num % 2 ? 1 : 0) + (Math.floor(num / 10) % 2 ? 1 : 0));
    return;
  }
  else {
    // 홀수 몇개?
    let n = num;
    while (n) {
      sum += (n % 2 ? 1 : 0);
      n = Math.floor(n / 10);
    }
    let s = num + "";
    let len = s.length;
    // 분할
    for (let i = 1; i < len - 1; i++) {
      for (let j = i + 1; j < len; j++) {
        // 숫자를 나눈다.
        let front = +s.slice(0, i);
        let middle = +s.slice(i, j);
        let back = +s.slice(j);
        sol(front + middle + back, sum);
      }
    }
  }
}
sol(input, 0);
console.log(min, max);