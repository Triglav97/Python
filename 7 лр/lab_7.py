import numpy as np
import pandas as pd

print("\nЗадание 1\n")

values = np.array([[np.nan, 2, np.nan],
                    [np.nan, 3, 5], 
                    [1, 4, 6]])
Dataframe = pd.DataFrame(values, columns = ['A', 'B', 'C'], 
                                    index = ['a', 'b', 'c'])
print(Dataframe)

print(Dataframe[Dataframe['C'].notnull()])

print(Dataframe[Dataframe['A'].isnull()])

print("\nЗадание 2\n")

values = np.array([[0.24, 58.64],
                    [0.62, -243.02],
                    [1.00, 1.00],
                    [1.88, 1.03],
                    [11.86, 0.41],
                    [29.46, 0.43],
                    [84.01, -0.72],
                    [164.8, 0.67],
                    [4.60, 0.38],
                    [248.09, -6.39],
                    [282.76, 0.16],
                    [309.88, None],
                    [558.0, 0.3]])
index = [
    ('Земная группа', 'Меркурий'), 
    ('Земная группа', 'Венера'), 
    ('Земная группа', 'Земля'),
    ('Земная группа', 'Марс'), 
    ('Газовые гиганты', 'Юпитер'),
    ('Газовые гиганты', 'Сатурн'),
    ('Газовые гиганты', 'Уран'),
    ('Газовые гиганты', 'Нептун'),
    ('Карликовые планеты', 'Церера'),
    ('Карликовые планеты', 'Плутон'),
    ('Карликовые планеты', 'Хаумеа'),
    ('Карликовые планеты', 'Макемаке'),
    ('Карликовые планеты', 'Эрида')]
columns = ['Период обращения (лет)','Период вращения (дней)']

index = pd.MultiIndex.from_tuples(index)
DataFrame = pd.DataFrame(values, index = index, columns = columns)
print(DataFrame)

print("\nЗадание 3\n")

def randint():
    return np.random.randint(-10,11, (4,4))

Data_1 = pd.DataFrame(randint(), 
                        columns=['A', 'B', 'C', 'D'])
Data_2 = pd.DataFrame(randint(),
                        columns=['AA', 'BB', 'CC', 'DD'])
print(Data_1, "\n", Data_2)

data_axis_0 = pd.concat([Data_1, Data_2], axis=0)
print(data_axis_0)
data_axis_1 = pd.concat([Data_1, Data_2], axis=1)
print(data_axis_1)

print("\nЗадание 4\n")

def randint():
    return np.random.randint(2,6)

values_1 = np.array([['qwe', 'математика'],
                    ['asd', 'русский'],
                    ['zxc', 'физика'],
                    ['Triglav', 'программирование'],
                    ['YVV', 'Python']])

values_2 = np.array([['qwe', randint()],
                    ['Triglav', 5],
                    ['YVV', 5],
                    ['asd', randint()],
                    ['zxc', randint()]])

columns_1 = ['ФИО', 'название дисциплины']
columns_2 = ['ФИО', 'оценка по дисциплине']

data_1 = pd.DataFrame(values_1, columns = columns_1)
data_2 = pd.DataFrame(values_2, columns = columns_2)
print(data_1, "\n\n", data_2, "\n")

merge_data = pd.merge(data_1, data_2, on='ФИО')
print(merge_data)