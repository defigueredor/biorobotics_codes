from individual import INDIVIDUAL
import copy
import random
from environments import ENVIRONMENTS
import constants as c


class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize
        self.Initialize()

    def Initialize(self):
        for i in range(0, self.popSize):
            self.p[i] = INDIVIDUAL(i)

    def Fill_From(self, other):
        self.Copy_Best_From(other)
        #self.Print()
        self.Collect_Children_From(other)
        #self.Print()

    def Copy_Best_From(self, other):
        control=0
        for i in self.p:
            if (other.p[i].fitness > other.p[control].fitness):
                 control=other.p[i].ID
            self.p[0] = copy.deepcopy(other.p[control])

    def Collect_Children_From(self, other):
        for j in range(1, len(self.p)):
            winner = other.Winner_Of_Tournament_Selection()
            winner.Mutate()
            self.p[j] = copy.deepcopy(winner)
            #self.p[j] = copy.deepcopy(other.p[j])

    def Winner_Of_Tournament_Selection(other):
        p1 = random.randint(0, len(other.p)-1)
        p2 = random.randint(0, len(other.p)-1)
        if (other.p[p1].fitness > other.p[p2].fitness):
            return other.p[p1]
        else:
            return  other.p[p2]

    def Print(self):
        for i in self.p:
            if (i in self.p):
                self.p[i].Print()
        print()

    def Evaluate(self, envs, pp, pb):
        for i in self.p:
            self.p[i].fitness = 0
        for e in range(0, len(envs.envs)):
            for i in self.p:
                self.p[i].Start_Evaluation(envs.envs[e], pp, pb)
            for i in self.p:
                self.p[i].Compute_Fitness()
        for i in self.p:
            self.p[i].fitness = self.p[i].fitness/c.numEnvs

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self,other):
        for i in self.p:
            if ( self.p[i].fitness < other.p[i].fitness ):
                self.p[i] = other.p[i]

