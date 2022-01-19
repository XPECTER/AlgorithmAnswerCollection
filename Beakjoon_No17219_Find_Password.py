# https://www.acmicpc.net/problem/17219
# time : 264 ms

import sys

N, M = map(int, sys.stdin.readline().split())
dic = {site: pw for site, pw in [sys.stdin.readline().split() for _ in range(N)]}
site_list = [sys.stdin.readline().rstrip() for _ in range(M)]
sys.stdout.write('\n'.join(dic.get(site) for site in site_list))


# very fastest solution
# sinput = sys.stdin.readline
# sprint = sys.stdout.write
#
# N, M = map(int, sinput().split())
# input_list = sys.stdin.read().splitlines()
#
# sites = dict(inputs.rstrip().split() for inputs in input_list[:N])
# questions = input_list[N:]
#
# sprint('\n'.join(sites.get(quest) for quest in questions))
