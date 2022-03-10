from typing import final
from matplotlib.container import BarContainer
from sklearn import impute
from sympy import li


class Board:
    def __init__(self, boardNumbers):
        
        self.lastCalled=None
        
        board=[]
        for i in boardNumbers:
            row=[]
            for j in i:
                row.append([j,False])
            board.append(row)

        self.board=board


    def printBoard(self):
        for i in self.board:
            for j in i:
                print(j,end="\t")
            print()

    def checkRow(self,index):
        row=self.board[index]
        for i in row:
            if i[1]==False:
                return False
        return True

    def checkCol(self,index):
        for row in self.board:
            if row[index][1]==False:
                return False
        return True 
    
    def shoutNumber(self,number):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j][0]==number:
                    self.board[i][j][1]=True
                    self.lastCalled=number
                    if self.checkCol(j) or self.checkRow(i):
                        return True
        return False

    def computeAnswer(self):
        sumMarked=0
        sumUnmarked=0
        for i in self.board:
            for j in i:
                if j[1]==True:
                    sumMarked+=j[0]
                else:
                    sumUnmarked+=j[0]
        return sumUnmarked*self.lastCalled

def readInput(targetFile):
    file=open(targetFile,'r')
    lines=file.readlines()


    inputs=lines[0].strip("\n")
    inputs=inputs.split(",")
    inputs = map(int, inputs)

    boards=[]
    boardCurr=[]
    for line in lines[2:]:
        if line=='\n':
            boards.append(Board(boardCurr))
            boardCurr=[]
        else:
            line=line.strip("\n")
            line=line.split(" ")
            
            try:
                while True:
                    line.remove('')
            except ValueError:
                pass

            line = map(int, line)
            boardCurr.append(line)
    boards.append(Board(boardCurr))

    return boards,inputs

def part1(boards,inputs):
    for inp in inputs:
        for board in boards:
            res=board.shoutNumber(inp)
            if res==True:
                ans=board.computeAnswer()
                return ans

def part2(boards,inputs):
    lastWinner=0
    indexBo=0

    for inp in inputs:
        indexBo=0
        if boards==[]:
            return lastWinner
        while indexBo<len(boards):
            res=boards[indexBo].shoutNumber(inp)
            if res==True:
                ans=boards[indexBo].computeAnswer()
                lastWinner=ans
                del boards[indexBo]
                indexBo-=1
            indexBo+=1
    return lastWinner

if __name__=="__main__":
    boards,inputs=readInput("1.txt")
    print(part1(boards,inputs))
    boards,inputs=readInput("1.txt")
    print(part2(boards,inputs))
                