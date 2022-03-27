import math
from numpy import matrix
from tqdm import tqdm

def readInput(targetFile):
    file=open(targetFile,"r")
    input=file.readlines()
    matrix=[[int(value) for value in line.strip("\n")] for line in input]
    return matrix
    
def printMatrix(matrix):
    for row in matrix:
        for elem in row:
                print(elem,end=" ")
        print()

def printMatrix(matrix):
    for row in matrix:
        for elem in row:
                print(elem,end=" ")
        print()

def parseMatrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            risk=matrix[y][x]
            visited=False
            currentCost=math.inf
            parent=None
            neighbors=[[-1,0],[1,0],[0,1],[0,-1]]
            validNeighbors=[]
            for neighbor in neighbors:
                if x+neighbor[0]>=0 and x+neighbor[0]<len(matrix[y]) and y+neighbor[1]>=0 and y+neighbor[1]<len(matrix):
                    xx=x+neighbor[0]
                    yy=y+neighbor[1]
                    validNeighbors.append([xx,yy])
            if x==0 and y==0:
                currentCost=0

            matrix[y][x]={"risk":risk,"visited":visited,"currentCost":currentCost,"parent":parent,'adjacent':validNeighbors}
    return matrix

def dijkstra(matrix):
    current=[0,0]
    unvisited=[]
    while(1):
        if current[1]==len(matrix)-1 and current[0]==len(matrix[current[1]])-1:
            return matrix 
        x=current[0]
        y=current[1]
        matrix[y][x]['visited']=True

        for adjacent in matrix[y][x]['adjacent']:
            xx=adjacent[0]
            yy=adjacent[1]
            if matrix[yy][xx]['visited']==True:
                continue
            cost=matrix[y][x]['currentCost']+matrix[yy][xx]['risk']
            if cost < matrix[yy][xx]['currentCost']:
                matrix[yy][xx]['parent']=[x,y]
                matrix[yy][xx]['currentCost']=cost
                unvisited.append([[xx,yy],cost])
        unvisited.sort(key=lambda x: x[1])
        current=unvisited[0][0]
        del unvisited[0]
    return matrix

def computeAnswerPart1(input):
    matrix=parseMatrix(input)
    matrix=dijkstra(matrix)
    
    path=[[len(matrix[len(matrix)-1])-1,len(matrix)-1]]
    while path[-1]!=[0,0]:
        x=path[-1][0]
        y=path[-1][1]
        path.append(matrix[y][x]['parent'])

    sum=0
    for elem in path:
        x=elem[0]
        y=elem[1]

        sum+=matrix[y][x]['risk']
    return sum-matrix[0][0]['risk']

def computeAnswerPart2(input):
    for y in range(len(input)):
        comp=len(input[y])
        for i in range(4):
            for x in range(comp):
                value=input[y][x]
                newValue=((value-1+(i+1))%9)+1
                input[y].append(newValue)
    
    comp=len(input)
    for i in range(4):
        for y in range(comp):
            row=[]
            for x in range(len(input[y])):
                value=input[y][x]
                newValue=((value-1+(i+1))%9)+1
                row.append(newValue)
            input.append(row) 
    matrix=parseMatrix(input)
    matrix=dijkstra(matrix)
    
    path=[[len(matrix[len(matrix)-1])-1,len(matrix)-1]]
    while path[-1]!=[0,0]:
        x=path[-1][0]
        y=path[-1][1]
        path.append(matrix[y][x]['parent'])

    sum=0
    for elem in path:
        x=elem[0]
        y=elem[1]

        sum+=matrix[y][x]['risk']
    return sum-matrix[0][0]['risk']

if __name__=="__main__":
    input=readInput("15.txt")
    #print(input)
    ans=computeAnswerPart1(input)
    print(ans)
    input=readInput("15.txt")
    ans=computeAnswerPart2(input)
    print(ans)