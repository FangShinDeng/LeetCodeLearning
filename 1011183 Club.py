import sys
M = int(sys.stdin.readline())
avg = 0
if 1 <= M <= 20:
    teamList = sys.stdin.readline().split(' ')
    if M == len(teamList):
        heightList = []
        for person in teamList:
            if 100 <= int(person) <= 200:
                heightList.append(int(person))
        
        avg = sum(heightList)/len(heightList)      
                
        if avg >= 183:
            print('real')
        else:
            print('fake')
    else:
        print(False)