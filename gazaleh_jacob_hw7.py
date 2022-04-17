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

x=np.where((wv>=10) & (wv<=1000))
s= x[0]
lowerbound=s[0]
upperbound=s[-1]

#make the array go from the upper bound to the lower bound

wv_in=[]
lum_in=[]
i=lowerbound
while i<upperbound:
    wv_in.append(wv[i])
    lum_in.append(lum[i])
    i +=1

#print(wv_in)
#print(lum_in)
print(upperbound,lowerbound)

print(np.trapz(np.flip(lum_in), np.flip(wv_in)))




#print(x)
#idk how this works like this, but it gives me the indices of wv that are between 10 and 1000 which is 0 to 833

"""
plt.plot(wv, lum)
plt.set_yscale('log')
plt.set_xscale('log')
plt.show()
plt.savefig('exsamkjhple', dpi=82)
"""