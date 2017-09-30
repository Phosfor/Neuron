#Hopfield

from neuron import TNeuron
import cPickle

neuronen = []

generate = raw_input("(L)oad/(G)enerate? ").upper()=="G"


def addAllToInput(x, y):
    print "Neuron[", x, "][", y, "]"
    for i in range(0, len(neuronen)):
        for j in range(0, len(neuronen[0])):
            if not(i == x and j == y):
                neuronen[x][y].addInput(neuronen[i][j], 0)

def neuronLearn(x,y, pat):
    status = pat[x][y]
    for i in range(0, len(neuronen)):
        for j in range(0, len(neuronen[0])):
            if not(i == x and j == y):
                if status == pat[i][j]:
                    gewicht = neuronen[x][y].getWeight(neuronen[i][j]) + 1
                else:
                    gewicht = neuronen[x][y].getWeight(neuronen[i][j]) - 1
                neuronen[x][y].setWeight(neuronen[i][j],gewicht)

def learnPat(pat):
    print "Lerne"
    for i in range(0, len(pat)):
        print 
        for j in range(0, len(pat[0])):
            if pat[i][j] < 0:
                print " ",
            else:
                print "X",
            neuronLearn(i,j, pat)
    print "100%"

def setPat(pat):
    for i in range(0, len(neuronen)):
        for j in range(0, len(neuronen[0])):
            neuronen[i][j].setValue(pat[i][j])

def erkenne():
    for i in range(0, len(neuronen)):
        print
        for j in range(0, len(neuronen[0])):
            neuronen[i][j].setValue(neuronen[i][j].getInput())
            output = neuronen[i][j].getOutput()
            if output < 0:
                print " ",
            else:
                print "X",

def printpat(pat):
    for i in range(0, len(pat)):
        print
        for j in range(0, len(pat[0])):
            if pat[i][j] < 0:
                print " ",
            else:
                print "X",

def setOutputFunc():
    for i in range(0, len(neuronen)):
        for j in range(0, len(neuronen[0])):
            neuronen[i][j].setOutputFunc('''if val <= 0:
    out = -1
else:
    out = 1''')#fehler

def zeigeGewichtung(x,y):
    for i in range(0, len(neuronen[x][y].weights)):
        print neuronen[x][y].weights[i],
    print

x=1
o=-1

pat = [[o,o,o,o,x,x,x,x,o,o,o,o],\
       [o,o,o,x,x,x,x,x,x,o,o,o],\
       [o,o,x,x,x,o,o,x,x,x,o,o],\
       [o,x,x,x,o,o,o,o,x,x,x,o],\
       [o,x,x,x,o,o,o,o,x,x,x,o],\
       [x,x,x,o,o,o,o,o,o,x,x,x],\
       [x,x,x,o,o,o,o,o,o,x,x,x],\
       [x,x,x,o,o,o,o,o,o,x,x,x],\
       [x,x,x,x,x,x,x,x,x,x,x,x],\
       [x,x,x,x,x,x,x,x,x,x,x,x],\
       [x,x,x,x,x,x,x,x,x,x,x,x],\
       [x,x,x,o,o,o,o,o,o,x,x,x],\
       [x,x,x,o,o,o,o,o,o,x,x,x],\
       [x,x,x,o,o,o,o,o,o,x,x,x],\
       [x,x,x,o,o,o,o,o,o,x,x,x]]

pat1= [[x,x,x,x,x,x,x,x,o,o,o,o],\
       [x,x,x,o,o,o,x,x,x,x,o,o],\
       [x,x,x,o,o,o,o,x,x,x,x,o],\
       [x,x,x,o,o,o,o,o,x,x,x,o],\
       [x,x,x,o,o,o,o,x,x,x,x,o],\
       [x,x,x,x,x,x,x,x,x,x,o,o],\
       [x,x,x,x,x,x,x,x,o,o,o,o],\
       [x,x,x,x,x,x,x,x,o,o,o,o],\
       [x,x,x,o,o,o,x,x,x,x,o,o],\
       [x,x,x,o,o,o,o,x,x,x,x,o],\
       [x,x,x,o,o,o,o,o,x,x,x,o],\
       [x,x,x,o,o,o,o,o,x,x,x,o],\
       [x,x,x,o,o,o,o,x,x,x,x,o],\
       [x,x,x,x,x,x,x,x,x,x,o,o],\
       [x,x,x,x,x,x,x,x,o,o,o,o]]


