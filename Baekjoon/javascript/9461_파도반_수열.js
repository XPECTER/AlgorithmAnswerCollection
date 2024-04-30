// [백준9461](https://www.acmicpc.net/problem/9461)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./9461.txt')
  .toString()
  .trim()
  .split('\n');

const cases = inputs.splice(1).map(Number);
const arr = [0, 1, 1, 1, 2, 2].concat(Array(95).fill(0));
const answer = [];

for (let c of cases) {
  if (arr[c] !== 0) {
    answer.push(arr[c]);
    continue;
  }

  for (let j = 5; j <= c; j++) {
    if (arr[j] === 0) {
      arr[j] = arr[j - 1] + arr[j - 5];
    }
  }

  answer.push(arr[c]);
}

console.log(answer.join('\n'));
