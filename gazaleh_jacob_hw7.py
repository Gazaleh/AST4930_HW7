#import the useful packages
import astropy as ast
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u


#import the relevant data
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

"""
plt.plot(np.flip(wv), lum)
plt.yscale("log")
plt.xscale("log")
plt.ylabel("Wave length")
plt.xlabel("Luminosity")
plt.show()
plt.savefig('example', dpi=82)
"""