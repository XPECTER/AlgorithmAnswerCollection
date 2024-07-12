// [백준2630](https://www.acmicpc.net/problem/2630)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./2630.txt')
  .toString()
  .trim()
  .split('\n');

const N = +inputs.shift();
const paper = inputs.map((arr) => arr.split(' ').map(Number));
let blue = 0;
let white = 0;

function recursive(length, startX, startY) {
  const color = paper[startY][startX];

  try {
    for (let j = 0; j < length; j++) {
      for (let i = 0; i < length; i++) {
        if (paper[startY + j][startX + i] !== color) {
          throw true;
        }
      }
    }
    color === 1 ? blue++ : white++;
  } catch {
    const newLen = length / 2;
    recursive(newLen, startX, startY);
    recursive(newLen, startX, startY + newLen);
    recursive(newLen, startX + newLen, startY);
    recursive(newLen, startX + newLen, startY + newLen);
  }
}

recursive(N, 0, 0);
console.log(white + '\n' + blue);
