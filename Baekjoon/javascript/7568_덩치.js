// [백준7568](https://www.acmicpc.net/problem/7568)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./7568.txt')
  .toString()
  .trim()
  .split('\n');

const N = +inputs.shift();
const arr = inputs.map((elem) => elem.split(' ').map(Number));
const answer = [];
console.log(N, arr);

for (let i = 0; i < arr.length; i++) {
  let grade = 1;

  for (let j = 0; j < arr.length; j++) {
    if (i === j) continue;

    if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) {
      grade++;
    }
  }

  answer.push(grade);
}

console.log(answer.join(' '));
