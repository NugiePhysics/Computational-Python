import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.38,	3.39,	4.75,	6.56,	7.76])
y = np.array([5.01,	4.10,	3.65,	2.51,	1.83])

n = len(x)     # jumlah data di dalam x

xy = np.zeros(n)  # mengalokasikan memori untuk xy
x2 = np.zeros(n)  # mengalokasikan memori untuk x2
for i in range(n):
    xy[i] = x[i]*y[i]
    x2[i]    = x[i]**2

# --------------------------------------------
# hitung gradien
# --------------------------------------------
pembilang = n*np.sum(xy) - np.sum(x)*np.sum(y)
penyebut  = n*np.sum(x2) - (np.sum(x))**2   
m = pembilang/penyebut

# --------------------------------------------
# hitung titik potong dengan sb y
# --------------------------------------------
y_avg = np.sum(y)/n
x_avg = np.sum(x)/n
c = y_avg - m*x_avg

x_fit = np.linspace(1, 8, 10)
y_fit = m*x_fit + c

plt.plot(x,y, 'o')
plt.plot(x_fit,y_fit, '-r')

plt.xlabel('masa siput [ons]')
plt.ylabel('kecepatan siput [mm/s]')
plt.show()






