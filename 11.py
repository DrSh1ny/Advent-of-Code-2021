def readInput(targetFile):
    file=open(targetFile,"r")
    inp=file.readlines()
    inp=[list(entry.strip("\n")) for entry in inp]

    for i in range(len(inp)):
        for k in range(len(inp[i])):
            inp[i][k]=int(inp[i][k])
    return inp

def printMatrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem[0],end="")
        print()
    print("\n\n")

flashes=0
matrix=[]
def checkOctopus(x,y):
    global matrix,flashes
    if matrix[y][x][0]>=10 and matrix[y][x][1]==False:
        matrix[y][x][1]=True
        flashes+=1
        neighborsCord=[[-1,0],[1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
        for xx,yy in neighborsCord:
            if x+xx>=0 and x+xx<len(matrix[0]) and y+yy>=0 and y+yy<len(matrix):
                matrix[y+yy][x+xx][0]+=1
                checkOctopus(x+xx,y+yy)

def computeAnswerPart1(input):
    global matrix,flashes
    matrix=input
    steps=100
    for y in range(len(input)):
            for x in range(len(input[y])):
                matrix[y][x]=[matrix[y][x],False]

    for step in range(steps):
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                matrix[y][x][0]+=1
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                checkOctopus(x,y)
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x][1] == True:
                    matrix[y][x][0]=0
                    matrix[y][x][1]=False
                    
    return flashes

def computeAnswerPart2(input):
    global matrix,flashes
    matrix=input
    flashes=0
    steps=100
    for y in range(len(input)):
            for x in range(len(input[y])):
                matrix[y][x]=[matrix[y][x],False]

    steps=0
    while True:
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                matrix[y][x][0]+=1
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                checkOctopus(x,y)
        numberFlashes=0
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x][1] == True:
                    numberFlashes+=1
                    matrix[y][x][0]=0
                    matrix[y][x][1]=False
        if numberFlashes==len(matrix)*len(matrix[0]):
            return steps+1
        steps+=1
                    
    return None

if __name__=="__main__":
    input=readInput("11.txt")
    #print(input)
    ans=computeAnswerPart1(input)
    print(ans)
    input=readInput("11.txt")
    ans=computeAnswerPart2(input)
    print(ans)