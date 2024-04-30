// [백준11726](https://www.acmicpc.net/problem/11726)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
const N = +require('fs').readFileSync('./11726.txt').toString();
const arr = new Array(N + 1).fill(1);

for (let i = 2; i <= N; i++) {
  arr[i] = (arr[i - 1] + arr[i - 2]) % 10007;
}

console.log(arr[N]);
