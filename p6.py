#Prob 6: We have implemented Rk4 method to solve these 

import numpy as np
import matplotlib.pyplot as plt

def f1(x,y1,y2):
	return 32*y1+66*y2+2/3*x+2/3
def f2(x,y1,y2):					# These two functions return dy1/dx and dy2/dx
	return -66*y1-133*y2-1/3*x-1/3

x=0
y1=1/3
y2=1/3
h=0.001
xl,y1l,y2l=[],[],[]

while(x<=0.5+h):
	xl.append(x)
	y1l.append(y1)
	y2l.append(y2)

	k1=h*f1(x,y1,y2)
	l1=h*f2(x,y1,y2)

	k2=h*f1(x+h/2,y1+k1/2,y2+l1/2)
	l2=h*f2(x+h/2,y1+k1/2,y2+l1/2)

	k3=h*f1(x+h/2,y1+k2/2,y2+l2/2)
	l3=h*f2(x+h/2,y1+k2/2,y2+l2/2)

	k4=h*f1(x+h,y1+k3,y2+l3)
	l4=h*f2(x+h,y1+k3,y2+l3)

	y1+=1/6*(k1+k4+2*(k2+k3))				#standard rk4 formula
	y2+=1/6*(l1+l4+2*(l2+l3))
	x+=h

#plotting the result

plt.title("prob6: Solution of coupled differential equation by rk4 method")
plt.plot(xl,y1l,label=r'$y_1$')
plt.plot(xl,y2l,label=r'$y_2$')
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

