def readInput(targetFile):
    file=open(targetFile,"r")
    inp=file.readlines()
    inp=inp[0].strip("\n").split(",")
    inp = list(map(int, inp))
    return inp
    
def computeAnswerPart1(input):
    return None

if __name__=="__main__":
    pass