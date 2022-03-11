from statistics import mean, median


def readInput(targetFile):
    file=open(targetFile,"r")
    inp=file.readlines()
    inp=inp[0].strip("\n").split(",")
    inp = list(map(int, inp))
    return inp
    
def computeAnswerPart1(input):
    centroid=round(median(input))
    fuel=0
    for crab in input:
        fuel+=abs(crab-centroid)
    return centroid,fuel

def computeCostFuel(input,centroid):
    fuel=0
    for crab in input:
        dist=abs(crab-centroid)
        cost=round(dist*(dist+1)/2)
        fuel+=cost
    return fuel

def computeAnswerPart2(input):
    lastCentroid=None
    costLastCentroid=None
    for centroid in range(min(input),max(input)+1):
        cost=computeCostFuel(input,centroid)
        if costLastCentroid==None or  costLastCentroid>=cost:
            lastCentroid=centroid
            costLastCentroid=cost
    return lastCentroid,costLastCentroid


if __name__=="__main__":
    input=readInput("7.txt")
    print(input)
    ans=computeAnswerPart1(input)
    print(ans)
    ans=computeAnswerPart2(input)
    print(ans)