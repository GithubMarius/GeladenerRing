import math
import matplotlib.pyplot as plt
n = 1000
h = 0.1
a = 0
R = 1

ergebnis = []
Ort = []
rho = 1
epsilon_o = 8.8541878128 * 10**(-12) # [As/Vm]
constant = rho / (4 * math.pi * epsilon_o)

def f(x, r):
    return constant * 1 / ( ((r - R * math.cos(x))**2 + R**2 * math.sin(x)**2)**(1/2) )


for r in range(0, 99):
    r = r/100
    erg = 0
    for i in range(62):
        for j in range(i):
            x = h * j
            erg += h / 2 * f(x,r) + f(x+h,r)
    Ort.append(r)
    ergebnis.append(erg)


for r in range(101, 3000):
    r = r/100
    erg = 0
    for i in range(62):
        for j in range(i):
            x = h * j
            erg += h / 2 * f(x,r) + f(x+h,r)
    Ort.append(r)
    ergebnis.append(erg)

print(Ort, ergebnis)
plt.plot(Ort, ergebnis)
plt.show()