// [백준18111](https://www.acmicpc.net/problem/18111)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./18111.txt')
  .toString()
  .trim()
  .split('\n');

let [M, N, B] = inputs.shift().split(' ').map(Number);
const ground = new Array(257).fill(0);

let minSecond = Infinity;
let height = 0;

inputs.map((elem) => {
  elem.split(' ').map((val) => {
    ground[+val]++;
  });
});

for (let i = 256; i >= 0; i--) {
  let cut = 0;
  let fill = 0;

  ground.map((amount, idx) => {
    if (idx > i) {
      cut += (idx - i) * amount;
    } else if (idx < i) {
      fill += (i - idx) * amount;
    }
  });

  if (fill - cut > B) {
    continue;
  }

  let second = fill + cut * 2;

  if (second < minSecond) {
    minSecond = second;
    height = i;
  } else if (second > minSecond) {
    break;
  }
}

console.log(minSecond, height);
