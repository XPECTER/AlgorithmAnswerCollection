// [백준1074](https://www.acmicpc.net/problem/1074)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim();

// IDE 입력
const inputs = require('fs').readFileSync('./1074.txt').toString().trim();

const [N, r, c] = inputs.split(' ').map(Number);

function recursive(len, row, col) {
  if (len === 1) return 0;

  const half = len / 2;
  let square = 0;
  if (col >= half) {
    square++;
    col = col - half;
  }
  if (row >= half) {
    square += 2;
    row = row - half;
  }

  return half * half * square + recursive(half, row, col);
}

const answer = recursive(2 ** N, r, c);
console.log(answer);
