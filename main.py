#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sourcer import *

### 分析代码打印分析过程（测试）
# analys_debug('exp/Test.java')
# analys_debug('exp/test.c')

### 某tag的代码的详情（测试）
# info_dir_tag('D:\\GitHub\\rabbitmq-server', 'rabbitmq_v3_6_12')
# info_dir_tag('D:\\GitHub\\kafka', '0.11.0')

### 当前代码详情（测试）
# info_dir('D:\\GitHub\\kafka')
# info_dir('D:\\GitHub\\sourcer\\exp')

### 统计某tag的代码（生产）
# scan_tag('D:\\GitHub\\rabbitmq-server', 'rabbitmq_v3_6_12')
# scan_tag('D:\\GitHub\\kafka', '1.0.0')

### 统计所有tag（生产）
# scan_all_tag('D:\\GitHub\\rabbitmq-server')
scan_all_tag('D:\\GitHub\\mesos')
