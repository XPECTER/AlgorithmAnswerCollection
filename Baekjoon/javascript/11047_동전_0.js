// [백준11047](https://www.acmicpc.net/problem/10026)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./11047.txt')
  .toString()
  .trim()
  .split('\n');

let [N, K] = inputs.shift().split(' ').map(Number);
const coins = inputs.map(Number);
let answer = 0;

for (let i = coins.length - 1; i >= 0; i--) {
  if (K / coins[i] >= 1) {
    answer += Math.floor(K / coins[i]);
    K %= coins[i];

    if (K === 0) break;
  }
}

console.log(answer);
