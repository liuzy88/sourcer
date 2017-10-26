#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sourcer import *

### 分析代码打印分析过程（测试）
# analys_debug('exp/Test.java')
# analys_debug('exp/test.c')

### 某tag的代码的详情（测试）
# info_dir_tag('D:\\GitHub\\rabbitmq-server', 'rabbitmq_v3_6_12')

### 当前代码详情（测试）
# info_dir('D:\\GitHub\\kafka')

### 统计某tag的代码（生产）
# scan_tag('D:\\GitHub\\rabbitmq-server', 'rabbitmq_v3_6_12')

### 统计所有tag（生产）
scan_all_tag('D:\\GitHub\\libjson')
