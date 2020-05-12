import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
import random
import math
import numpy
import constants as c
from environment import ENVIRONMENT

class INDIVIDUAL:
    def __init__(self, i):
        self.genome = numpy.random.rand(5, 8) * 2 - 1
        #self.genome[0,0]=0
        #print(self.genome[0, 0])
        #print(self.genome)
        #exit()
        self.fitness = 0
        self.ID = i

    #def Evaluate(self,pb):

    def Start_Evaluation(self, env, pp, pb):
        self.sim=pyrosim.Simulator(play_paused=pp, eval_time=c.evalTime, play_blind = pb )
        self.robot=ROBOT(self.sim, self.genome)
        env.Send_To(self.sim)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        #x = self.sim.get_sensor_data(sensor_id =  self.robot.P4, svi = 0)
        #y = self.sim.get_sensor_data(sensor_id =  self.robot.P4, svi = 1)
        #z = self.sim.get_sensor_data(sensor_id =  self.robot.P4, svi = 2)
        y = self.sim.get_sensor_data(sensor_id=self.robot.L4)
        self.fitness = self.fitness + y[-1]
        del self.sim

    def Mutate(self):
        ###########################################
        geneToMutate_x = random.randint(0, 4)
        geneToMutate_y = random.randint(0, 7)
        #print(geneToMutate_x, geneToMutate_y)
        self.genome[geneToMutate_x, geneToMutate_y] = random.gauss(self.genome[geneToMutate_x, geneToMutate_y],
                                                                   math.fabs(
                                                                       self.genome[geneToMutate_x, geneToMutate_y]))
        if (self.genome[geneToMutate_x, geneToMutate_y]<-1):
            self.genome[geneToMutate_x, geneToMutate_y]=-1
        elif(self.genome[geneToMutate_x, geneToMutate_y]>1):
            self.genome[geneToMutate_x, geneToMutate_y] = 1
        else:
            self.genome[geneToMutate_x, geneToMutate_y]=self.genome[geneToMutate_x, geneToMutate_y]

    def Print(self):
        print('[', self.ID, self.fitness, ']', end=" ")

    #sensorData = sim.get_sensor_data( sensor_id = P2)
    #print(sensorData)

#f=plt.figure()
#panel= f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(0,+1.5)
#plt.show()
