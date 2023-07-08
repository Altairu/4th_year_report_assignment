import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,10,10)

a= np.loadtxt("./vib4.csv",delimiter=',')

b,c= plt.subplots(figsize=(6,4))

c.plot(a[:,0],a[:,1])

c.set_xlabel('Time [s]')
c.set_ylabel('Acceleration [$m/s^2$]')
plt.xlim(0,2000)
#plt.xlim(0,1400)
#plt.ylim(-11,11)
plt.ylim(-4,4)
#c.set_xticks([0, 1000])
c.set_xticks([0,1000,2000])
c.legend(loc='best')
#c.grid(ls=':')
plt.savefig("vib4.png", format="png", dpi=300)
plt.show()
