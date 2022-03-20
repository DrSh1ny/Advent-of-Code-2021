import math

from attr import fields_dict

def readInput(targetFile):
    file=open(targetFile,"r")
    inp=file.readlines()
    seperation=0
    for i,entry in enumerate(inp):
        if entry=="\n":
            seperation=i
            break
    
    board=inp[0:seperation]
    commands=inp[seperation+1:]
    maxY=0
    maxX=0
    for i,entry in enumerate(board):
        entry=entry.strip("\n")
        entry=entry.split(",")
        entry=[int(value) for value in entry]
        board[i]=entry

        if entry[0]>maxX:
            maxX=entry[0]
        if entry[1]>maxY:
            maxY=entry[1]
    
    for i,entry in enumerate(commands):
        entry=entry.strip("\n")
        entry=entry.split("=")
        entry=[entry[0][-1],int(entry[1])]
        commands[i]=entry

    field=[[0 for i in range(maxX+1)] for j in range(maxY+1)]
    for entry in board:
        field[entry[1]][entry[0]]=1

    return field,commands

def printMatrix(matrix):
    for row in matrix:
        for elem in row:
            if elem==1:
                print('x',end="")
            else:
                print(' ',end="")
        print()
    print("\n\n")

def mergeTwo(field1,field2):
    while(len(field2)<len(field1)):
            field2.insert(0,[0 for i in range(len(field1[0]))])
    for i,entry in enumerate(field1):
        while(len(field2[i])<len(field1[i])):
            field2[i].insert(0,0)

    for y in range(len(field1)):
        for x in range(len(field1[y])):
            try:
                field1[y][x]= field1[y][x] | field2[y][x]
            except:
                field1[y][x]= field1[y][x]
    return field1

def verticalFold(field,axis):
    up=[]
    down=[]
    for i,entry in enumerate(field):
        if i<axis:
            up.append(entry)
        elif i>axis:
            down.append(entry)
    down.reverse()
    return up,down

def horizontalFold(field,axis):
    left=[]
    right=[]
    for i,entry in enumerate(field):
        rowLeft=[]
        rowRight=[]
        for j,value in enumerate(entry): 
            if j<axis:
                rowLeft.append(value)
            elif j>axis:
                rowRight.append(value)
        rowRight.reverse()
        left.append(rowLeft)
        right.append(rowRight)
    return left,right

def computeNumberDots(field):
    sum=0
    for entry in field:
        for value in entry:
            sum+=value
    return sum

def computeAnswerPart1(field,commands):
    axis=commands[0][0]
    if axis=="x":
        field1,field2=horizontalFold(field,commands[0][1])
    else:
        field1,field2=verticalFold(field,commands[0][1])

    field=mergeTwo(field1,field2)
        
    return computeNumberDots(field)

def computeAnswerPart2(field,commands):
    for command in commands:
        axis=command[0]
        if axis=="x":
            field1,field2=horizontalFold(field,command[1])
        else:
            field1,field2=verticalFold(field,command[1])

        field=mergeTwo(field1,field2)

    return field

if __name__=="__main__":
    
    field,commands=readInput("13.txt")
    #print((field,commands))
    ans=computeAnswerPart1(field,commands)
    print(ans)
    field=computeAnswerPart2(field,commands)
    printMatrix(field)
    
    