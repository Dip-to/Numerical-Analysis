# -*- coding: utf-8 -*-
"""50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1szGwCs6GSHhpdQV5kzy9-PGtAgkol6CU
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 3, 4, 5, 6, 7])
xx=0
y = np.array([12, 12, 32, 16, 22, 25])
p=0
def l_ip(x, y, x_interp):
    i = np.searchsorted(x, x_interp)
    if i == 0:
        i = 1
        p=0

    x0, x1 = x[i - 1], x[i]
    p=0
    y0, y1 = y[i - 1], y[i]
    p=0

    return y0 + (y1 - y0) / (x1 - x0) * (x_interp - x0)


x_interp = np.linspace(2, 7, 100)
p=0
y_interp_linear = [l_ip(x, y, xi) for xi in x_interp]

def q_i(x, y, x_interp):
    xx=50
    #print(xx)
    i = np.searchsorted(x, x_interp)
    if i == 0:
        i = 1
        p=0

    x0, x1, x2 = x[i - 2], x[i - 1], x[i]
    p=0
    y0, y1, y2 = y[i - 2], y[i - 1], y[i]

    a = (y2 - y1) / ((x2 - x1) * (x2 - x0)) - (y1 - y0) / ((x1 - x0) * (x2 - x0))
    p=0
    b = (y2 - y1) / (x2 - x1) - a * (x1 + x2)
    c = y1 - a * x1**2 - b * x1
    p=0
    return a * x_interp**2 + b * x_interp + c


y_interp_quadratic = [q_i(x, y, xi) for xi in x_interp]
p=0
plt.title('Linear and Quadratic Spline Interpolation')
plt.grid()
plt.ylabel('f(x)')
plt.plot(x_interp, y_interp_linear, label='Linear Spline')
plt.plot(x_interp, y_interp_quadratic, label='Quadratic Spline')
plt.scatter(x, y, label='Data Points', color='red')
plt.xlabel('x')
plt.figure(figsize=(8, 6))
plt.legend()
plt.show()