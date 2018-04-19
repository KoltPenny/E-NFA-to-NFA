from collections import defaultdict
import random
class State:

    def __init__(self,name):
        self.name = name
        self.st = defaultdict(set)
        self.st["E"].add(self)

    def __str__(self):
        transitions = ""
        for key in self.st: transitions = transitions.join(str(len(self.st[key])))
        return "{ State: "+self.name+" | Transitions: "+transitions+" }"

    #Getters y setters esenciales
    def addQ(self,next_state,symbol):
        self.st[symbol].add(next_state);

    #
    def getQ(self,symbol): return self.st[symbol]
    def getName(self): return self.name

    #Métodos de clase
    def genEp(self,epsilon):
        #sz = size
        sett = set.union(epsilon,self.getQ("E"))
        #sz = len(sett)
        if(epsilon.issubset(sett)): return sett
        epsilon.discard("t")
        
        for item in self.getQ("E"):
            set.union(item.genEp(epsilon),epsilon)
        return sett

class Automata:

    def __init__(self,states,sigma,init,final):
        self.states = states
        self.sigma = sigma
        self.init = init
        self.final = final

    def getQs(self): return self.states
    def getSig(self): return self.sigma
    def getInit(self): return self.init
    def getFinal(self): return self.final

def constructAutomata(filename):

    states = dict();
        
    with open(filename) as file:

        for state in file.readline().strip("\n").split(","):
            states[state] = State(state)
            
            #for st in states: print(states[st])

        sigma = file.readline().split(",")
        init = file.readline()
        final = file.readline().split(",")

        for line in file:
            state = line.strip("\n").split(",")
            states[state[0]].addQ(states[state[2]],state[1])

        for st in states: print(states[st])
    return Automata(states,sigma,init,final)

antik = constructAutomata("Thompson1a.txt")

states = antik.getQs()
Z= states["0"].genEp( set(["t"]))

for el in Z:
    print (el)
