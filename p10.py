import numpy as np
import matplotlib.pyplot as plt

def f(x):
	if abs(x)<1 :
		return 1			#Defining box function
	else:
		return 0
for i in range(3):
	N=int(input("Enter the value of N:"))		# user input N. The program takes three inputs and compute the result one after another.
	x_min=-50
	x_max=50
	x=np.linspace(x_min,x_max,N)
	d=(x_max-x_min)/(N-1)
	fx,fk=[],[]

	for i in range(N):
		fx.append(f(x[i]))			# the box function array

	dft=np.fft.fft(fx,norm='ortho')			#performing DFT
	k=2*np.pi*np.fft.fftfreq(N,d)			#sampling k values

	factor=np.exp(-1j*k*x_min)

	FT=d*np.sqrt(N/(2*np.pi))*factor*dft		#Fourier transform

	#Plotting
	fig, ax= plt.subplots(1,2)
	fig.suptitle("p10:Fourier transform with sampling rate {:,.4f}".format(d))
	ax[0].plot(x,fx,'blue',label="box function")
	ax[0].set_xlabel(r'$x\rightarrow$',fontsize=15)
	ax[0].legend()
	ax[0].set_ylabel(r'$f(x)\rightarrow$',fontsize=15)
	ax[1].plot(k,FT,'red',label="FT of box function")
	ax[1].set_xlabel(r'$k\rightarrow$')
	ax[1].set_ylabel(r'$\tilde{f}(k)\rightarrow$')
	ax[1].legend()
	plt.show()





