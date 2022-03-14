"""
digit   -   nº of segments  -   real code
1       -   2               -   cf
7       -   3               -   acf
4       -   4               -   bcdf
2       -   5               -   acdeg       acdeg & cf = c      acdeg & bcdf = cd       
3       -   5               -   acdfg       acdfg & cf = cf          
5       -   5               -   abdfg       abdfg & cf = f      abdfg & bcdf = bdf      
0       -   6               -   abcefg      abcefg & cf = cf    abcefg & acdfg = acfg
6       -   6               -   abdefg      abdefg & cf = f
9       -   6               -   abcdfg      abcdfg & cf = cf    abcdfg & acdfg = acdfg
8       -   7               -   abcdefg
"""

from inspect import trace
from numpy import empty
from sympy import sec


def readInput(targetFile):
    file=open(targetFile,"r")
    inp=file.readlines()
    inp=[entry.strip("\n") for entry in inp]

    entries=[]
    for entry in inp:
        entry=entry.split("|")
        firstHalf=entry[0]
        secndHalf=entry[1]
        entry={"first":firstHalf.strip(" ").split(" "),"secnd":secndHalf.strip(" ").split(" ") }
        entry=sortEntry(entry)
        entries.append(entry)
    return entries

def identifyDigit(digit,sets):
    try:
        if len(digit)==2:
            return 1
        if len(digit)==3:
            return 7
        if len(digit)==4:
            return 4
        if len(digit)==7:
            return 8
        if len(digit)==5 and len(sets[1] & set(digit))==2:
            return 3
        if len(digit)==5 and len(sets[4] & set(digit))==2:
            return 2
        if len(digit)==5:
            return 5
        if len(digit)==6 and len(sets[1] & set(digit))==1:
            return 6
        if len(digit)==6 and len(sets[3] & set(digit))==5:
            return 9
        if len(digit)==6:
            return 0
    except:
        pass
    return None

def sortEntry(entry):
    for i in range(len(entry["first"])):
        entry["first"][i]="".join(sorted(entry["first"][i]))
    for i in range(len(entry["secnd"])):
        entry["secnd"][i]="".join(sorted(entry["secnd"][i]))
    return entry

def inicialSets():
    alphabet=set("abcdefg")
    dict={}

    for item in alphabet:
        dict[item]=alphabet
    return dict

def realSets():
    dict={}
    dict[0]=set("cf")
    dict[1]=set("cf")
    dict[2]=set("acdeg")
    dict[3]=set("acdfg")
    dict[4]=set("bcdf")
    dict[5]=set("abdfg")
    dict[6]=set("abdefg")
    dict[7]=set("acf")
    dict[8]=set("abcdefg")
    dict[9]=set("abcdfg")

    return dict

def computeAnswerPart1(input):
    sum=0
    for entry in input:
        first=entry["first"]
        secnd=entry["secnd"]

        for sample in secnd:
            if identifyDigit(sample,{}) != None:
                sum+=1
    return sum

def computeAnswerPart2(input):
    sum=0
    for entry in input:
        changedRef={}
        first=entry["first"]
        secnd=entry["secnd"]
    
        for i in range(3):
            for sample in first:
                digit=identifyDigit(sample,changedRef)
                if digit != None:
                    changedRef[digit]=set(sample)
        for key in changedRef.keys():
            changedRef[key]="".join(sorted("".join(changedRef[key])))
        
        wholeNumber=""
        for sample in secnd:
            for key in changedRef:
                if changedRef[key]==sample:
                    digit=key
                    wholeNumber+=str(digit)
        sum+=int(wholeNumber)
    return sum
    
if __name__=="__main__":
    input=readInput("8.txt")
    #print(input)
    ans=computeAnswerPart1(input)
    print(ans)
    ans=computeAnswerPart2(input)
    print(ans)