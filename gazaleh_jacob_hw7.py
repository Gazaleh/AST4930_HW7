#this was ran on miniconda

#import the useful packages
import astropy as ast
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u


#import the relevant data
#i saved the data to my folder from /blue/ast4930/desika_narayanan
open('/home/jessa.gazaleh/AST4930/HW7/sed.txt', 'r')
sed= np.loadtxt('/home/jessa.gazaleh/AST4930/HW7/sed.txt', delimiter= ",")


#assign an array to each coloumn
wv= np.asarray(sed[:,0])
lum= np.asarray(sed[:,1])

#integrate from the correct bounds
#find where those bounds are and use that in the next step
x=np.where((wv>=10) & (wv<=1000))
s= x[0]
lowerbound=s[0]
upperbound=s[-1]

#make the array go from the upper bound to the lower bound
wv_in=[] #in means integral
lum_in=[]
i=lowerbound
while i<upperbound:
    wv_in.append(wv[i])
    lum_in.append(lum[i])
    i +=1
#now we have arrays of the desired integration bounds 

#integrate the data with units
wv_in_unit= wv_in * u.micron
lum_in_unit= lum_in * u.Lsun/u.micron
print(np.trapz(np.flip(lum_in_unit), np.flip(wv_in_unit)))
#this is the integral with units

#this is the integral in different units
integral=np.trapz(np.flip(lum_in_unit), np.flip(wv_in_unit))
print(integral.to(u.erg/u.s))


fig, ax = plt.subplots(1,2)

#raw data graph
ax[0].plot(wv, lum)
ax[0].set_yscale("log")
ax[0].set_xscale("log")
ax[0].set_xlim([0,lum[0]])
ax[0].set_ylabel("Wave length")
ax[0].set_xlabel("Luminosity")

#integrated section graph
ax[1].plot(wv, lum)
ax[1].bar(wv_in, lum_in)
ax[1].set_yscale("log")
ax[1].set_xscale("log")
ax[1].set_xlim([0,lum[0]])
ax[1].set_ylabel("Wave length")
ax[1].set_xlabel("Luminosity")

plt.show()
plt.savefig('gazaleh_jacob_hw7.png', dpi=82)

print(lum[0], lum[-1])

"""
ax[0,0].plot(wv, lum)
plt.yscale("log")
plt.xscale("log")
plt.ylabel("Wave length")
plt.xlabel("Luminosity")
plt.show()
plt.savefig('example', dpi=82)
"""