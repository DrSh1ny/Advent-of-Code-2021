


from numpy import sign
from pyrsistent import inc


def readInput(targetFile):
    file=open(targetFile,'r')
    lines=file.readlines()
    
    inputs=[]
    for line in lines:
        line=line.strip("\n")
        line=line.replace("->"," ")
        line=line.replace(","," ")
        line=line.split(" ")
        try:
            while(True):
                line.remove('')
        except:
            pass
        
        for i in range(len(line)):
            line[i]=int(line[i])

        inputs.append(line)
    return inputs

def computeAnswer(inputs):
    dic={}
    for line in inputs:
        incX=line[2]-line[0]
        incY=line[3]-line[1]
        
        if incY==0 and incX!=0:
            lista=[(line[0]+i*incX/abs(incX),line[1]) for i in range(abs(incX)+1)]
        elif incX==0 and incY!=0:
            lista=[(line[0],line[1]+i*incY/abs(incY)) for i in range(abs(incY)+1)]
        else:
            continue
        for pair in lista:
            dic[pair]=dic.get(pair,0)+1
    
    answer=0
    for key,value in dic.items():
        if value>=2:
            answer+=1
    return answer


def computeAnswerPart2(inputs):
    dic={}
    for line in inputs:
        incX=line[2]-line[0]
        incY=line[3]-line[1]
        
        try:
            signalX=incX/abs(incX)
        except:
            signalX=0
        
        try:
            signalY=incY/abs(incY)
        except:
            signalY=0

        lista=[(line[0]+i*signalX,line[1]+i*signalY) for i in range(max(abs(incX),abs(incY))+1)]
        for pair in lista:
            dic[pair]=dic.get(pair,0)+1
    
    answer=0
    for key,value in dic.items():
        if value>=2:
            answer+=1
    return answer


if __name__=="__main__":
    inp=readInput("test.txt")
    ans=computeAnswer(inp)
    print(ans)
    ans=computeAnswerPart2(inp)
    print(ans)