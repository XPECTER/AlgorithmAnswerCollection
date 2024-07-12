// [백준11724](https://www.acmicpc.net/problem/11724)

// 백준 입력
// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// IDE 입력
// const inputs = require('fs')
//   .readFileSync('./11724.txt')
//   .toString()
//   .trim()
//   .split('\n');
//
// const [N, M] = inputs[0].split(' ').map(Number);
// const graph = Array.from({ length: N + 1 }, (v, i) => i);
//
// console.log(graph);
//
// for (let i = 1; i <= M; i++) {
//   const [node1, node2] = inputs[i].split(' ').map(Number);
//
//   if (node1 <= node2) {
//     graph[node2] = graph[node1];
//   } else {
//     graph[node1] = graph[node2];
//   }
// }
//
// console.log(graph);

const [N, M] = inputs.shift().split(' ').map(Number);
const visited = Array(N + 1).fill(false);
const graph = new Map();
let answer = 0;

for (let i = 0; i < N; i++) {
  graph.set(i + 1, []);
}

for (let i = 0; i < M; i++) {
  const [node1, node2] = inputs[i].split(' ').map(Number);

  graph.get(node1).push(node2);
  graph.get(node2).push(node1);
}

for (let i = 1; i <= N; i++) {
  if (visited[i]) {
    continue;
  }

  const stack = [i];
  while (stack.length !== 0) {
    const node = stack.pop();
    visited[node] = true;

    for (const nextNode of graph.get(node)) {
      if (!visited[nextNode]) {
        stack.push(nextNode);
      }
    }
  }

  answer++;
}

console.log(answer);
