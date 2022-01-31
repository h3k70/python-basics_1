# Функция для расчета расстояния между двумя точками
def dist(point_a, point_b):
    return ((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2) ** 0.5


# Переносим точки с карты
point_1 = (0, 2)
point_2 = (2, 5)
point_3 = (5, 2)
point_4 = (6, 6)
point_5 = (8, 3)

# Рассчитываем расстояние между всеми точками
distance = {
    "1-2": dist(point_1, point_2),
    "1-3": dist(point_1, point_3),
    "1-4": dist(point_1, point_4),
    "1-5": dist(point_1, point_5),
    "2-3": dist(point_2, point_3),
    "2-4": dist(point_2, point_4),
    "2-5": dist(point_2, point_5),
    "3-4": dist(point_3, point_4),
    "3-5": dist(point_3, point_5),
    "4-5": dist(point_4, point_5)
}

# Создаем таблицу расстояний
streets = (
    (0, distance["1-2"], distance["1-3"], distance["1-4"], distance["1-5"]),
    (distance["1-2"], 0, distance["2-3"], distance["2-4"], distance["2-5"]),
    (distance["1-3"], distance["2-3"], 0, distance["3-4"], distance["3-5"]),
    (distance["1-4"], distance["2-4"], distance["3-4"], 0, distance["4-5"]),
    (distance["1-5"], distance["2-5"], distance["3-5"], distance["4-5"], 0)
)

# Минимальный путь для будущего первого сравнения
min_path = float('inf')

# Здесь будет записан итоговый путь по точкам
path = ""

# Перебор всех вариантов маршрута (первая точка маршрута всегда 0)
i1 = 0
for i2 in range(5):
    for i3 in range(5):
        for i4 in range(5):
            for i5 in range(5):

                # Улицы не должны повторяться
                if (
                    (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and
                    (i2 != i3) and (i2 != i4) and (i2 != i5) and
                    (i3 != i4) and (i3 != i5) and
                    (i4 != i5)
                ):

                    #  Расчет текущего маршрута и сравнение его с минимальным
                    path_length = (streets[i1][i2] + streets[i2][i3] + streets[i3][i4] + streets[i4][i5] + streets[i5][i1])
                    if (path_length < min_path):

                        # Записываем маршрут и его длину
                        path = "point_" + str(i1 + 1) + ' -> ' + \
                               "point_" + str(i2 + 1) + " [" + str(streets[i1][i2]) + "]" + ' -> ' + \
                               "point_" + str(i3 + 1) + " [" + str(streets[i1][i2] + streets[i2][i3]) + "]" + ' -> ' + \
                               "point_" + str(i4 + 1) + " [" + str(streets[i1][i2] + streets[i2][i3] + streets[i3][i4]) + "]" + ' -> ' + \
                               "point_" + str(i5 + 1) + " [" + str(streets[i1][i2] + streets[i2][i3] + streets[i3][i4] + streets[i4][i5]) + "]" + ' -> ' + \
                               "point_" + str(i1 + 1) + " [" + str(path_length) + "]" + " = " + \
                               str(path_length)
                        min_path = path_length

# Вывод итогового маршрута
#print(path)

# Вывод итогового маршрута (вариант как в ТЗ)
print(path.replace("point_1", "(0, 2)").replace("point_2", "(2, 5)").replace("point_3", "(5, 2)").replace("point_4", "(6, 6)").replace("point_5", "(8, 4)"))

# Вывод итогового маршрута (с названиями улиц)
"""
print(path.replace("point_1", "Почтовое отделение") \
      .replace("point_2", "Ул. Грибоедова, 104/25") \
      .replace("point_3", "Ул. Бейкер стрит, 221б") \
      .replace("point_4", "Ул. Большая Садовая, 302-бис") \
      .replace("point_5", "Вечнозелёная Аллея, 742"))
"""

