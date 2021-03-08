# https://oj.lidemy.com/problem/1003
import sys
def solution():
    combineStr = ''
    finalStr = ''
    try:
        print('請輸入1個1-100之間的數字')
        n = int(sys.stdin.readline().strip('\n'))
        if 1 <= n <= 100:
            for i in range(0, n):
                line = sys.stdin.readline().strip('\n')
                if len(line) <= 100:
                    combineStr = combineStr + line
                else:
                    print('字串太長')
            combineStr = combineStr.lower() # 改為小寫
            print('合併字串: '+ combineStr)
            print(len(combineStr))
            print('請輸入一個數字, 在合併字串中最大值以內')
            m = int(sys.stdin.readline().strip('\n'))
            if 1 <= m <= len(combineStr):
                for j in range(0, m):
                    number = int(sys.stdin.readline().strip('\n'))
                    finalStr = finalStr + combineStr[number - 1]
                print(finalStr)
            else:
                print('沒進來m執行')
        else:
            print('數字錯誤, 請重新輸入')
    except Exception as e:
        print(e)

solution()

# ---------------- 縮減版 --------------- #
# import sys
# def solution():
#     combineStr = ''
#     finalStr = ''

#     n = int(sys.stdin.readline().strip('\n'))
#     if 1 <= n <= 100:
#         for i in range(0, n):
#             line = sys.stdin.readline().strip('\n')
#             if len(line) <= 100:
#                 combineStr = combineStr + line
#         combineStr = combineStr.lower() # 改為小寫
#         m = int(sys.stdin.readline().strip('\n'))
#         if 1 <= m <= len(combineStr):
#             for j in range(0, m):
#                 number = int(sys.stdin.readline().strip('\n'))
#                 finalStr = finalStr + combineStr[number - 1]
#             print(finalStr)

# solution()