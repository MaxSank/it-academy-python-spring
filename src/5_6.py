"""Вводится число найти его
максимальный делитель, являющийся
степенью двойки. 10(2) 16(16), 12(4).
"""


number = int(input("Insert the number: "))
print(number & - number)
