from individual import INDIVIDUAL
import pickle

f=open('robot.p','rb')
best=pickle.load(f)
f.close()
best.Evaluate(True)
print(best.fitness)