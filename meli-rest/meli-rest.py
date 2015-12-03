#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import urllib2
import getopt


def read_file(name):
    f = open(name, 'r')
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
        response = json.loads(text, 'utf-8')
        print json.dumps(response, sort_keys=False, indent=4, separators=(',', ': '), encoding="utf-8", ensure_ascii=False)
    except:
        print "El texto no es un JSon válido:\n%s"%text
        sys.exit()

def parse_argv(argv):
    try:
        urls = []
        opts, args = getopt.getopt(sys.argv[1:], 'ip',['url=','file=','item-api=', 'content='])
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
    is_file = False

    if opts.get('--item-api'):
        itemId = opts['--item-api']
        url = "mercadolibre.com/items/%s"%itemId

    if opts.get('--url'):
        url = opts['--url']
    elif opts.get('--file'):
        is_file = True
        url = opts['--file']
    elif '-p' in opts:
        url = "https://api."+url
    else:
        url = "http://internal."+url

    return url, content, is_file

if __name__ == '__main__':
    uri, content, is_file = parse_argv(sys.argv[1:])

    response = ''
    if (is_file):
        response = read_file(uri)
    else:
        response = call_api(uri, content)
    print_json(response)
