# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

if __name__ == '__main__':

   for i in range(105, 999, 7):
     i1 = i % 10
     i2 = (i // 10) % 10
     i3 = (i // 100) % 10
   if (i1 + i2 + i3) % 7 == 0:
    print(i)