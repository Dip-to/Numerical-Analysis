# -*- coding: utf-8 -*-
"""50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BwkYZH8UpSrjrh1ynatDmbWwKDYWkveH
"""

import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x ** 3 - x - 1

def df(x):
    return 3 * x ** 2 - 1

print("---------------------------------------------------------------------------------------------------------------------------")
print("      Xi      |       f(xi)      |      f'(xi)     |       xi+1     | Approximation Error | Relative Approximation Error")
print("---------------------------------------------------------------------------------------------------------------------------")
x0 = 50
iteration = 1
it_arr = []
apprx_arr=[]

while abs(f(x0)) >= 10 ** -5:
    it_arr.append(iteration)
    iteration += 1
    xi = x0 - (f(x0) / df(x0))
    apprx =abs( xi - x0)
    r_apprx = (apprx * 100) / xi
    print(f"  {x0:10.6f}  | {f(x0):15.6f} | {df(x0):15.6f} | {xi:15.6f} | {apprx:19.6f} | {r_apprx:20.6f}%")
    apprx_arr.append(apprx)
    x0 = xi

x = np.array(it_arr)
y = np.array(apprx_arr)

plt.bar(x,y)
plt.show()