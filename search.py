import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
import random

for i in range(0,10):
    sim=pyrosim.Simulator(eval_time=10000)
    robot=ROBOT(sim,random.random()*2-1)
    sim.start()
#sim.wait_to_fnish()
    #sensorData = sim.get_sensor_data( sensor_id = P2)
    #print(sensorData)

#f=plt.figure()
#panel= f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(0,+1.5)
#plt.show()
