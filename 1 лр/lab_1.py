import numpy as np

def CreateMatrix_5x5(x, y):
    return(np.random.randint(x, y, (5, 5)))

def SumPositiveNumInMatrix(x):
    print("Сумма положительных чисел = ", np.sum(x[x>=0]))

def SumNegativeNumInMatrix(x):
    print("Сумма отрицательных чисел = ", np.sum(x[x<0]))

print("Задание 1\n")

matrix = CreateMatrix_5x5(-10, 11)
print(matrix)    
SumPositiveNumInMatrix(matrix)
SumNegativeNumInMatrix(matrix)

print("\nЗадание 2\n")
         
fMass = np.loadtxt("text.csv", delimiter=",")

X_1 = fMass[1::2, :11]
X_2 = fMass[0::2, :11]
Y_1 = fMass[1::2, 11:]
Y_2 = fMass[0::2, 11:]
print("Матрица X_1\n", X_1, "\n\n", 
        "Матрица X_2\n", X_1, "\n\n", 
        "Матрица Y_1\n", X_1, "\n\n", 
        "Матрица Y_2\n", Y_2, "\n")

XT_1 = X_1.T
XT_2 = X_2.T
YT_1 = Y_1.T
YT_2 = Y_2.T
print("Транспонированная матрица X_1\n",XT_1, "\n\n",
        "Транспонированная матрица X_2\n", XT_2, "\n\n",
        "Транспонированная матрица Y_1\n", YT_1, "\n\n",
        "Транспонированная матрица Y_1\n", YT_2)

print("\nЗадание 3\n")

def CreateVector(x, y, z):
    return np.random.randint(x, y, z)

A = CreateVector(-10,10,10)
print("Вектор А: \n", A)

B = A[A<0]
print("Вектор B: \n", B)

C = A[A>=0]
print("Вектор C: \n", C)

print("\nЗадание 4\n")

X = CreateMatrix_5x5(-100, 100)

print("Матрица X\n", X)

I = CreateVector(0,5,5)
print("Вектор I\n", I)

J = CreateVector(0,5,5)
print("Вектор J\n", J)

Y = np.array(X[I, J])
print("Вектор Y\n", Y)

print("\nЗадание 5\n")

def F(n, t):
        if (n<0):
            print("Невозможно создать матрицу")
        else:
            if (t == "zero"):
                print(np.zeros((n,n), dtype=int))
            elif (t == "one"):
                print(np.ones((n,n), dtype=int))
            elif (t == "identity"):
                print(np.identity(n, dtype=int))
            elif (t == "full"):
                print(np.full((n,n), n, dtype=int))
            else:
                print("Невозможно создать матрицу")

while (True):
    while (True):
        print("Введите целое число n (exit для выхода): \n") 
        n = input()
        if (n=="exit"):
            break
        try: 
            int(n)
            break
        except ValueError:
            print("n не целочисленная")

    if (n=="exit"):
        print("Я вышел")
        break

    print("Введите \"zero\", \"one\", \"identity\" или \"full\" t (exit для выхода): \n")
    t = input()
    if (t=="exit"):
        print("Я вышел")
        break
    print("Размер матрицы: ",n,"\nТип матрицы: ", t)
    F(int(n), t) 