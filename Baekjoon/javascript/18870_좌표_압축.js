// [백준18870](https://www.acmicpc.net/problem/18870)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync(__dirname + '/18870.txt')
  .toString()
  .trim()
  .split('\n');

const N = +inputs[0];
const numbers = inputs[1].split(' ').map(Number);

// const mappingArr = [];
// let numSet = new Set(numbers);
// numSet = [...numSet].sort((a, b) => a - b);

// for (let i = 0; i < numSet.length; i++) {
//   mappingArr[numSet[i]] = i;
// }

// const answer = numbers.map((num) => mappingArr[num]);
// console.log(answer.join(' '));

// 중복 제거 및 정렬 없이 직접 인덱스 매핑
const mappingArr = [];
const used = Array(1000001).fill(false); // 문제 조건에 따라 최대 1000000 이하의 정수가 주어짐

for (let i = 0; i < N; i++) {
  const num = numbers[i];
  if (!used[num + 1000000]) {
    used[num + 1000000] = true;
    mappingArr.push(num);
  }
}

const mappingObj = {};
mappingArr
  .sort((a, b) => a - b)
  .forEach((num, idx) => {
    mappingObj[num] = idx;
  });

const answer = numbers.map((num) => mappingObj[num]);
console.log(answer.join(' '));
