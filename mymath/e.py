#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author  :  swolf.qu
# E-mail  :  swolf.qu@gmail.com
# Date    :  2018-01-26 19:22:08

import sys


for i in range(1, int(sys.argv[1]) + 1):
    print("{:<10} {}".format(i, (1 + 1/i) ** i))
