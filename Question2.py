import sys

# line = sys.stdin.readline()

ContainerList = [1,8,6,2,5,4,8,3,7]
ContainerList = [1,1]
def MaxContainer(ContainerList:list):

    Area = 0
    AreaList = []
    i = 0
    for y1 in ContainerList:
        i = i + 1
        j = 0
        for y2 in ContainerList[i:]:
            j = j + 1
            x1 = ContainerList.index(y1) + 1
            x2 = x1 + j
            Area = (x2 - x1)*(min(y2,y1))
            AreaList.append(Area)
            print("x1: " + str(x1), "y1: " + str(y1) , "x2: " + str(x2), "y2: " + str(y2))
            
    print(max(AreaList))
    return(max(AreaList))
    
MaxContainer(ContainerList)