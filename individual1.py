#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    n = int(input("Введите номер месяца: "))

    if n == 1:
        print("первое полугодие, 31 день")
    elif n == 2:
        print("первое полугодие, 28 дней")
    elif n == 3:
        print("первое полугодие, 31 день")
    elif n == 4:
        print("первое полугодие, 30 дней")
    elif n == 5:
        print("первое полугодие, 31 день")
    elif n == 6:
        print("первое полугодие, 30 дней")
    elif n == 7:
        print("второе полугодие, 31 день")
    elif n == 8:
        print("второе полугодие, 30 дней")
    elif n == 9:
        print("второе полугодие, 31 день")
    elif n == 10:
        print("второе полугодие, 30 дней")
    elif n == 11:
        print("второе полугодие, 31 день")
    elif n == 12:
        print("второе полугодие, 30 дней")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)