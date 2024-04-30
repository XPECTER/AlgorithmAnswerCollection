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
  let maxLen = Math.max(...lines);
  let minLen = 1;
  let answer = 0;

  while (minLen <= maxLen) {
    let middle = Math.floor((maxLen + minLen) / 2);
    let cuts = lines.reduce((acc, cur) => acc + Math.floor(cur / middle), 0);

    if (cuts >= N) {
      minLen = middle + 1;
      answer = middle;
    } else {
      maxLen = middle - 1;
    }
  }

  return answer;
};

console.log(solution(K, N, lines));
