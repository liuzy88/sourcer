#!/usr/bin/python
# -*- coding: UTF-8 -*-

languages = [{
        'name': 'C/C++',
        'exts': ['.h', '.c', '.cpp'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': ['//'],
        'comment_open': ['/*'],
        'comment_close': ['*/']
    }, {
        'name': 'C#',
        'exts': ['.cs'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': ['//'],
        'comment_open': ['/*'],
        'comment_close': ['*/']
    }, {
        'name': 'ASP.NET',
        'exts': ['.asp', '.aspx', '.inc'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': ["'"],
        'comment_open': [],
        'comment_close': []
    }, {
        'name': 'Java',
        'exts': ['.java', '.jsp'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': ['//'],
        'comment_open': ['/*'],
        'comment_close': ['*/']
    }, {
        'name': 'PHP',
        'exts': ['.php'],
        'string_regex': ['"[\S \t]*?"', "'[\S \t]*?'"],
        'single_comment': ['//'],
        'comment_open': ['/*'],
        'comment_close': ['*/']
    }, {
        'name': 'Scala',
        'exts': ['.scala'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': ['//'],
        'comment_open': ['/*'],
        'comment_close': ['*/']
    }, {
        'name': 'Python', # 多行字符串处理？
        'exts': ['.py'],
        'string_regex': ['"[\S \t]*?"', "'[\S \t]*?'"],
        'single_comment': ['#'],
        'comment_open': [],
        'comment_close': []
    }, {
        'name': 'Erlang',
        'exts': ['.hrl', '.erl'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': ['%'],
        'comment_open': [],
        'comment_close': []
    }, {
        'name': 'Ruby',
        'exts': ['.rb'],
        'string_regex': ['#'],
        'string_regex': ['"[\S \t]*?"'],
        'comment_open': ['=begin'],
        'comment_close': ['=end']
    }, {
        'name': 'GO',
        'exts': ['.go'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': ['//'],
        'comment_open': ['/*'],
        'comment_close': ['*/']
    }, {
        'name': 'Pascal',
        'exts': ['.pas'],
        'string_regex': ["'[\S \t]*?'"],
        'single_comment': ['//'],
        'comment_open': ['{'],
        'comment_close': ['}']
    }, {
        'name': 'Lua',
        'exts': ['.lua'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': ['--'],
        'comment_open': ['--[['],
        'comment_close': [']]']
    }, {
        'name': 'Delphi',
        'exts': ['.go'],
        'string_regex': ["'[\S \t]*?'"],
        'single_comment': ['//'],
        'comment_open': ['{','(*'],
        'comment_close': ['}','*)']
    }, {
        'name': 'Swift',
        'exts': ['.swift'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': ['//'],
        'comment_open': ['/*'],
        'comment_close': ['*/']
    }, {
        'name': 'JS',
        'exts': ['.js'],
        'string_regex': ['"[\S \t]*?"', "'[\S \t]*?'"],
        'single_comment': ['//'],
        'comment_open': ['/*'],
        'comment_close': ['*/']
    }, {
        'name': 'Shell',
        'exts': ['.sh'],
        'string_regex': ['"[\S \t]*?"', "'[\S \t]*?'"],
        'single_comment': ['#'],
        'comment_open': [],
        'comment_close': []
    }, {
        'name': 'DOS',
        'exts': ['.cmd', '.bat'],
        'string_regex': [],
        'single_comment': ["'"],
        'comment_open': [],
        'comment_close': []
    }, {
        'name': 'html',
        'exts': ['.htm', '.html'],
        'string_regex': [],
        'single_comment': [],
        'comment_open': ['<--'],
        'comment_close': ['-->']
    }, {
        'name': 'XML',
        'exts': ['.xml'],
        'string_regex': ['"[\S \t]*?"'],
        'single_comment': [],
        'comment_open': ['<--'],
        'comment_close': ['-->']
    }, {
        'name': 'xsl',
        'exts': ['.xsl'],
        'string_regex': [],
        'single_comment': [],
        'comment_open': ['<--'],
        'comment_close': ['-->']
    }]