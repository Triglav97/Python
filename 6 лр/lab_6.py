import numpy as np
import pandas as pd

print("\nЗадание 1\n")

def randint():
    return np.random.randint(2,6, dtype = np.int16)

def check_mark(firstname, lastname, course, DataFrame):
    flag = False
    for i in range( 0, len(list(DataFrame.First_Name)) ):
        if (DataFrame.First_Name[i] == firstname) and (DataFrame.Last_Name[i] == lastname) and check_column(course, DataFrame):
            print (DataFrame.First_Name[i], DataFrame.Last_Name[i], "курс: ", course, "оценка: ", DataFrame[course][i])
            flag = True
    if flag == False:
        print("Неправильные данные")

def check_column(course, DataFrame):
    for i in range (2, len(list(DataFrame.columns)) ):
        if (course == DataFrame.columns[i]):
            return True
    return False

DataFrame = pd.DataFrame([
    {'First_Name': 'qwe', 'Last_Name': 'wer', 'Course_1': randint(), 'Course_2': randint(), 'Course_3': randint()},
    {'First_Name': 'asd', 'Last_Name': 'sdf', 'Course_1': randint(), 'Course_2': randint(), 'Course_3': randint()},
    {'First_Name': 'zxc', 'Last_Name': 'xcv', 'Course_1': randint(), 'Course_2': randint(), 'Course_3': randint()},
    {'First_Name': 'rty', 'Last_Name': 'tyu', 'Course_1': randint(), 'Course_2': randint(), 'Course_3': randint()},
    {'First_Name': 'dfg', 'Last_Name': 'fgh', 'Course_1': randint(), 'Course_2': randint(), 'Course_3': randint()}
    ])

print(DataFrame)
i=0
while (i<3):
    print("Введите имя")
    firstname = input()
    print("Введите фамилию")
    lastname = input()
    print("Введите курс")
    course = input()

    check_mark(firstname, lastname, course, DataFrame)

    i=i+1 #для 3 проверок за раз для 1 таблицы, надеюсь не критично, я 'ручками' проводил поиск, тестил, решил оставить, дальше пользовался функционалом pandas 

print("\nЗадание 2\n")

DataFrame = pd.read_csv("text.csv", sep=',', encoding='cp1251')

print(DataFrame.loc[
    (DataFrame['длина чашелистика'] >= 5) & (DataFrame['ширина чашелистика'] <= 3)
    ])
print("----------------------------------\n")
print(DataFrame.loc[
    (DataFrame['длина лепестка'] <= 2) & (DataFrame['ширина лепестка'] <= 2)
    ])
print("----------------------------------\n")
print(DataFrame.loc[
    (DataFrame['вид ириса'] == 'Iris-versicolor')
    ])

print("\nЗадание 3\n")

NumPy = np.random.randint(-10,10,(5,5))

DataFrame = pd.DataFrame(NumPy, 
        columns = ['A','B','C','D','E'], 
        index = ['a','b','c','d','e'])
print(DataFrame)

DataFrame.loc[DataFrame['A'] < 0,['A']] = np.exp(1)
DataFrame.loc[DataFrame['B'] < 0,['B']] = np.exp(1)
DataFrame.loc[DataFrame['C'] < 0,['C']] = np.exp(1)
print(DataFrame)

DataFrame[DataFrame.iloc[:2] > 1] = np.pi
print(DataFrame)

DataFrame['DE'] = DataFrame['D']/DataFrame['E']
print(DataFrame)

DataFrame.to_csv('new_csv.csv', sep=',', index = False)

print("\nЗадание 4\n")

NumPy = np.zeros((2,2))
A = pd.DataFrame(NumPy)
print(A)

NumPy = np.ones((2,2))
B = pd.DataFrame(NumPy)
print(B)

C = A - B + np.pi
print(C)

C[1]=C.iloc[:,1:]-1
print(C)