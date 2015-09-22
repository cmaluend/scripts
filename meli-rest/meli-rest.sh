#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import urllib2

def test(k):
	f = open('json.out', 'r')
	return f.read()

def call_api(url):
	try:
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		content = response.read()
		return content
	except:
		print "Error en la conexión"
		sys.exit()


def print_json(text):
	try:
		response = json.loads(text)
		print json.dumps(response, sort_keys=False, indent=4, separators=(',', ': '))
	except:
		print "El texto no es un Json válido:\n%s"%text
		sys.exit()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "%s url"%sys.argv[0]
		sys.exit()
	response = call_api(sys.argv[1])
	print_json(response)