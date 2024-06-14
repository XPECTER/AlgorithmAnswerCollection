// [백준31403](https://www.acmicpc.net/problem/31403)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./31403.txt')
  .toString()
  .trim()
  .split('\n');

const numberAnswer = inputs.reduce((acc, cur, idx) => {
  if (idx === 2) acc -= +cur;
  else acc += +cur;

  return acc;
}, 0);
const stringAnswer = inputs.reduce((acc, cur, idx) => {
  if (idx === 2) acc -= cur;
  else acc += cur;

  return acc;
}, '');

console.log(numberAnswer);
console.log(stringAnswer);
