from Population import POPULATION
import copy

parents = POPULATION(1)
parents.Evaluate(False)
exit()
parents.Print()

for g in range(0,200):

    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate(True)
    parents.ReplaceWith(children)
    children.Print()
    print(g, end=" ")
    parents.Print()
    if(g==199):
        children = copy.deepcopy(parents)
        children.Mutate()
        children.Evaluate(False)
        parents.ReplaceWith(children)
        children.Print()
        print(g, end=" ")
        parents.Print()

"""import pyrosim
from individual import INDIVIDUAL
import matplotlib.pyplot as plt
from robot import ROBOT
import random
import copy
import pickle

parent = INDIVIDUAL()
parent.Evaluate(False)
print(parent.fitness)

for i in range(0,100):
    child = copy.deepcopy(parent)
    child.Mutate()
    child.Evaluate(True)
    print("[g:", i, "]", "[pw:", parent.genome, "]", "[p:", parent.fitness, "]", "[C:", child.fitness, "]")
    if(child.fitness > parent.fitness):
        child.Evaluate(False)
        parent=child
        f = open('robot.p', 'wb') #ojo, colocar wb en vez de solo w
        pickle.dump(parent,f)
        f.close()
#for i in range(0,10):
#    individual=INDIVIDUAL()
#    individual.Evaluate()
#    print(individual.fitness)


#    sim=pyrosim.Simulator(eval_time=100)
#    robot=ROBOT(sim,random.random()*2-1)
#    sim.start()
#    sim.wait_to_fnish()
#    x = sim.get_sensor_data(sensor_id=robot.P4,svi=0)
#    y = sim.get_sensor_data(sensor_id=robot.P4, svi=1)
#    z = sim.get_sensor_data(sensor_id=robot.P4, svi=2)
#    print(x[-1])


    #sensorData = sim.get_sensor_data( sensor_id = P2)
    #print(sensorData)

#f=plt.figure()
#panel= f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(0,+1.5)
#plt.show()
"""
