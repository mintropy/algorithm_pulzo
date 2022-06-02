const [MN, ...D] = require("fs")
  .readFileSync(require("path").join(__dirname, "dev/stdin"))
  .toString()
  .split("\n");
const [M, N] = MN.split(" ").map((e) => +e);

const storedValues = Array(M)
  .fill()
  .map((_) => Array(N).fill(0));
const outputValues = Array(M)
  .fill()
  .map((_) => Array(N).fill(0));

for (let i = 0; i < M; i++) {
  outputValues[i][0] = +D[i][0];
}

for (let j = 1; j < N; j++) {
  for (let i = 0; i < M; i++) {
    const inputValues = [outputValues[i][j - 1]];
    if (i - 1 > 0) inputValues.push(outputValues[i - 1][j - 1]);
    if (i + 1 < M) inputValues.push(outputValues[i + 1][j - 1]);
    const maxValue = Math.max(...inputValues);
    storedValues[i][j] = maxValue;
    outputValues[i][j] = +D[i][j] + maxValue;
  }
}

console.log(Math.max(...storedValues[M - 1]));
