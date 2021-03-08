# https://oj.lidemy.com/problem/1007
import sys

M = int(sys.stdin.readline())

personScoreList = []
personNameList = []
if 1 <= M <= 50:
    for i in range(0, M):
        person = sys.stdin.readline().split(' ')
        personNameList.append(person[0])
        personScoreList.append(int(person[1]))
        # print(person)
    mvpIndexList = [j for j,v in enumerate(personScoreList) if v == max(personScoreList)]
    # print(mvpIndexList)    
    for index in mvpIndexList:        
        print(personNameList[index])
