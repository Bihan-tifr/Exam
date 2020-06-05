#Problem8: Solving boundary value problem; we apply shooting method to do so.

import numpy as np
import matplotlib.pyplot as plt

def Ivp(p_0):      #Solves initial value problem given an initial value for dy/dx
	
	x,y,h=0,0,0.01
	p=p_0
	yl=[]
	while(x<=1+h):
		yl.append(y)
		y+=p*h
		p+=4*(y-x)*h
		x+=h
	return yl

xl=np.arange(0,1.01,0.01)
yan=(np.exp(2*xl)-np.exp(-2*xl))/(np.exp(4)-1)*np.exp(2)+xl			#Analytical Solution
N=len(xl)
z=0
while(1):
	p1=float(input("Enter 1st initial guess of dy/dx:"))
	p2=float(input("Enter 2nd initial guess of dy/dx:"))
	y1l=Ivp(p1)
	y2l=Ivp(p2)

	plt.plot(xl,y1l,'y')
	plt.plot(xl,y2l,'y')

	y1f=y1l[N-1]								#value of y at x=2
	y2f=y2l[N-1]
	if(y1f==2):
		z=1
		print("{} is correct initial guess".format(p1))			#If solution of initial value problem produces
		plt.plot(xl,y1l,'k',label="bvp_solution")			#correct boundary condition, that is our desired solution.
		break
	elif(y2f==2):
		z=2
		print("{} is true initial guess".format(p2))
		plt.plot(xl,y2l,'k',label="bvp_solution")
		break
	elif((y1f-2)*(y2f-2)<0):
		z=3
		print("True initial guess lies in between {} and {}".format(p1,p2))
		break

if(z==3): 
	y1=(y1f-2)
	y2=(y2f-2)
	for i in range(0,50): #solution by bisection
		p=(p1+p2)/2
		yl=Ivp(p)
		yf=yl[N-1]-2
		if(yf==0):
			print("True initial guess for dy/dx is {}".format(p))
			z=4
			break
		elif(abs(yf)<0.000000001):
			print("True initial guess for dy/dx is {}".format(p))
			z=4
			break
		elif(y1*yf<0):
			p2=p
			y2=yf
		elif(y2*yf<0):
			p1=p
			y1=yf
		plt.plot(xl,yl,'y')

err=abs((yan-yl)/yan)    # Stores relative error between numerical and analytical result. However,yan[0]=yl[0]=0. division by zero is encountered.
err[0]=0		#So err[0]=0, 	because of no absolute error at that point.

print("Relative Error\n{}".format(err))   # prints error array


#plotting
plt.title("p8:Boundary value problem via shooting method")
plt.xlim(0,1.1)
plt.xlabel(r'$x\rightarrow$',fontsize=15)
plt.ylabel(r'$y\rightarrow$',fontsize=15)
if(z==4):
	plt.plot(xl,yl,'k',label="bvp_num_sol")
plt.plot(xl,yan,'r',linestyle='dashed',label="Analytical_sol")
plt.legend()
plt.savefig("p8.jpg")
plt.show()
		




	
