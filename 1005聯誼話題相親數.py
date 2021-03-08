# import sys

# inputNumber = int(sys.stdin.readline().strip('\n'))
# ans = []

# while inputNumber != 0:
        
#     numberList1 = [] # 因數list
#     numberList2 = [] 
#     # 判斷因數
#     for i in range(1, inputNumber + 1):
#         if inputNumber % i == 0:
#             numberList1.append(i)
    
#     numberList1.pop() # 去除自己的因數
#     print(numberList1) # 所有因數
    
#     numsum1 = 0
#     numsum2 = 0
#     for num1 in numberList1:
#         numsum1 = numsum1 + num1
#     print('{}因數總和: '.format(str(inputNumber)) + str(numsum1))
    
#     for j in range(1, numsum1 + 1):
#         if numsum1 % j == 0:
#             numberList2.append(j)
#     numberList2.pop() # 去除自己的因數
#     print('{}相愛數因數: '.format(str(numsum1)))
#     print(numberList2)

#     for num2 in numberList2:
#         numsum2 = numsum2 + num2
    
#     if inputNumber == numsum2:
#         ans.append(numsum1)
#     else:
#         ans.append('QQ')

#     inputNumber = int(sys.stdin.readline().strip('\n'))
# else:
#     for a in ans:
#         print(a)

# ------------縮減版------------ #
import sys

inputNumber = int(sys.stdin.readline().strip('\n'))
ans = []

while inputNumber != 0:
        
    numberList1 = [] # 因數list
    numberList2 = [] 
    # 判斷因數
    for i in range(1, inputNumber + 1):
        if inputNumber % i == 0:
            numberList1.append(i)
    
    numberList1.pop() # 去除自己的因數
    
    numsum1 = 0
    numsum2 = 0
    for num1 in numberList1:
        numsum1 = numsum1 + num1
    
    for j in range(1, numsum1 + 1):
        if numsum1 % j == 0:
            numberList2.append(j)
    numberList2.pop() # 去除自己的因數

    for num2 in numberList2:
        numsum2 = numsum2 + num2
    
    if inputNumber == numsum2:
        ans.append(numsum1)
    else:
        ans.append('QQ')

    inputNumber = int(sys.stdin.readline().strip('\n'))
else:
    for a in ans:
        print(a)
    