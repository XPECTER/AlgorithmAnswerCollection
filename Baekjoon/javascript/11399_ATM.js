// [백준11399](https://www.acmicpc.net/problem/11399)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./11399.txt')
  .toString()
  .trim()
  .split('\n');

const amount = +inputs.shift();
const arr = inputs[0]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);
const answer = arr.reduce((acc, cur, idx) => (acc += cur * (amount - idx)), 0);
console.log(answer);
