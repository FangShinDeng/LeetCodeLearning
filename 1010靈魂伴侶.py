import sys

ABList = sys.stdin.readline().split(' ')
A = int(ABList[0])
B = int(ABList[1])
if 1 <= A and B <= 2**31 -1:
  if A == B:
    print('Yes')
  else:
    print('No')