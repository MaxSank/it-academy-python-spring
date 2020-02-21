"""Шоколадка **
Определения:
1. Шоколадка - прямоугольник, размером
n×m (n, m - натуральные).
2. Разлом - деление шоколадки на две
части с натуральными размерами по прямой.
3. Долька - элемент шоколадки размером
1х1. Очевидно шоколадка состоит из n*m долек.
4. Кусок - элемент шоколадки произвольного
(целочисленного размера).

1. Определите, можно ли одним разломом отделить
от шоколадки кусок площадью ровно k.
2. Определите, можно ли отломить от шоколадки ровно
k долек за некоторое количество разломов.
3. Определите, можно ли отломить от шоколадки ровно
k долек с помощью t разломов
Описание решения поместите в docstring
"""

n = int(input("Insert n: "))
m = int(input("Insert m: "))
k = int(input("Insert k: "))

# long "non-lazy" first version
if k < n * m:
    if (k / n) < m and k % n == 0:
        print("Можно, целый кусок размером {} "
              "на {}".format(n, int(k / n)))
    elif (k / m) < n and k % m == 0:
        print("Можно, целый кусок размером {} "
              "на {}".format(m, int(k / m)))
    else:
        print("Нельзя")

# short second version
"""Я же уже проверил в начальном if первые 
условия в последующем if и elif из first version"""

if k < n * m:
    if k % n == 0 or k % m == 0:
        print("Можно")
    else:
        print("Нельзя")

"""В первой задаче нам надо сначала 
убедиться, что в принципе можно отломить 
такую площадь.
Т.к. отломить надо за один раз, то 
одна из сторон отломанной части k должна 
быть равна или n или m. Значит, деление k на 
n или m должно давать целое число."""

# shortest 3th version
if k < n * m:
    print(k % n == 0 or k % m == 0)

"""Условие второй подзадачи: Определите, можно 
ли отломить от шоколадки ровно k долек за 
некоторое количество разломов."""

razl = 0
if k < n * m:
    while k > 0:
        if k % n < k % m and (k // n > 0 or k // m > 0):
            """Делаем разлом параллельно стороне n для 
            получения целого максимально возможного куска 
            шоколада, содержащего только искомые дольки"""

            (m, k) = (m - (k // n), k - (n * (k // n)))
            razl += 1
        elif k % m <= k % n and (k // n > 0 or k // m > 0):
            """Делаем разлом параллельно стороне m для 
            получения целого максимально возможного куска 
            шоколада, содержащего только искомые дольки"""

            (n, k) = (n - (k // m), k - (m * (k // m)))
            razl += 1
        elif k // n == 0 or k // m == 0:
            """Если одним разломом искомые дольки уже не 
            отломить, два условия выше становятся
             направлены на отламывание ненужных"""

            k = n * m - k

    print("Количество разломов: ", razl)
