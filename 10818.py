import os

N = input()
L = list(map(int, os.sys.stdin.readline().split()))
L.sort()
print(L[0], L[-1])
