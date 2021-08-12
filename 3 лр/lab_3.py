import numpy as np

print("Задание 1\n")

A = np.random.randint(0, 256, (4, 4))

print (A , "\n")

B = np.empty((2,2))
B.fill(np.NaN)
B[0,0] = np.max(A[0:2, 0:2])
B[0,1] = np.max(A[0:2, 2:4])
B[1,0] = np.max(A[2:4, 0:2])
B[1,1] = np.max(A[2:4, 2:4])

print (B , "\n")

C = np.empty((2,2))
C.fill(np.NaN)
C[0,0] = np.min(A[0:2, 0:2])
C[0,1] = np.min(A[0:2, 2:4])
C[1,0] = np.min(A[2:4, 0:2])
C[1,1] = np.min(A[2:4, 2:4])

print (C , "\n")

D = np.empty((2,2))
D.fill(np.NaN)
D[0,0] = np.mean(A[0:2, 0:2])
D[0,1] = np.mean(A[0:2, 2:4])
D[1,0] = np.mean(A[2:4, 0:2])
D[1,1] = np.mean(A[2:4, 2:4])

print (D , "\n")

print("Задание 2\n")

A = np.random.randint(-100, 100, (8, 8))

print (A , "\n")

print ("сумма элементов = ", np.sum(A), "\n")

print ("максимальные значения в столбцах", np.amax(A, axis = 0))
print ("минимальные значения в столбцах", np.amin(A, axis = 0))
print ("максимальные значения в строках", np.amax(A, axis = 1))
print ("минимальные значения в строках", np.amin(A, axis = 1), "\n")

print ("медианa: \n", np.median(A))
print ("процентиль: \n", np.percentile(A, 50))
print ("В лекции ошибка, np.percentile - это процентиль, для вычисления квантиля используется функция np.quantile")
print ("квантиль: \n", np.quantile(A, q=0.5))

print("Задание 3\n")

A = np.random.randint(0, 10, (5, 5))
print (A)

B = np.mean(A, axis = 1)
C = np.mean(A, axis = 0)

print ("средние значеня по строкам: ", B)
print ("средние значеня по столцам: ", C)
print ("вычитание из каждого эл по строкам соот ср знач: \n", (A.T - B).T)
print ("вычитание из каждого эл по столбцам соот ср знач: \n", A - C)

print("Задание 4\n")

X = np.random.randint(-100, 100, (8, 8))
X = np.float64(X)
print (X)

X = np.where(X>0, np.pi, X)
X = np.where((X<-10), np.exp(1), X)
X = np.where(X<0, 0, X)
print (X)

print("Задание 5\n")

Y = np.random.randint(-10, 10, (8, 8))
print(Y)

print("сумма, удовлетворяющая условию:", np.sum(
            np.where( 
                ((Y**2)-5 >20) | ((Y-1) <0), Y, 0  
            )   
        )
    )

print("Задание 6\n")

V = np.random.randint(-20, 20, 10)
print(V)

V_unique, V_coutns = np.unique(V, return_counts=True)
print(V_unique)
print(V_coutns)