// [백준11659](https://www.acmicpc.net/problem/11659)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./11659.txt')
  .toString()
  .trim()
  .split('\n');

const [N, M] = inputs.shift().split(' ').map(Number);
const arr = inputs.shift().split(' ').map(Number);
const sumArr = [];
const answer = [];
let sum = 0;

for (let i = 0; i < N; i++) {
  sum += arr[i];
  sumArr.push(sum);
}

for (let j = 0; j < M; j++) {
  let [start, end] = inputs[j].split(' ').map(Number);

  if (start === 1) {
    answer.push(sumArr[end - 1]);
    continue;
  }

  answer.push(sumArr[end - 1] - sumArr[start - 2]);
}

console.log(answer.join('\n'));
