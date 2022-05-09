from vpython import *
#GlowScript 3.1 VPython
#Constants
H = 0.1#height of trolley A and trolley B
L = 0.1#lenght of trolley A and trolley B
W = 0.1#width of trolley A and trolley B
troll_A = box(pos=vector(-1,0.05,0), length=L, height=H, width=W, color=color.blue, make_trail=True)#animation of trolley A, its position is 1 unit away from trolley B before COLLISION
mass_A = 2#mass of trolley A
mom_A = mass_A*vector(0.5,0,0)#momentum of trolley A with the velocity as a vector, the initial velocity is 5 m/s in the positive x-direction

troll_B = box(pos=vector(0,0,0), length=L, height=H, width=W, color=color.red, make_trail=True)#animation of trolley B at rest
mass_B = 1#mass of trolley B
mom_B = mass_B*vector(0,0,0)#momentum of trolley B with the velocity as a vector, the trolley is at rest 

t = 0#initial time
dt = 0.01#change in time, the step size

k = 100#spring constant

Velocity_graph=graph(title = "velocity vs. time")#plotting the graph of v vs. t
gdisplay( xtitle="Time [s]", ytitle="velocity [m/s]")#designating the axis
t1=gcurve(label = "Trolley A", color=color.blue)#the function of trolley A
t2=gcurve(label = "Trolley B",color=color.red)#the function of trolley B

Momentum_graph=graph(title = "momentum vs. time")#plotting the graph of p vs. t
gdisplay( xtitle="Time [s]", ytitle="momentum [m/s^2]")#designating the axis
p1=gcurve(label = "Trolley A", color=color.blue)#the function of trolley A
p2=gcurve(label = "Trolley B",color=color.red)#the function of trolley B
p3=gcurve(label = "Total momentum of the system", color=color.black)#the function of the conservation of momentum,should appear as straight line

#Processing
while t < 4:
  rate(100)#iterations per second
  FA = vector(0,0,0)#Applie Force acting on the trolleys in the beginning
  x = troll_B.pos - troll_A.pos#distance between A and B
  if mag(x)<L:#setting the condition for a collision between trolley A and trolley B
    FA = -k*x#Hookes's Law
  mom_A = mom_A + FA*dt#
  mom_B = mom_B - FA*dt#
  troll_A.pos = troll_A.pos + mom_A*dt/mass_A#
  velo_A = mom_A/mass_A#velocity of trolley A
  troll_B.pos = troll_B.pos + mom_B*dt/mass_B#
  velo_B = mom_B/mass_B#velocity of trolley B
  t = t + dt#time, that is increased incrementaly
  mom_tot = mom_A+mom_B#Total momentum in the system
  #Output
  t1.plot(t,velo_A.x)
  t2.plot(t,velo_B.x)
  p1.plot(t,mom_A.x)
  p2.plot(t,mom_B.x)
  p3.plot(t,mom_tot.x)
  print("Velocity of A(m/s)",velo_A," ","Time (s)",t)
  print("Velocity of B(m/s)",velo_B," ","Time (s)",t)
  