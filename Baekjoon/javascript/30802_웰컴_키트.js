// [백준30802](https://www.acmicpc.net/problem/30802)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./30802.txt')
  .toString()
  .trim()
  .split('\n');

console.log(inputs);

const N = +inputs.shift();
const sizes = inputs.shift().split(' ').map(Number);
const [T, P] = inputs.shift().split(' ').map(Number);

let chunk = 0;

for (let size of sizes) {
  chunk += Math.floor((size - 1) / T) + 1;
}

let pen = [0, 0];
pen[0] = Math.floor(N / P);
pen[1] = N % P;

console.log(chunk);
console.log(pen.join(' '));
