

def readInput(targetFile):
    file=open(targetFile,"r")
    inp=file.readlines()
    inp=[entry.strip("\n").split("-") for entry in inp]

    return inp

def computeNeighborsDictionary(input):
    dict={}
    for entry in input:
        a=entry[0]
        b=entry[1]
        dict[a]=dict.get(a,list())+[b]
        dict[b]=dict.get(b,list())+[a]
       
    return dict

def isNeighbor(neighbors,vertexSource,vertexTarget):
    if vertexTarget in neighbors[vertexSource]:
        return True
    else:
        return False
def displayPaths(paths):
    prettyPaths=""
    for path in paths:
        for vertex in path:
            if vertex==path[-1]:
                prettyPaths+=vertex+"\n"
            else:
                prettyPaths+=vertex+","
    return prettyPaths

neighbors={}
vertices={}
paths=[]
def computePath(path,possibleVertices):
    global neighbors,vertices
    if path[-1]=='end':
        if path not in paths:
            paths.append(path)
        return
    if len(possibleVertices)==0:
        return

    for vertex in possibleVertices:
        if isNeighbor(neighbors,path[-1],vertex):
            newPath=path[:]
            newPath.append(vertex)
            if vertex.isupper()==False:
                newPossibleVertices=possibleVertices.copy()
                newPossibleVertices.remove(vertex)
                computePath(newPath,newPossibleVertices)
            else:
                computePath(newPath,possibleVertices)
    return


def computePathRepetition(path,possibleVertices,isRepeated):
    global neighbors,vertices
    if path[-1]=='end':
        if path not in paths:
            paths.append(path)
        return
    if len(possibleVertices)==0:
        return

    for vertex in possibleVertices:
        if isNeighbor(neighbors,path[-1],vertex):
            newPath=path[:]
            newPath.append(vertex)
            if vertex.isupper()==False:
                newPossibleVertices=possibleVertices.copy()
                newPossibleVertices.remove(vertex)
                computePathRepetition(newPath,newPossibleVertices,isRepeated)
                if isRepeated==False:
                    computePathRepetition(newPath,possibleVertices,True)
            else:
                computePathRepetition(newPath,possibleVertices,isRepeated)
    return


def computeAnswerPart1(input):
    global neighbors,vertices
    neighbors=computeNeighborsDictionary(input)
    vertices=[key for key in neighbors.keys()]
    possibleVert=vertices.copy()
    possibleVert.remove('start')
    computePath(['start'],possibleVert)

    prettyPaths=displayPaths(paths)
    return len(paths)

def computeAnswerPart2(input):
    global neighbors,vertices
    neighbors=computeNeighborsDictionary(input)
    vertices=[key for key in neighbors.keys()]
    possibleVert=vertices.copy()
    possibleVert.remove('start')
    computePathRepetition(['start'],possibleVert,False)

    prettyPaths=displayPaths(paths)
    return len(paths)

if __name__=="__main__":
    input=readInput("12.txt")
    #print(input)
    ans=computeAnswerPart1(input)
    print(ans)
    ans=computeAnswerPart2(input)
    print(ans)