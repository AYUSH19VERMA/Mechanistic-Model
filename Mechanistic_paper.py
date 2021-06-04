import numpy as np
import matplotlib
from scipy.integrate import odeint
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
y0 = [1e6, 0, 0, 0,]	
t = np.linspace(0, 48, 70)
alpha = 0.0017
beta = 0.28
k_NF = 1.2e-6
d_MF = 0.32e-6
k_C = 0.38e-12
k_NC = 0.31e-6
delta_C = 0.066
delta_N = 1.2
delta_F = 0.090


params = [alpha, beta, k_NF, d_MF, k_C, k_NC, delta_C, delta_N, delta_F]

def sim(variables, t, params):
	F = variables[0]	
	C = variables[1]    
	N = variables[2]
	Fd = variables[3]    
	Nv =  150e6            
        
	M = 0.3e6       

	alpha = params[0]
	beta = params[1]
	k_NF = params[2]
	d_MF = params[3]
	k_C = params[4]
	k_NC = params[5]
	delta_C = params[6]
	delta_N = params[7]
	delta_F = params[8]


	dFdt = beta*F - k_NF*N*F - d_MF*M*F
	dCdt = k_C*M*F + k_NC*N - delta_C*C     
	dNdt = alpha*Nv*C - k_NF*N*F - delta_N*N 
	dFddt = k_NF*N*F + d_MF*M*F - delta_F*Fd

	return([dFdt, dCdt, dNdt, dFddt]) 


y = odeint(sim, y0, t, args=(params,))
a1 = y[:,0]
a2 = y[:,1]
a3 = y[:,2]
a4 = y[:,3]     

plt.plot(t, a1, color ='blue', label = 'F')
plt.plot(t,a2*1e6, color ='cyan', label = 'C')
plt.plot(t,a3, color ='red')
plt.plot(t,a4, color ='pink')
plt.yscale("log",)
plt.ylim(1e4,1e10)
ticks1 = [0,24,48]
plt.xticks([0,24,48],ticks1)



plt.xlabel("Time[h]")
plt.ylabel("Cells")
plt.title("Immunocompoetent")

plt.grid()

plt.show()

