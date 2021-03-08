import sys

raceNumber = int(sys.stdin.readline().strip('\n'))
ans = []
if 1 <= raceNumber <= 50:
    for i in range(0, raceNumber):
        raceList = sys.stdin.readline().split(' ')
        A = int(raceList[0])
        B = int(raceList[1])
        BigSmall = int(raceList[2].strip('\n'))

        if BigSmall == 1:
            if A > B:
                ans.append('A')
            elif A == B:
                ans.append('DRAW')
            else:
                ans.append('B')
        if BigSmall == -1:
            if A < B:
                ans.append('A')
            elif A == B:
                ans.append('DRAW')
            else:
                ans.append('B')
    
    for a in ans:
        print(a)