#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from util import config, Dir

start = time.time()

Dir('exp').analys()

end = time.time()

print '耗时', round(end-start, 3), '秒'
