import math
from functools import lru_cache

def readInput(targetFile):
    file=open(targetFile,"r")
    inp=file.readlines()
    inp=inp[0].strip("\n").split(",")
    inp = list(map(int, inp))
    return inp
    
def computeAnswerPart1(input,days):
    fish=input.copy()
    for day in range(days):
        currSize=len(fish)
        for i in range(currSize):
            if fish[i]==0:
                fish[i]=6
                fish.append(8)
            else:
                fish[i]-=1

    return len(fish)    

@lru_cache(maxsize = 100000)
def computeSonsFish(maturity,daysLeft):
    pass
    if maturity>=daysLeft:
        return 1
    else:
        totalSons=2
        daysLeft=daysLeft-maturity-1
        for k in range(math.floor((daysLeft)/7)):
            totalSons+=computeSonsFish(8,daysLeft-(k)*7)
        return totalSons

def computeAnswerPart2(input,days):
    totalFish=0
    for i in range(len(input)):
        ans=computeSonsFish(input[i],days)
        totalFish+=ans
        #print([input[i],days,ans])

    return totalFish
        
if __name__=="__main__":
    input=readInput("6.txt")
    ans=computeAnswerPart1(input,80)
    print(ans)
    ans=computeAnswerPart2(input,256)
    print(ans)