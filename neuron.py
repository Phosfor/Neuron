# module Neuron

from random import random

debug = 0;

class TNeuron:
    '''Diese Klasse stellt ein Neuron dar.

    addInput(neuron, weight = rand())
    delInput(neuron)
    getIndex(neuron):index
    
    setWeight(neuron, weight)
    getInput():gesammtInput
    getOutput():Output
    setValue(value)
    setOutputFunc(func)'''

    def __init__(self):
        if debug == 1:
            print "(Neuron wird erzeugt)"
        self.outputFunc = "out = val"
        self.value   = 1
        self.inputs  = []
        self.weights = []

    def __del__(self):
        if debug == 1:
            print "Neuron Stirbt"

    def getIndex(self, neuron):
        if debug == 1:
            print "Suche neuronenindex von ", neuron
        index = -1
        for I in range(0, len(self.inputs)):
            if self.inputs[I] == neuron:
                if debug == 1:
                    print "Gefunden: ", I
                index = I
        return index

    def addInput(self, neuron, weight = "random"):
        if weight == "random":
            weight = random()
        self.inputs.append(neuron)
        self.weights.append(weight)
        if debug == 1:
            print "Neuron-input hinzugefuegt. Index Nr. ", len(self.inputs)-1
            print "Gewichtung: ", self.weights[len(self.inputs)-1]
        
    def delInput(self, neuron):
        index = self.getIndex(neuron)
        if index == -1:
            if debug == 1:
                print "Dieser Input Exestiert nicht"
        else:
            del self.inputs[index]
            del self.weights[index]

    def setWeight(self, neuron, weight):
        index = self.getIndex(neuron)
        self.weights[index] = weight
        if debug == 1:
            print "new Weight from ", index, " = ", weight

    def getWeight(self, neuron):
        return self.weights[self.getIndex(neuron)]

    def getOutput(self):
        val = self.value
        exec self.outputFunc
        return out

    def setOutputFunc(self, func):
        self.outputFunc = func
    
    def getInput(self):
        value = 0
        anzahl = len(self.inputs)
        for i in range(0, anzahl):
            out = self.inputs[i].getOutput()
            weight = self.weights[i]
            val = out * weight
            value = value + val
        return value

    def setValue(self, val):
        self.value = val
            
        
if __name__ == "__main__":
    debug = 1
    print "Starte Beispiel"
    print TNeuron.__doc__

    print
    print
    n1 = TNeuron()
    print
    n2 = TNeuron()
    print
    n3 = TNeuron()
    n3.addInput(n1, 2)
    n3.addInput(n2, 8)

    print
    print
    print "Setzte n1.value auf 2"
    n1.setValue(2)
    print n3.getInput()

    print
    del n1
    del n2
    del n3
    
    print "ENDE"
    
