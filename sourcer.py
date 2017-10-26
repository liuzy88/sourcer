#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re, time, config

### 基础配置
####################################################

debug = False
languages = config.languages
config_langs = []
config_exts = []
ext_lang = {}
for x in languages:
    config_langs.append(x['name'])
    exts = x['exts']
    for y in exts:
        config_exts.append(y)
        ext_lang[y] = x
config_langs.sort()
config_exts.sort()

### 打印详情
####################################################

def list_files(dir, files):
    list = os.listdir(dir)
    for f in list:
        path = os.path.join(dir, f)
        if os.path.isdir(path) and not(f.startswith('.')):
            files = list_files(path, files)
        elif os.path.isfile(path):
            files.append(path)
    return files

def info_dir_tag(dir, tag):
    x = os.popen('git pull')
    x.close()
    x = os.popen('git checkout ' + tag)
    x.close()
    info_dir(dir)

def info_dir(dir):
    all_files = list_files(dir, [])
    file_lang, included_langs, included_exts, exts_nums, other_exts = [], [], [], {}, { '*': 0 }
    for f in all_files:
        ext = os.path.splitext(f)[1]
        if ext == '':
            other_exts['*'] += 1
            continue
        # 跳过不在配置文件中的
        if ext not in config_exts:
            if ext not in other_exts.keys():
                other_exts[ext] = 0
            other_exts[ext] += 1
            continue
        # 扩展名和个数
        if ext not in exts_nums.keys():
            exts_nums[ext] = 0
        exts_nums[ext] += 1
        # 文件的语言
        file_lang.append({ 'path': f, 'ext': ext, 'lang': ext_lang[ext]})
        # 包含的扩展名
        if ext not in included_exts:
            included_exts.append(ext)
    # 包含的语言
    for x in languages:
        for y in x['exts']:
            if x['name'] not in included_langs and y in included_exts:
                included_langs.append(x['name'])
    included_langs.sort()
    included_exts.sort()
    print '已配置的语言:', config_langs
    print '已配置的扩展名:', config_exts
    print '当前目录:', dir
    print '包含的语言:', included_langs
    print '包含的扩展名:', exts_nums
    print '忽略的扩展名:', other_exts
    print '文件总数/处理/忽略:', '%d/%d/%d'%(len(all_files), len(file_lang), len(all_files) - len(file_lang))
    langs, files, codes, comments, blanks, lines = {}, 0, 0, 0, 0, 0
    for x in file_lang:
        lang = x['lang']['name']
        ret = analys(x['path'], x['lang'])
        if lang not in langs.keys():
            langs[lang] = { 'files': 0, 'codes': 0, 'comments': 0, 'blanks': 0, 'lines': 0 }
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
    print '统计结果:'
    print ' Language  Files  Code Lines  Comment Lines  Blank Lines  Total Lines  Total Per'
    for x in langs:
        print '%8s:'%x[0], '%6d'%x[1]['files'], '%11d'%x[1]['codes'], '%14d'%x[1]['comments'], '%12d'%x[1]['blanks'], '%12d'%x[1]['lines'], '%9.2f%%'%(100.0*x[1]['lines']/lines)
    print '   Totals', '%6d'%files, '%11d'%codes, '%14d'%comments, '%12d'%blanks, '%12d'%lines

### 扫描版本
####################################################

def scan_all_tag(dir):
    os.chdir(dir)
    x = os.popen('git pull')
    x.close()
    x = os.popen('git tag')
    tags = x.readlines()
    x.close()
    ret = []
    for x in tags:
        tag = x[:-1]
        x = os.popen('git checkout ' + tag)
        x.close()
        x = os.popen('git log -1 --format=%ct')
        date = time.strftime("%Y-%m-%d", time.localtime(int(x.read()[:-1])))
        x.close()
        info = scan(dir)
        print tag, date, info
        ret.append({ 'tag': tag, 'date': date, 'info': info })
    return ret

def scan_tag(dir, tag):
    x = os.popen('git checkout ' + tag)
    x.close()
    x = os.popen('git log -1 --format=%ct')
    date = time.strftime("%Y-%m-%d", time.localtime(int(x.read()[:-1])))
    x.close()
    info = scan(dir)
    print tag, date, info
    return { 'tag': tag, 'date': date, 'info': info }

### 扫描
####################################################

def read_files(dir, files):
    list = os.listdir(dir)
    for f in list:
        path = os.path.join(dir, f)
        if os.path.isdir(path) and not(f.startswith('.')):
            files = read_files(path, files)
        elif os.path.isfile(path):
            ext = os.path.splitext(f)[1]
            if ext != '' and ext in config_exts:
                files.append(path)
    return files

