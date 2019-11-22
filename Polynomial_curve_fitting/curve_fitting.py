import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
import random 



###-------------training dataset-------------###
trainx=[]
trainy=[]


###-------------sin fuction-------------###
#sin graph#
x = np.linspace(0,1,100) # from 0 to 1 by 100 unit
y = np.sin(2*np.pi*x)


###-------------display-------------###
#generate N points with Gaussian distribution(normal distribution)
print ("Input N that is number of points : %d")
N=int(input())
trainx=np.linspace(0,1,N)
trainy=np.sin(2*np.pi*trainx)
noisey=[]

###-------------noise with gaussian-------------###
#make noise
for i in range(0, N) :
    variance=random.gauss(0.0, 0.1)
    #print ("%.16f" % (random.gauss(0.0, 1.0))) #midium, deviation
    noisey.append(0)
    noisey[i] = trainy[i] + variance
#print (trainx, noise)


###-------------polynomial curve fitting-------------###
polyy=np.polyfit(trainx,noisey,1)



###-------------display-------------#
#sine function graph plot
plt.plot(x, y, label='sin(2πx)')

#noise point
plt.plot(trainx,noisey, 'ro', markersize = 10)


#display all the informations
plt.xlabel("x")
plt.ylabel("t")
plt.title('sin(2πx)')
plt.show()
