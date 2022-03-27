from operator import index, le
from tkinter.messagebox import NO
from sympy import octave_code
from tqdm import tqdm

def readInput(targetFile):
    file=open(targetFile,"r")
    input=file.readlines()

    template=list(input[0].strip('\n'))
    rules={}
    for i in range(2,len(input)):
        rule=input[i]
        rule=rule.strip('\n').split(" -> ")
        rules[rule[0]]=rule[1]
    return template,rules

def displayTemplate(template):
    text=""
    for letter in template:
        text+=letter
    print(text)

def applyRules(template,rules):
    newTemplate=[]
    newTemplate.append(template[0])
    for i in range(1,len(template)):
        word=template[i-1]+template[i]
        match=rules.get(word,None)

        if match!=None:
            newTemplate.append(match)
        newTemplate.append(template[i])
        
    return newTemplate  

def applyRules2(indexes,rules):
    newIndexes={}
    #print(indexes)
    for rule in rules.keys():
        occurr=indexes.pop(rule, None)
        newWord1=rule[0]+rules[rule]
        newWord2=rules[rule]+rule[1]
        if occurr!=None:
            newIndexes[newWord1]=newIndexes.get(newWord1,0)+occurr
            newIndexes[newWord2]=newIndexes.get(newWord2,0)+occurr
    #print(newIndexes)
    return newIndexes

def desintegrateTemplate(template):
    indexes={}
    for i in range(1,len(template)):
        word=template[i-1]+template[i]
        indexes[word]=indexes.get(word,0)+1
    return indexes

def computeAnswerPart1(template,rules):
    steps=10
    ocorr={}
    for i in range(steps):
        #displayTemplate(template)
        template=applyRules(template,rules)

    for letter in template:
        ocorr[letter]=ocorr.get(letter,0)+1
    return ocorr

def computeAnswerPart2(template,rules):
    steps=40
    ocorr={}
    indexes=desintegrateTemplate(template)
    for i in range(steps):
        indexes=applyRules2(indexes,rules)

    ocorr[template[0]]=1
    highest=0
    lowest=0
    for word in indexes.keys():
        letter2=word[1]
        ocorr[letter2]=ocorr.get(letter2,0)+indexes[word]
    
    sorted=[]
    for letter in ocorr.keys():
        sorted.append(ocorr[letter])
    sorted.sort()
    return sorted

if __name__=="__main__":
    input=readInput("14.txt")
    #print(input)
    ans=computeAnswerPart1(*input)
    print(ans)
    ans=computeAnswerPart2(*input)
    print(ans)
    
    