def scan(dir):
    all_files = read_files(dir, [])
    all_files.sort()
    file_lang = []
    for f in all_files:
        ext = os.path.splitext(f)[1]
        file_lang.append({ 'path': f, 'ext': ext, 'lang': ext_lang[ext]})

    langs, files, codes, comments, blanks, lines = {}, 0, 0, 0, 0, 0
    for x in file_lang:
        lang = x['lang']['name']
        ret = analys(x['path'], x['lang'])
        if lang not in langs.keys():
            langs[lang] = { 'files': 0, 'codes': 0, 'comments': 0, 'blanks': 0, 'lines': 0 }
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
    return { 'files': files,  'codes': codes, 'comments': comments, 'blanks':blanks, 'lines': lines }

### 代码分析
####################################################

def r(regex):
    for x in ['*', '{', '}', '[', ']', '(', ')']:
        regex = regex.replace(x, '\\' + x)
    return regex

def cls(line, string_regex):
    old_line = line
    line = line.replace('\\"', '').replace("\\'", '')
    for x in string_regex:
        line = re.sub(x, '', line)
    if old_line != line and debug:
        print '   ┌====>|', line
    return line

def log(num, tag, rline):
    if debug:
        print '%3d|'%num, '%4s'%'' + tag + '|', rline

def analys_debug(path):
    global debug
    debug = True
    ext = os.path.splitext(path)[1]
    lang = ext_lang[ext]
    analys(path, lang)

def analys(path, lang):
    codes, comments, blanks, lines = 0, 0, 0, 0
    try:
        string_regex = lang['string_regex']
        single_comment = lang['single_comment']
        comment_open = lang['comment_open']
        comment_close = lang['comment_close']
        comment_open_index = 0 # 多行注释序号
        COMMENT_STAT = False
        if debug:
            print '文件', path
            print '类型', lang['name']
        if os.path.exists(path):
            with open(path, 'r') as f:
                for line in f.readlines():
                    lines += 1
                    #0 去掉最后的换行
                    line = line[:-1]
                    if line.endswith('\r'):
                        line = line[:-1]
                    rline = line
                    #1 是否空行
                    if re.match('^[\\s]*$', line) != None:
                        blanks += 1
                        log(lines, '空行', rline)
                        continue
                    #2 是否在多行注释中
                    if COMMENT_STAT:
                        #9 去掉字符串
                        line = cls(line, string_regex)
                        #10 是否包含多行注释结尾
                        close = comment_close[comment_open_index]
                        if close in line:
                            COMMENT_STAT = False
                            next_str = line.split(close)[-1]
                            #11 多行注释结尾后面的是否空白
                            if re.match('^[\\s]*$', next_str) != None:
                                comments += 1
                                log(lines, '多行', rline)
                            else:
                                #12 多行注释结尾后面的是否单行注释
                                f12 = False
                                for x in single_comment:
                                    if re.match('^[\\s]*' + x + '.*', next_str) != None:
                                        f12 = True
                                        break
                                if f12:
                                    comments += 1
                                    log(lines, '多行', rline)
                                else:
                                    codes += 1
                                    log(lines, '代码', rline)
                        else:
                            comments += 1
                            log(lines, '多行', rline)
                    else:
                        #3 是否单行注释
                        f3 = False
                        for x in single_comment:
                            if re.match('^[\\s]*' + x + '.*', line) != None:
                                f3 = True
                                comments += 1
                                log(lines, '单行', rline)
                                break
                        if f3:
                            continue
                        #4 去掉字符串
                        line = cls(line, string_regex)
                        #5 是否多行注释开头
                        f5 = False
                        for x in xrange(0,len(comment_open)):
                            if re.match('^[\\s]*' + r(comment_open[x]) + '.*', line) != None:
                                comment_open_index = x
                                COMMENT_STAT = True
                                f5 = True
                                break
                        if f5:
                            #6 是否多行注释结尾
                            close = comment_close[comment_open_index]
                            if close in line:
                                COMMENT_STAT = False
                                next_str = line.split(close)[-1]
                                #7 多行注释结尾后面的是否空白
                                if re.match('^[\\s]*$', next_str) != None:
                                    comments += 1
                                    log(lines, '多行', rline)
                                else:
                                    #8 多行注释结尾后面的是否单行注释
                                    f8 = False
                                    for x in single_comment:
                                        if re.match('^[\\s]*' + x + '.*', next_str) != None:
                                            f8 = True
                                            break
                                    if f8:
                                        comments += 1
                                        log(lines, '多行', rline)
                                    else:
                                        codes += 1
                                        log(lines, '代码', rline)
                        else:
                            codes += 1
                            log(lines, '代码', rline)
    except Exception as e:
        pass
    if debug:
        print '总行:%4d'%lines
        print '代码:%4d'%codes, '占比:%6.2f%%'%(100.0*codes/lines)
        print '注释:%4d'%comments, '占比:%6.2f%%'%(100.0*comments/lines)
        print '空行:%4d'%blanks, '占比:%6.2f%%'%(100.0*blanks/lines)
    return { 'path': path,  'codes': codes, 'comments': comments, 'blanks':blanks, 'lines': lines }

####################################################