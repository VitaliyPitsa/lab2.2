#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    print("введите 3 числа")

    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    print ("наибольшее число ")
    if a >= b and a >= c:
        print(a)
    elif b >= c and b >= a:
        print(b)
    else :
        print(c)