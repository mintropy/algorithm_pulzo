const [NM, ...K] = require("fs")
  .readFileSync(require("path").join(__dirname, "dev/stdin"))
  .toString()
  .split("\n");
const [N, M] = NM.split(" ").map((e) => +e);
const Kn = K.map((e) => e.split(" ").map((el) => +el));
const dx = [-1, -1, 1, 1];
const dy = [1, -1, -1, 1];
const visited = Array(N)
  .fill()
  .map((_) => Array(M).fill(true));
let maxValue = 0;

function dfs(n, value) {
  if (n >= N * M) {
    maxValue = Math.max(value, maxValue);
    return;
  }
  const y = Math.floor(n / M);
  const x = n % M;
  if (!visited[y][x]) {
    dfs(n + 1, value);
  } else {
    visited[y][x] = false;
    for (let k = 0; k < 4; k++) {
      const ny = y + dy[k];
      const nx = x + dx[k];

      if (
        ny >= 0 &&
        ny < N &&
        nx >= 0 &&
        nx < M &&
        visited[ny][x] &&
        visited[y][nx]
      ) {
        visited[ny][x] = false;
        visited[y][nx] = false;
        const nextValue = Kn[y][x] * 2 + Kn[ny][x] + Kn[y][nx];
        dfs(n + 1, value + nextValue);
        visited[ny][x] = true;
        visited[y][nx] = true;
      }
    }
    visited[y][x] = true;
    dfs(n + 1, value);
  }
}

dfs(0, 0);

console.log(maxValue);
