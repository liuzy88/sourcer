#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from util import config, Dir

start = time.time()

Dir('D:\\Github\\kafka').analys()

print '耗时'
print round(time.time()-start, 3), '秒'
