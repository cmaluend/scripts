#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import urllib2
import getopt

def test(k):
	f = open('json.out', 'r')
	return f.read()

def call_api(url, content=None):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        output = response.read()
        return output
    except Exception as e:
        print "Error en el llamado a la api con los parámetros:\n> url: %s\n> content: %s"%(url, content)
        sys.exit()


def print_json(text):
	try:
		response = json.loads(text)
		print json.dumps(response, sort_keys=False, indent=4, separators=(',', ': '))
	except:
		print "El texto no es un JSon válido:\n%s"%text
		sys.exit()

def parse_argv(argv):
    try:
        urls = []
        opts, args = getopt.getopt(sys.argv[1:], 'ip',['url=','item-api=', 'content='])
        opts = dict(opts)
        #print opts
        #print args
        if len(opts)==0:
            raise Exception()
    except Exception as e:
        print '''
        uso: %s [-p | -i] options
        
        -p : Api pública
        -i : Api internal (default)
        
        options:
        --url=URL : llamar a la API usando URL.
        --content=CONTENT : Llamado de la API con los parámetros CONTENT.
        --item-api=ITEM_ID : Detalle para el ITEM_ID
        '''%(sys.argv[0])
        sys.exit()
        
    url = None
    content = None
    
    if opts.get('--item-api'):
        itemId = opts['--item-api']
        url = "mercadolibre.com/items/%s"%itemId
        
    if opts.get('--url'):
        url = opts['--url']
    elif '-p' in opts:
        url = "https://api."+url
    else:
        url = "http://internal."+url
    
    return url, content

if __name__ == '__main__':
    url, content = parse_argv(sys.argv[1:])
    response = call_api(url, content)
    print_json(response)