import pyrosim






sim=pyrosim.Simulator(play_paused = True, eval_time=1000)
whiteObject =sim.send_cylinder( x=0 , y=0 , z=0.6)
#redObject=sim.send_cylinder(x=0.5, y=0, z=1.1,r1=1,r2=0,r3=-1, r=1, g=0, b=0)
redObject=sim.send_cylinder(x=0, y=0.35, z=0.7,r1=0,r2=1,r3=-1.2, r=1, g=0, b=0)
joint=sim.send_hinge_joint(first_body_id=whiteObject, second_body_id=redObject,x=0,y=0,z=1.1,n1=-1,n2=0,n3=0,lo=-3.14159/2 , hi=3.14159/2)
sim.start()
sim.wait_to_finish()