# https://oj.lidemy.com/problem/1006
# import sys

# print('請輸入總座位數')
# totalSeat = int(sys.stdin.readline()) # 總座位數
# print('請輸入被座走的座位數')
# blockSeat = int(sys.stdin.readline()) # 被座走的座位數

# rows = int(totalSeat / 2)
# columns = 2 # 預設為雙排

# if totalSeat % 2 == 0 and 2 <= totalSeat <= 30:
#     print('輸入為偶數個座位')
    
# # 全部座位座標
# allSeatList = [] 
# index = 0
# for row in range(rows, 0, -1):
#     for col in range(1, columns + 1):
#         index = index + 1 # 編號
#         point = [col, row]
#         allSeatList.append({'seatNumber' : index, 'point' : point})

# print(allSeatList)

# # 減去被擋住的編號
# print('請輸入被人坐走的座位編號')
# for i in range(0, blockSeat):
#     blockSeatNumber = int(sys.stdin.readline())
#     allSeatList.pop(blockSeatNumber - 1 - i)

# print(allSeatList)

# # 兩個對坐的座位集合
# index = 0
# ans = []
# for row in allSeatList:
#     index = index + 1
#     currentPoint = row['point']    
#     for pi in allSeatList[index:]:
#         ansPoint = [currentPoint[z] - pi['point'][z] for z in range(len(currentPoint))]
#         if ansPoint[0] == 0 and abs(ansPoint[1]) == 1:
#             ans.append({'小明':row['seatNumber'], '小花': pi['seatNumber'], 'ans':ansPoint})
#         elif ansPoint[1] == 0 and abs(ansPoint[0]) == 1:
#             ans.append({'小明':row['seatNumber'], '小花': pi['seatNumber'], 'ans':ansPoint})            

# ansNumber = len(ans)
# print('總排列組合數目' + str(ansNumber))
# print(ans)

# ----------------縮減版---------------- #
import sys

N = int(sys.stdin.readline().strip('\n')) # 總座位數
M = int(sys.stdin.readline().strip('\n')) # 被座走的座位數

rows = int(N / 2)
columns = 2 # 預設為雙排

if N % 2 == 0 and 2 <= N <= 30:
    if 0 <= M <= N:
        # 全部座位座標
        allSeatList = [] 
        index = 0
        for row in range(rows, 0, -1):
            for col in range(1, columns + 1):
                index = index + 1 # 編號
                point = [col, row]
                allSeatList.append({'seatNumber' : index, 'point' : point})

        # 減去被擋住的編號
        for i in range(0, M):
            blockSeatNumber = int(sys.stdin.readline().strip('\n'))
            allSeatList.pop(blockSeatNumber - 1 - i)

        # 兩個對坐的座位集合
        index = 0
        ans = []
        for row in allSeatList:
            index = index + 1
            currentPoint = row['point']    
            for pi in allSeatList[index:]:
                ansPoint = [currentPoint[z] - pi['point'][z] for z in range(len(currentPoint))]
                if ansPoint[0] == 0 and abs(ansPoint[1]) == 1:
                    ans.append({'小明':row['seatNumber'], '小花': pi['seatNumber'], 'ans':ansPoint})
                elif ansPoint[1] == 0 and abs(ansPoint[0]) == 1:
                    ans.append({'小明':row['seatNumber'], '小花': pi['seatNumber'], 'ans':ansPoint})            

        ansNumber = len(ans)
        print(ansNumber)