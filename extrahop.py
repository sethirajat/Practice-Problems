
import urllib
from bs4 import BeautifulSoup
import re

def findnextcoords(curr_coord):
    #print "current coord are: ", curr_coord

    global legal_moves
    next_coords = []
    x = 0
    y = 0
    for coord in legal_moves:
        x = curr_coord[0] + coord[0]
        y = curr_coord[1] + coord[1]
        if x >= 0 and x <= 7 and y >=0 and y <= 7:
            next_coords.append((x,y))

    return next_coords

def inputmatrix(filenm):
    fileM = open(filenm, 'r')
    matrix = [[0 for x in range(8)]for y in range(8)]
    global startingpoints
    y = 0
    for line in fileM:
        if y > 7:
            raise Exception("y greater than 7")
        x=0
        for char in line.split():
            lowchar = char.lower()
            if x > 7:
                raise Exception("x greater than 7")
            matrix[y][x] = lowchar
            if lowchar in startingpoints:
                coordlist = startingpoints[lowchar]
                coordlist.append((y,x))
                startingpoints[lowchar] = coordlist
            else:
                tup = []
                tup.append((y,x))
                startingpoints[lowchar] = tup
            x += 1
        y += 1

    fileM.close()
    return matrix
'''
def returnpossible(coords,char,matrix):
    possibles = []
    for coord in coords:
        nextcoords = findnextcoords(coord)
        for nextcoord in nextcoords:
            if matrix[nextcoord[1]][nextcoord[2]] == char:
                possibles.append(nextcoord)

    return possibles
'''


def possible_cords(coordlist1, coordlist2):
    possib_cords = []
    for coord1 in coordlist1:
        nextcoords = findnextcoords(coord1)
        for coord2 in coordlist2:
            if coord2 in nextcoords:
                possib_cords.append(coord2)
                coordlist2.remove(coord2)

    return possib_cords



def checkword(word,currentpos,current_coords = []):
    if currentpos >= len(word):
        return 1
    global startingpoints
    curr_char = word[currentpos]
    if curr_char not in startingpoints:
        return 0
    char_coords = startingpoints[curr_char]
    #print "the coords from startingpoints are: ", char_coords
    if currentpos == 0:
        return checkword(word,currentpos+1,char_coords)
    else:
        #print "the coords passed to the fun are: ", current_coords
        next_coords = possible_cords(current_coords[:],char_coords[:])
        if len(next_coords) == 0:
            return 0
        else:
            return checkword(word,currentpos+1,next_coords)

def matchwords():
    matches = []
    global wordlist
    for word in wordlist:
        #print "current word is: ", word
        if checkword(word,0):
            matches.append(word)

    print "the matched words are as follows: "
    print matches

    longest_len = 0
    longest = ""
    for match in matches:
        if len(match) > longest_len:
            longest_len = len(match)
            longest = match

    return longest


link = "http://shakespeare.mit.edu/lll/full.html"
f = urllib.urlopen(link)
myfile = f.read()
#print myfile
raw = BeautifulSoup(myfile,"html.parser")
text = raw.get_text()
#print text
lowertext = text.lower()

cleantext = re.sub('[^A-Za-z \n]+', '', lowertext)
#print cleantext
wordlist = cleantext.split()
wordlist.append("etcx")
wordlist = list(set(wordlist))
#wordlist = ("etcx","etux","etfiapi")
#wordlist1 = lowertext.split()
#print wordlist1
#print wordlist
#print wordlist[0]
#print "word length is: ", len(wordlist[0])
startingpoints = {}
matrix = inputmatrix("inputs.txt")
#print "the starting dict is:"
#print startingpoints
legal_moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,-1),(2,1),(-2,-1),(-2,1)]
longest_word = matchwords()
print "the longest word matching is: ", longest_word

