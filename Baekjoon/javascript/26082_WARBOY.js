// [백준26082](https://www.acmicpc.net/problem/26082)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim();

// IDE 입력
const inputs = require('fs').readFileSync('./26082.txt').toString().trim();
const [A, B, C] = inputs.split(' ').map(Number);
console.log((B / A) * 3 * C);
console.log(A, B, C);
