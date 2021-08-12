import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

from skimage import io
from skimage.transform import resize
from mpl_toolkits import mplot3d
 
print("Задание 1\n")

X = np.loadtxt("text.csv", delimiter=",")

plt.subplot(2,2,1)
plt.plot(X.T[0][:10],X.T[1][:10], 'ob', label="Iris-setosa")
plt.plot(X.T[0][10:20],X.T[1][10:20], '^c', label="Iris-versicolor")
plt.plot(X.T[0][20:30],X.T[1][20:30], 'xr', label="Iris-virginica")
plt.legend(numpoints=1)
plt.xlim(4, 16)
plt.grid()

plt.subplot(2,2,2)
plt.plot(X.T[2][:10],X.T[3][:10], '^c', label="Iris-setosa")
plt.plot(X.T[2][10:20],X.T[3][10:20], 'ob', label="Iris-versicolor")
plt.plot(X.T[2][20:30],X.T[3][20:30], 'xr', label="Iris-virginica")
plt.legend(numpoints=1)
plt.xlim(1, 14)
plt.grid()

plt.subplot(2,2,3)
plt.plot(X.T[0][:10],X.T[2][:10], 'xr', label="Iris-setosa")
plt.plot(X.T[0][10:20],X.T[2][10:20], '^c', label="Iris-versicolor")
plt.plot(X.T[0][20:30],X.T[2][20:30], 'ob', label="Iris-virginica")
plt.legend(numpoints=1)
plt.xlim(4, 15)
plt.grid()

plt.subplot(2,2,4)
plt.plot(X.T[1][:10],X.T[3][:10], '1g', label="Iris-setosa")
plt.plot(X.T[1][10:20],X.T[3][10:20], '^c', label="Iris-versicolor")
plt.plot(X.T[1][20:30],X.T[3][20:30], 'xr', label="Iris-virginica")
plt.legend(numpoints=1)
plt.xlim(2, 11)
plt.grid()

plt.show()

print("Задание 2\n")

img = io.imread('Bridge.jpg')
resized_img = resize(img, (400, 400))


k=100
new = resized_img.copy()
while k < 400:
    new[k:k+1, 0:400] = [0, 0, 1]
    k += 100
k=100
while k < 400:
    new[0:400, k:k+1] = [1, 0, 0]
    k += 100
plt.figure()
plt.axis('off')
plt.imshow(new)
plt.show()
plt.imsave('new.png', new)

print("Задание 3\n")

img = io.imread('Bridge.jpg')
A = resize(img, (224, 224, 3))
B = A[0:100, 0:100]

plt.imsave('new2.png', B)
print("фото в файле new2.png")

print("Задание 4\n")

NumPy = np.loadtxt("text2.csv", delimiter=", ")

plt.figure()
plt.hist(NumPy, bins=10)
plt.show()

counts, bin_edges = np.histogram(NumPy, bins=10)
print(counts)

print("Задание 5\n")

NumPy2 = np.loadtxt("text3.csv", delimiter=", ")

plt.figure()
plt.hist(NumPy2, bins=10)
plt.show()

counts, bin_edges = np.histogram(NumPy2, bins=10)
print(counts)

print("Задание 6\n")

kwargs= dict(histtype='stepfilled', alpha=0.3, bins=15)

plt.figure()

plt.hist(NumPy, **kwargs)
plt.hist(NumPy2, **kwargs)

plt.show()

print("Задание 7\n")

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

z1 = np.sin(X)**2 - np.cos(Y)**2

plt.figure()
plt.contourf(X, Y, z1, 100, cmap='coolwarm')
plt.colorbar()

plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, z1, 100, cmap='inferno')

z2 = 2 * X**2 - Y**3

plt.figure()
plt.contourf(X, Y, z2, 100, cmap='winter')
plt.colorbar()

plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, z2, 100, cmap='winter')

plt.show()