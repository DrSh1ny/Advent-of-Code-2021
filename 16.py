import math
from struct import pack
from numpy import mat
from tqdm import tqdm
from anytree import Node, RenderTree

def readInput(targetFile):
    file=open(targetFile,"r")
    input=file.readlines()
    input= input[0].strip("\n")
    return input

def translateHexToBin(hexaString):
    binString=""
    dict={'0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'}

    for letter in hexaString:
        binString+=dict[letter]
    return binString

def nextPacket(binaryString):
    if len(binaryString)<11:
        return None,binaryString
    
    version=int(binaryString[0:3],2)
    id=int(binaryString[3:6],2)
    lenghType=None
    length=None
    
    binaryString=binaryString[6:]

    if id==4:
        number=""
        while True:
            chunk=binaryString[0:5]
            number+=binaryString[1:5]
            binaryString=binaryString[5:]
            if chunk[0]=='0':
                break

        number=int(number,2)
        return Node((version,id,lenghType,length,number)),binaryString

    else:
        number=None
        lenghType=binaryString[0]
        binaryString=binaryString[1:]
        if lenghType=='0':
            length=int(binaryString[0:15],2)
            binaryString=binaryString[15:]
            childrenString=binaryString[0:length]
            thisNode=Node((version,id,0,length,number))
            while True:
                newChildren,childrenString=nextPacket(childrenString)
                if newChildren==None:
                    break
                newChildren.parent=thisNode
            return thisNode,binaryString[length:]

        elif lenghType=='1':
            length=int(binaryString[0:11],2)
            binaryString=binaryString[11:]
            childrenString=binaryString[0:]
            thisNode=Node((version,id,0,length,number))
            for i in range(length):
                newChildren,childrenString=nextPacket(childrenString)
                newChildren.parent=thisNode
            return thisNode,childrenString

def valueOfPacket(packet):
    if packet.name[1]==4:
        return packet.name[4]
    elif packet.name[1]==0:
        sum=0
        for desc in packet.children:
            sum+=valueOfPacket(desc)
        return sum
    elif packet.name[1]==1:
        sum=1
        for desc in packet.children:
            sum*=valueOfPacket(desc)
        return sum
    elif packet.name[1]==2:
        min=math.inf
        for desc in packet.children:
            val=valueOfPacket(desc)
            if val<min:
                min=val
        return min
    elif packet.name[1]==3:
        maxi=-math.inf
        for desc in packet.children:
            val=valueOfPacket(desc)
            if val>maxi:
                maxi=val
        return maxi
    elif packet.name[1]==5:
        if valueOfPacket(packet.children[0])>valueOfPacket(packet.children[1]):
            return 1
        else:
            return 0
    elif packet.name[1]==6:
        if valueOfPacket(packet.children[0])<valueOfPacket(packet.children[1]):
            return 1
        else:
            return 0
    elif packet.name[1]==7:
        if valueOfPacket(packet.children[0])==valueOfPacket(packet.children[1]):
            return 1
        else:
            return 0
    else:
        return "oops"

def computeAnswerPart1(input):
    binString=translateHexToBin(input)
    root,binString=nextPacket(binString)
    sum=root.name[0]
    for descendent in root.descendants:
        sum+=descendent.name[0]
    return sum
    
def computeAnswerPart2(input):
    binString=translateHexToBin(input)
    root,binString=nextPacket(binString)
    value=valueOfPacket(root)
    return value

if __name__=="__main__":
    input=readInput("16.txt")
    #print(input)
    ans=computeAnswerPart1(input)
    print(ans)
    ans=computeAnswerPart2(input)
    print(ans)