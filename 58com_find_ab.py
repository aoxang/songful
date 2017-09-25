#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

a = []
for i in range(10000000):
    a.append(random.randint(1, 6553523))


def get_ab(list, n):
    z_list = []
    f_list = []
    map = [0] * (n + 1)
    for item in list:
        if item < 1 or item > n:
            z_list.append(-1)
            f_list.append(-1)
        else:
            z_list.append(item)
            map[item] += 1
            if map[item] == 0:
                print item
            f_list.append(n - item)
            map[n-item] += -1
            if map[n-item] == 0:
                print n-item


if __name__ == '__main__':
    get_ab(a, 1000)
