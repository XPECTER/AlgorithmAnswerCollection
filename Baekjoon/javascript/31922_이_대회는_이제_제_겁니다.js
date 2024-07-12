// [백준31922](https://www.acmicpc.net/problem/31922)

// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim();

// IDE 입력
const inputs = require('fs').readFileSync('./31922.txt').toString().trim();

const [A, P, C] = inputs.split(' ').map(Number);
console.log(A + C > P ? A + C : P);
