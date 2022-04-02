
from matplotlib.pyplot import hist

class Target:
    def __init__(self,input):
        self.minX=input[0]
        self.maxX=input[1]
        self.minY=input[2]
        self.maxY=input[3]

    def hit(self,point):
        if point.x>=self.minX and point.x<=self.maxX and point.y>=self.minY and point.y<=self.maxY:
            return True
        return False

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
class Missile:
    def __init__(self,x,y,velX,velY):
        self.x=x
        self.y=y
        self.velX=velX
        self.velY=velY

        self.history=[Point(self.x, self.y)]
    
    def nextStep(self):
        self.x+=self.velX
        self.y+=self.velY

        self.velY-=1
        if self.velX>0:
            self.velX-=1
        elif self.velX<0:
            self.velX+=1
        
        self.history.append(Point(self.x,self.y))

    def printHistory(self,target):
        print("x\ty")
        for point in self.history:
            print("{}\t{}".format(point.x,point.y),end="\n")
        print("\n\n")
        
    def highest(self):
        maxY=0
        for point in self.history:
            if point.y>maxY:
                maxY=point.y
        return maxY

def readInput(targetFile):
    file=open(targetFile,"r")
    input=file.readlines()
    input= input[0].strip("\n")

    input = input.replace('target area: x=','')
    input = input.replace(' y=','')

    input=input.split(",")
    input[0]=input[0].split("..")
    input[1]=input[1].split("..")
    coord=[]
    for elem in input:
        for cor in elem:
            coord.append(int(cor))
    return coord

def computeAnswerPart1(input):
    target=Target(input)

    upperVelX=200
    upperVelY=200
    lowerVelX=-200
    lowerVelY=-200

    maxY=0
    velBestX=0
    velBestY=0
    for velX in range(lowerVelX,upperVelX):
        for velY in range(lowerVelY,upperVelY):
            missile=Missile(0, 0, velX, velY)

            while missile.y>=target.minY:
                missile.nextStep()
                if missile.velX<=0 and missile.x<target.minX:
                    break
                if target.hit(missile):
                    if missile.highest()>maxY:
                        maxY=missile.highest()
                        velBestX=velX
                        velBestY=velY 
                    break       
    return maxY
    
def computeAnswerPart2(input):
    target=Target(input)

    upperVelX=350
    upperVelY=350
    lowerVelX=-350
    lowerVelY=-350

    count=0
    for velX in range(lowerVelX,upperVelX):
        for velY in range(lowerVelY,upperVelY):
            missile=Missile(0, 0, velX, velY)

            while missile.y>=target.minY:
                missile.nextStep()
                if missile.velX<=0 and missile.x<target.minX:
                    break
                if target.hit(missile):
                    count+=1
                    break     
    return count

if __name__=="__main__":
    input=readInput("17.txt")
    #print(input)
    ans=computeAnswerPart1(input)
    print(ans)
    ans=computeAnswerPart2(input)
    print(ans)