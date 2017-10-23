#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re, config

debug = config.config['debug']

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

def analys(path, lang):
    codes, comments, blanks, lines = 0, 0, 0, 0

    string_regex = lang['string_regex']
    single_comment = lang['single_comment']
    comment_open = lang['comment_open']
    comment_close = lang['comment_close']
    comment_open_index = 0 # 多行注释序号

    COMMENT_STAT = False

    if debug:
        print '文件', path
        print '类型', lang['name']

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
                #6 去掉字符串
                line = cls(line, string_regex)
                #7 是否包含多行注释结尾
                close = comment_close[comment_open_index]
                if close in line:
                    COMMENT_STAT = False
                    next_str = line.split(close)[-1]
                    #9 多行注释结尾后面的是否空白
                    if re.match('^[\\s]*$', next_str) != None:
                        comments += 1
                        log(lines, '多行', rline)
                    else:
                        #10 多行注释结尾后面的是否单行注释
                        f10 = False
                        for x in single_comment:
                            if re.match('^[\\s]*' + x + '.*', next_str) != None:
                                f10 = True
                                break
                        if f10:
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
                    comments += 1
                    log(lines, '多行', rline)
                else:
                    codes += 1
                    log(lines, '代码', rline)

    # print '总行:%4d'%lines
    # print '代码:%4d'%codes, '占比:%6.2f%%'%(100.0*codes/lines)
    # print '注释:%4d'%comments, '占比:%6.2f%%'%(100.0*comments/lines)
    # print '空行:%4d'%blanks, '占比:%6.2f%%'%(100.0*blanks/lines)

    return { 'path': path,  'codes': codes, 'comments': comments, 'blanks':blanks, 'lines': lines }
