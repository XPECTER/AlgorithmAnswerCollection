// [백준28702](https://www.acmicpc.net/problem/28702)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./28702.txt')
  .toString()
  .trim()
  .split('\n');

let num, idx;

for (let i = 0; i < 3; i++) {
  const n = parseInt(inputs[i]);

  if (!n) continue;

  num = n;
  idx = i;
  break;
}

num = num + 3 - idx;

if (num % 5 === 0 && num % 3 === 0) {
  console.log('FizzBuzz');
} else if (num % 5 === 0) {
  console.log('Buzz');
} else if (num % 3 === 0) {
  console.log('Fizz');
} else {
  console.log(num);
}
