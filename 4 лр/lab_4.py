import matplotlib.pyplot as plt
import numpy as np
 
print("Задание 1\n")
 
k1, k2, k3 = 4, 15, 3

freq = 100  
a, b = -10, 10

xi = np.linspace(a, b, freq)
y = [k1 * t * t + k2 * t + k3 for t in xi]
plt.plot(xi, y)


plt.grid()
plt.show()

print("Задание 2\n")

freq = 100  
a, b = 0.1, 10

xi = np.linspace(a, b, freq)
y_1 = [1 / (1 + np.exp(-x)) for x in xi]
y_2 = [np.log(x) for x in xi]
y_3 = [np.exp(x) + 1 for x in xi]

fig = plt.figure()
plt.subplot(1,3,1)
plt.plot(xi, y_1, color="red", linestyle='--')
plt.grid()

plt.subplot(1,3,2)
plt.plot(xi, y_2, color="green", linestyle='-.')
plt.grid()

plt.subplot(1,3,3)
plt.plot(xi, y_3, color="brown", linestyle=':')
plt.grid()

plt.show()

print("Задание 3\n")

freq = 100  
a, b = -10, 10

xi = np.linspace(a, b, freq)
y_1 = [np.sin(x) for x in xi]
y_2 = [np.cos(x) for x in xi]
y_3 = [np.sin(x)**2 for x in xi]

plt.plot(xi, y_1, ':b', label='sin(x)')
plt.plot(xi, y_2, '--y', label='cos(x)')
plt.plot(xi, y_3, '-c', label='sin(x)^2')
plt.grid()

plt.legend()
plt.show()

print("Задание 4\n")

freq = 100  
a, b = 0, 1.2

x=[0,0,1,1]
y=[0,1,0,1]
plt.scatter(x, y, color='green')

xi = np.linspace(a, b, freq)
y=[-x+1.2 for x in xi]

plt.plot(xi, y)

plt.annotate('y=-x+1.2', xy=(0.6, 0.6), xytext=(1, 0.8), arrowprops=dict(facecolor='black', width=1, headwidth=5))

plt.annotate('[0,0]', xy=(0, 0), xytext=(0, 0.2), arrowprops=dict(facecolor='black', width=1, headwidth=5))
plt.annotate('[0,1]', xy=(0, 1), xytext=(0, 0.8), arrowprops=dict(facecolor='black', width=1, headwidth=5))
plt.annotate('[1,0]', xy=(1, 0), xytext=(0.8, 0), arrowprops=dict(facecolor='black', width=1, headwidth=5))
plt.annotate('[1,1]', xy=(1, 1), xytext=(1, 1.2), arrowprops=dict(facecolor='black', width=1, headwidth=5))

plt.title('x1&x2')
plt.grid()
plt.show()