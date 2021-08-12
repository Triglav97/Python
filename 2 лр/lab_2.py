import numpy as np

print("Задание 1\n")

X = np.random.randint(-10, 10, (4,6))
print(X)

X_1, X_2, X_3 = np.hsplit(X, 3)
print("X_1\n", X_1,"\nX_2\n", X_2,"\nX_3\n", X_3)

Y_1 = X_1 @ X_2.T
print("Y_1\n", Y_1)
Y_2 = X_2 @ X_3.T
print("Y_2\n", Y_2)

Y = np.concatenate([Y_1, Y_2], axis = 0)
print("Y\n", Y)

print("\nЗадание 2\n")

def Euclide(v_1, v_2):
    v = v_1-v_2
    v = np.power(v, 2)
    d = np.sqrt(sum(v))
    print(d)

v_1 = np.random.randint(-10, 10, 3)
v_2 = np.random.randint(-10, 10, 3)
Euclide(v_1, v_2)

print("\nЗадание 3\n")

def MassNumpy(x, a, n):
    if a is "+":
        return(x + n)    
    elif a is "-":
        return(x - n)
    elif a is "*":
        return(x * n)
    elif a is "/":
        return(x / n)
    elif a is "//":
        return(x // n)
    elif a is "%":
        return(x % n)
    elif a is "**":
        return(x ** n)
    else:
        print("Нет такого")

x = np.random.randint(-5, 6, (5,5))
a = input()
n = int(input())

print(MassNumpy(x, a, n))

print("\nЗадание 4\n")

A = np.random.randint(-100, 100, (4,4))
B = np.random.randint(-100, 100, (4,4))

print ("A\n", A, "\nB\n", B)

C = 2*A+3*B-1
D = 5*A-4*B+7

print ("C\n", C, "\nD\n", D)

print("\nЗадание 5\n")

def NeuralNetwork(X, W, U):
    h = np.dot(X.T, W)
    h = F_activity(h)
    y = np.dot(h, U)
    y = F_activity(y)
    return np.float64(y)
def F_activity(S):
    return 1/(1 + np.exp(-S))

W = np.random.uniform(-1,1, (2,2))
U = np.random.uniform(-1,1, (2,1))

X = np.array([[1], [0]])

print(f"y = ", NeuralNetwork(X, W, U))