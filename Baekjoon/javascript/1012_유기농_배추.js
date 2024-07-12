// [백준1012](https://www.acmicpc.net/problem/1012)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./1012.txt')
  .toString()
  .trim()
  .split('\n');
const cases = inputs.shift();
const answer = [];

for (let i = 0; i < cases; i++) {
  const [M, N, K] = inputs.shift().split(' ').map(Number);
  const dir = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];

  const field = Array.from(Array(N), () => Array(M).fill(0));
  const cabage = inputs.splice(0, K).map((e) => e.split(' ').map(Number));
  cabage.map(([x, y]) => (field[y][x] = 1));
  let area = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (field[i][j] === 0) {
        continue;
      }

      const stack = [];
      stack.push([j, i]);

      while (stack.length > 0) {
        const [curX, curY] = stack.pop();
        if (field[curY][curX] === 0) {
          continue;
        }

        field[curY][curX] = 0;

        for (let [dY, dX] of dir) {
          let nX = curX + dX;
          let nY = curY + dY;
          if (0 <= nX && nX < M && 0 <= nY && nY < N && field[nY][nX] === 1) {
            stack.push([nX, nY]);
          }
        }
      }

      area++;
    }
  }
  answer.push(area);
}

console.log(answer.join('\n'));
