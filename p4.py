import numpy as np
import matplotlib.pyplot as plt

N=1024
x=np.linspace(0,1,1024)				#We sample only from 0<x<1 range
np.random.seed(0)
fx=np.random.rand(N)				# 1024 random numbers between 0 and 1.

k=2*np.pi*np.fft.fftfreq(N,d=1/(N-1))		#sample of k
dft=np.fft.fft(fx,norm='ortho')
power_spec=(1/N)*(np.absolute(dft))**2		#Power spectra is defined as a periodogram
print("Maximum value of k: {}".format(max(k)))
print("Minimum Value of k: {}".format(min(k)))

#Plotting

plt.subplot(2,2,1)
plt.title("1024 random numbers between 0 & 1")
plt.plot(x,fx)
plt.xlabel(r'$x\rightarrow$',fontsize=15)
plt.ylabel(r'$f(x)\rightarrow$',fontsize=15)      #Plotting all random numbers in between 0 and 1


plt.subplot(2,2,2)
plt.plot(k,dft,'teal',label="DFT")
plt.xlabel(r'$k\rightarrow$',fontsize=15)
plt.ylabel(r'$\tilde{f}(k)\rightarrow$',fontsize=15)
plt.legend()

plt.subplot(2,2,3)
plt.plot(k,power_spec,'red',label="Power spectra")
plt.xlabel(r'$k\rightarrow$',fontsize=15)
plt.ylabel(r'$|\tilde{f}(k)|^2$',fontsize=15)
plt.legend()

plt.subplot(2,2,4)
plt.hist(power_spec,range=(min(k),max(k)),bins=5,density=True,facecolor='salmon',label="Histogram")
plt.xlabel(r'$k\rightarrow$',fontsize=15)
plt.ylabel(r'$|\tilde{f}(k)|^2_{bins}\rightarrow$',fontsize=15)
plt.legend()

plt.show()
print("\n\nAll the random numbers are drawn from uniform deviate. So the distribution looks like a flat line, as we have sampled only from the region 0<x<1.\n Therefore, it's Fourier transform is expected to be a delta function. and that is reflected in the power spectra we have obtained.")

