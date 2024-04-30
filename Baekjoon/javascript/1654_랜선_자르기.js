// [백준1654](https://www.acmicpc.net/problem/1654)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const inputs = require('fs')
  .readFileSync('./1654.txt')
  .toString()
  .trim()
  .split('\n');

const [K, N] = inputs.shift().split(' ').map(Number);
const lines = inputs.map(Number);

const solution = (K, N, lines) => {
  let maxLen = Math.floor(lines.reduce((acc, cur) => (acc += cur), 0) / N);
  let minLen = 0;

  while (minLen < maxLen) {
    let middle = Math.floor((maxLen + minLen) / 2);
    let cuts = 0;

    lines.forEach((val, idx) => {
      if (val / middle >= 1) {
        cuts += Math.floor(val / middle);
      }
    });

    if (cuts >= N) {
      minLen = middle + 1;
    } else if (cuts < N) {
      maxLen = middle - 1;
    }
  }

  return minLen;
};

console.log(solution(K, N, lines));
