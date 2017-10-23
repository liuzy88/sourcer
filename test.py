#!/usr/bin/python
# -*- coding: UTF-8 -*-


langs = {
	'Xml': {'lines': 21},
	'Scala': {'lines': 11},
	'Java': {'lines': 55}
}

sorted(langs.items(), key=lambda item:item[1]['lines'])

print langs