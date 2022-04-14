print("hello world")
import astropy as ast
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u

open('/home/jessa.gazaleh/AST4930/HW7/sed.txt', 'r')
sed= np.loadtxt('/home/jessa.gazaleh/AST4930/HW7/sed.txt', delimiter= ",")
#print(sed)

wv= np.asarray(sed[:,0])
lum= np.asarray(sed[:,1])
arr=[wv,lum]
#print(arr)

x=np.where((wv>=10) & (wv<=1000))
y=np.where((lum>=10) & (lum<=1000))
print(wv[-1], lum[-1])
print(wv[0], lum[0])
print(x)
#idk how this works like this, but it gives me the indices of wv that are between 10 and 1000 which is 0 to 833

"""
plt.plot(wv, lum)
plt.set_yscale('log')
plt.set_xscale('log')
plt.show()
plt.savefig('exsamkjhple', dpi=82)
"""