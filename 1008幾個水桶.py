# https://oj.lidemy.com/problem/1008
import sys

M = int(sys.stdin.readline())
bucketNumber = 0            
def findMaxPow(number):
    for i in range(1,32):
        if 2 ** i > number:
            return i - 1
            break

for j in range(1,99):
    if M != 0:
        maxBucket = findMaxPow(M)
        M = M - 2**maxBucket
        bucketNumber = j

print(bucketNumber)        