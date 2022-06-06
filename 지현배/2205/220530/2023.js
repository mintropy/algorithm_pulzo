const N = +require("fs")
  .readFileSync(require("path").join(__dirname, "dev/stdin"))
  .toString()
  .trim();

const prime = {
  1: [2, 3, 5, 7],
};

function check(value) {
  for (let i = 2; i <= value ** 0.5; i++) {
    if (value % i === 0) {
      return false;
    }
  }
  return true;
}

for (let i = 2; i < N + 1; i++) {
  prime[i] = [];
  prime[i - 1].forEach((p) => {
    for (let j = 0; j < 5; j++) {
      if (check(10 * p + 2 * j + 1)) {
        prime[i].push(10 * p + 2 * j + 1);
      }
    }
  });
}

console.log(prime[N].join("\n"));
