#!/usr/bin/python
# -*- coding: UTF-8 -*-

import config, os, json
from code import analys

# 配置文件
config = config.config
# 扩展名-语言
ext_lang = {}
# 已配置的语言
config_languages = []
# 已配置的扩展名
config_exts = []
for x in config['languages']:
    config_languages.append(x['name'])
    exts = x['exts']
    for y in xrange(0, len(exts)):
        config_exts.append(exts[y])
        ext_lang[exts[y]] = x
config_languages.sort()
config_exts.sort()
print '已配置的语言:'
print config_languages
print '已配置的扩展名:'
print config_exts

# 返回目录下所有文件
def read_files(rootpath, files):
    list = os.listdir(rootpath)
    for x in xrange(0, len(list)):
        path = os.path.join(rootpath, list[x])
        if os.path.isdir(path) and not(path.startswith('.')):
            read_files(path, files)
        if os.path.isfile(path):
            files.append(path)
    files.sort()
    return files

class Dir:
    def __init__(self, rootpath):
        # 目标目录
        self.rootpath = rootpath
        # 所有文件
        self.all_files = read_files(rootpath, [])
        # 包含的语言
        self.included_langs = []
        # 包含的扩展名
        self.included_exts = []
        # 扩展名和个数
        self.exts_nums = {}
        # 其他扩展名和个数
        self.other_exts = {}
        # 文件-语言
        self.file_lang = []

        for f in self.all_files:
            ext = os.path.splitext(f)[1]
            #1 跳过空
            if ext == '':
                continue
            #2 跳过不在配置文件中的
            if ext not in config_exts:
                if ext not in self.other_exts.keys():
                    self.other_exts[ext] = 0
                self.other_exts[ext] += 1
                continue
            #3 扩展名和个数
            if ext not in self.exts_nums.keys():
                self.exts_nums[ext] = 0
            self.exts_nums[ext] += 1
            #4 文件的语言
            self.file_lang.append({ 'path': f, 'ext': ext, 'lang': ext_lang[ext]})
            #5 包含的扩展名
            if ext not in self.included_exts:
                self.included_exts.append(ext)
        self.included_exts.sort()
        #6 包含的语言
        for x in config['languages']:
            for y in x['exts']:
                if x['name'] not in self.included_langs and y in self.included_exts:
                    self.included_langs.append(x['name'])

    def analys(self):
        print '当前目录'
        print self.rootpath
        print '文件个数'
        print len(self.all_files)
        print '包含的语言'
        print self.included_langs
        print '包含的扩展名和个数'
        print self.exts_nums
        print '这些扩展名不处理'
        print self.other_exts
        langs, files, codes, comments, blanks, lines = {}, 0, 0, 0, 0, 0
        for x in self.file_lang:
            lang = x['lang']['name']
            ret = analys(x['path'], x['lang'])
            if lang not in langs.keys():
                langs[lang] = { 'files': 0, 'lines': 0, 'codes': 0, 'comments': 0, 'blanks': 0 }
            langs[lang]['files'] += 1
            langs[lang]['codes'] += ret['codes']
            langs[lang]['comments'] += ret['comments']
            langs[lang]['blanks'] += ret['blanks']
            langs[lang]['lines'] += ret['lines']
            codes += ret['codes']
            comments += ret['comments']
            blanks += ret['blanks']
            lines += ret['lines']
            files += 1
        langs = sorted(langs.iteritems(), key = lambda item:item[1]['lines'], reverse = True)
        print '统计结果'
        print ' Language  Files  Code Lines  Comment Lines  Blank Lines  Total Lines  Total Per'
        for x in langs:
            print '%8s:'%x[0], '%6d'%x[1]['files'], '%11d'%x[1]['codes'], '%14d'%x[1]['comments'], '%12d'%x[1]['blanks'], '%12d'%x[1]['lines'], '%9.2f%%'%(100.0*x[1]['lines']/lines)
        print '   Totals', '%6d'%files, '%11d'%codes, '%14d'%comments, '%12d'%blanks, '%12d'%lines
