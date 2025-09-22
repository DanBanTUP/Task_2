import json
import numpy as np
import matplotlib.pyplot as plt
import sys

# Читаем данные из JSON файла
with open(sys.argv[1], 'r') as file:
    data = json.load(file)
x_values = []
y_values = []

# Извлекаем данные из JSON
for point in data['data']:
    x_values.append(point['x'])
    y_values.append(point['y'])

# Строим график
graf_from_json = plt.subplot()
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
graf_from_json.set_xlim((-5, 5))
plt.title('Graph of y = f(x)')

# Определяем шаг рисок по оси Y из командной строки
if len(sys.argv) > 2:
        try:
            y_step = float(sys.argv[2])
            plt.yticks(np.arange(min(y_values), max(y_values) + 1, y_step))
        except ValueError:
            print("Ошибка: Некорректный ввод шага для оси Y.")
else:
    y_step = 1  # Значение по умолчанию

# Отображаем график
plt.show()
