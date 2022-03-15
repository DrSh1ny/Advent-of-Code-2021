from queue import LifoQueue
import queue
from statistics import median

from numpy import mat

def readInput(targetFile):
    file=open(targetFile,"r")
    inp=file.readlines()
    inp=[entry.strip("\n") for entry in inp] 
    return inp

def incorrectScore(braket):
    if braket==")":
        return 3
    elif braket=="]":
        return 57
    elif braket=="}":
        return 1197
    elif braket==">":
        return 25137
    return None

def incompleteScore(braket):
    if braket==")":
        return 1
    elif braket=="]":
        return 2
    elif braket=="}":
        return 3
    elif braket==">":
        return 4
    return None

def isClose(braket):
    if braket in ["]",")",">","}"]:
        return True
    return False

def isMatch(braketOpen,braketClose):
    pairs=[["[","]"],["(",")"],["{","}"],["<",">"]]
    if [braketOpen,braketClose] in pairs:
        return True
    return False

def getMatch(braketOpen):
    pairs=[["[","]"],["(",")"],["{","}"],["<",">"]]
    for pair in pairs:
        if braketOpen in pair:
            return pair
    return None

def computeAnswerPart1(input):
    sum=0
    for entry in input:
        stack = LifoQueue(maxsize=100)
        for i,braket in enumerate(entry):
            if isClose(braket):
                match=stack.get()
                if not isMatch(match,braket):
                    sum+=incorrectScore(braket)
                    break
            else:
                stack.put(braket)
    return sum

def computeAnswerPart2(input):
    k=0
    while k<len(input):
        stack = LifoQueue(maxsize=100)
        for i,braket in enumerate(input[k]):
            if isClose(braket):
                match=stack.get()
                if not isMatch(match,braket):
                    del input[k]
                    k-=1
                    break
            else:
                stack.put(braket)
        k+=1
    
    scores=[]
    for entry in input:
        stack = LifoQueue(maxsize=100)
        for i,braket in enumerate(entry):
            if isClose(braket):
                match=stack.get()
            else:
                stack.put(braket)

        endMissing=[]
        score=0
        while not stack.empty():
            openBr=stack.get()
            match=getMatch(openBr)[1]
            endMissing.append(match)

        for miss in endMissing:
            score*=5
            score+=incompleteScore(miss)
        scores.append(score)
    scores.sort()
    return median(scores)

if __name__=="__main__":
    input=readInput("10.txt")
    #print(input)
    ans=computeAnswerPart1(input)
    print(ans)
    ans=computeAnswerPart2(input)
    print(ans)