import sys
from collections import defaultdict
input = sys.stdin.readline

vertexs, edges = map(int, input().split())

for _ in range(edges):
    a, b, c = map(int, input().split())