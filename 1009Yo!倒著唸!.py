# https://oj.lidemy.com/problem/1009
import sys 

string = sys.stdin.readline().strip('\n')

ans = ''

stringList = list(string)
stringList.reverse()
print(ans.join(stringList))