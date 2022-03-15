from sklearn import neighbors
from sqlalchemy import false


def readInput(targetFile):
    file=open(targetFile,"r")
    inp=file.readlines()
    inp=[list(entry.strip("\n")) for entry in inp]
    inp=[[int(i) for i in k]  for k in inp] 
    return inp

def checkMinimum(matrix,x,y):
    number=matrix[y][x]
    neighborsCord=[[-1,0],[1,0],[0,1],[0,-1]]
    for xx,yy in neighborsCord:
        if x+xx>=0 and x+xx<len(matrix[0]) and y+yy>=0 and y+yy<len(matrix) and matrix[y+yy][x+xx]<=number:
            return False
    return True

basins={}
seen=[]
def spreadBasin(matrix,x,y,basin):
    number=matrix[y][x]
    neighborsCord=[[-1,0],[1,0],[0,1],[0,-1]]
    if number<9 and [x,y] not in seen:
        basins[basin]=basins.get(basin,0)+1
        seen.append([x,y])
        for xx,yy in neighborsCord:
            if x+xx>=0 and x+xx<len(matrix[0]) and y+yy>=0 and y+yy<len(matrix) and matrix[y+yy][x+xx]<9:
                spreadBasin(matrix,x+xx,y+yy,basin)

def computeAnswerPart1(input):
    sum=0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if checkMinimum(input,x,y):
                risk=1+input[y][x]
                sum+=risk
    return sum

def computeAnswerPart2(input):
    for y in range(len(input)):
        for x in range(len(input[y])):
            if checkMinimum(input,x,y):
                spreadBasin(input,x,y,(x,y))
    all=[]
    for key in basins:
        all.append(basins[key])
    all.sort(reverse=True)
    return all[0]*all[1]*all[2]

    
if __name__=="__main__":
    input=readInput("test.txt")
    #print(input)
    ans=computeAnswerPart1(input)
    print(ans)
    ans=computeAnswerPart2(input)
    print(ans)