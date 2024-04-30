// [백준10026](https://www.acmicpc.net/problem/10026)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./10026.txt')
  .toString()
  .trim()
  .split('\n');

const edge = +inputs.shift();
inputs.forEach((elem, idx) => {
  inputs[idx] = elem.split('');
});

const common = JSON.parse(JSON.stringify(inputs));
const redGreen = JSON.parse(JSON.stringify(inputs));
const answer = [];

redGreen.forEach((val, idx) => {
  redGreen[idx] = val.map((char) => (char === 'R' ? 'G' : char));
});

const solution = (board, len) => {
  const stack = [];
  const dir = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  let area = 0;

  for (let row = 0; row < len; row++) {
    for (let col = 0; col < len; col++) {
      if (board[row][col] === 0) {
        continue;
      }

      stack.push([row, col]);
      let color = board[row][col];
      board[row][col] = 0;

      while (stack.length !== 0) {
        let [y, x] = stack.pop();

        for (let i = 0; i < 4; i++) {
          let nX = dir[i][0] + x;
          let nY = dir[i][1] + y;

          if (
            0 <= nX &&
            nX < len &&
            0 <= nY &&
            nY < len &&
            board[nY][nX] === color
          ) {
            board[nY][nX] = 0;
            stack.push([nY, nX]);
          }
        }
      }

      area += 1;
    }
  }

  return area;
};

answer.push(solution(common, edge));
answer.push(solution(redGreen, edge));
console.log(answer.join(' '));
