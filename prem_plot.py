#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
import sys

prem_model = sys.argv[1]

a = np.genfromtxt(prem_model,delimiter=',')

rad = a[:,0]
rho = a[:,2]
vp = a[:,3]
vs = a[:,5]

fig, ax = plt.subplots(figsize=(8,10))

#ax.set_title('Perturbations to PREM')
ax.plot(vp,rad,label=r'$V_{p}$',lw=2)
ax.plot(vs,rad,label=r'$V_{s}$',lw=2)
ax.plot(rho,rad,label=r'$\rho$',lw=2)
ax.grid()
ax.legend()
ax.set_xlim(0,15)
ax.set_ylim(0,6400)
ax.set_ylabel('Radius (m)')
ax.set_xlabel(r'Density $\left(\frac{kg}{m^3}\right)$, '+
              r'Velocity $\left(\frac{km}{s}\right)$')

plt.show()

