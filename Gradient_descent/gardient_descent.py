'''
followed by https://towardsdatascience.com/implement-gradient-descent-in-python-9b93ed7108d1
'''
import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
import matplotlib.pyplot as plt
cur = 3 # Initial value x=3
learning_rate = 0.01 # Learning rate
precision = 0.000001 #Minimum
prev_step_size = 1 #
global_step = 1000 # Globalsteps
steps = 0 # count steps
df = lambda x: 3*(x+2) #Gradient desecnt function 
mem=np.zeros(global_step+1)

while prev_step_size > precision and steps < global_step:
    prev = cur # Record current value in prev
    cur = cur - learning_rate * df(prev) # Grad descent
    prev_step_size = abs(cur - prev) #Change in val
    steps = steps+1 # Current step
    mem[steps]=cur
    print("Step",steps,"\n value is",cur) #Print steps & current value

plt.xlabel('Steps')
plt.xlim([0, 1000])
plt.xlabel('Current value')   
plt.plot(mem)
plt.show()

print("The local minimum occurs at", cur)
