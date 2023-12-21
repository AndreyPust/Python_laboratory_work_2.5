#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Даны два кортежа одного размера, в которых нет нулевых
# элементов. Получить третий кортеж, каждый элемент которого
# равен 1, если элементы заданных кортежей с тем же номером
# имеют одинаковый знак, и равен нулю в противном случае.

import sys


if __name__ == '__main__':
    # Ввести кортежи одной строкой.
    first_tuple = tuple(map(float, input("Введите кортеж 1"
                                         " без нулевых элементов: ").split()))
    second_tuple = tuple(map(float, input("Введите кортеж 2"
                                          " без нулевых элементов: ").split()))
    # Проверить размер обоих кортежей.
    if len(first_tuple) != len(second_tuple):
        print("Кортежи должны быть одинаковой длины!", file=sys.stderr)
        exit(1)
    # Проверить элементы в кортежах.
    if 0 in first_tuple or 0 in second_tuple:
        print("В кортежах есть нули!", file=sys.stderr)
        exit(1)

    # Составим третий кортеж.
    count = 0  # Счетчик для обращения к элементу второго кортежа
    third_tuple = ()
    for i in first_tuple:
        if ((i > 0 and second_tuple[count] > 0) or
                (i < 0 and second_tuple[count] < 0)):
            third_tuple += (1,)
        else:
            third_tuple += (0,)
        count += 1

    print("Элементы первого кортежа: ", first_tuple)
    print("Элементы второго кортежа: ", second_tuple)
    print("Элементы третьего кортежа: ", third_tuple)
