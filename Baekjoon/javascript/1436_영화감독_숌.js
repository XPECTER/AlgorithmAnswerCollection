// [백준1436](https://www.acmicpc.net/problem/1436)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs').readFileSync('./1436.txt').toString().trim();

let num = 666;
let count = 0;
const N = +inputs;
let answer = 0;

while (true) {
  if (num.toString().includes('666')) {
    count += 1;
    if (count === N) {
      answer = num;
      break;
    }
  }

  num++;
}

console.log(answer);