def load():
    f = open("AB.pat", "r")
    global neuronen
    neuronen = cPickle.load(f)
    f.close()
def save():
    f = open("AB.pat", "w")
    global neuronen
    cPickle.dump(neuronen, f)
    f.close()

if(generate):
    """Create the neurons"""
    for i in range(0,15):
        col = []
        for j in range(0,12):
            neuron = TNeuron()
            col.append(neuron)
        neuronen.append(col)

    """Connect neurons"""
    for i in range(0, len(neuronen)):
        for j in range(0, len(neuronen[0])):
            addAllToInput(i,j)
    
    print "Lerne Pat1"
    learnPat(pat)
    print "Lerne Pat2"
    learnPat(pat1)
    save();
else:
    load();



#for i in range(0, len(neuronen)):
#    for j in range(0, len(neuronen[0])):
#        zeigeGewichtung(i,j)

setOutputFunc();
print "OutputFunc:\n", neuronen[0][0].outputFunc

pat2 = [[o,o,o,o,x,x,x,x,o,o,o,o],\
       [o,x,o,x,x,o,x,x,x,x,o,o],\
       [o,o,x,x,o,o,o,o,x,x,o,o],\
       [o,x,o,x,o,o,o,o,x,x,x,o],\
       [o,x,x,x,o,o,o,o,x,o,x,o],\
       [x,x,x,o,o,x,x,o,o,x,x,x],\
       [x,x,o,o,o,o,o,x,o,o,o,o],\
       [x,x,x,o,o,o,o,o,o,x,o,x],\
       [o,x,x,x,x,x,x,x,o,x,x,x],\
       [x,x,x,o,x,x,o,x,x,x,o,x],\
       [x,o,x,x,x,x,x,x,x,x,x,x],\
       [x,x,x,o,o,o,o,o,o,x,o,x],\
       [x,x,x,o,o,o,x,o,o,x,x,x],\
       [x,o,o,o,x,x,x,o,o,x,o,x],\
       [x,x,o,o,o,o,o,o,o,x,x,x]]

pat3= [[x,x,x,x,x,o,x,x,o,o,o,o],\
       [o,o,o,o,o,o,x,x,x,o,o,o],\
       [x,x,x,o,o,o,o,x,x,o,x,o],\
       [x,o,x,o,x,x,o,o,x,o,x,o],\
       [x,x,x,o,o,o,o,x,x,x,x,o],\
       [x,x,o,o,o,x,x,x,x,x,o,o],\
       [x,x,x,o,x,x,o,x,o,o,o,o],\
       [x,x,x,o,x,x,x,o,o,o,x,o],\
       [x,x,x,o,o,o,x,x,x,x,x,o],\
       [x,o,x,o,o,o,o,x,o,x,x,o],\
       [x,x,o,o,o,o,o,o,x,x,x,o],\
       [x,x,x,o,o,o,o,o,x,o,x,o],\
       [x,x,o,o,o,o,o,x,x,x,x,o],\
       [x,o,x,x,x,o,x,x,x,x,o,o],\
       [x,x,x,x,x,x,o,x,o,o,o,o]]

print
print "Eingabemuster:"
printpat(pat2)

raw_input("\n\nEnter zum erkennen!")
print
print "Erkannt"
setPat(pat2)
erkenne()
#pat3
print
print "Eingabemuster:"
printpat(pat3)

raw_input("\n\nEnter zum erkennen!")
print
print "Erkannt"
setPat(pat3)
erkenne()
