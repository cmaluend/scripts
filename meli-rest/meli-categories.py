#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import urllib2

# Es importante agregar la variable de ambiente:
# export PYTHONIOENCODING='UTF-8'
# para redireccionar la salida std a un archivo.

def call(url):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        output = response.read()
        jout = json.loads(output, 'utf-8')
        return jout
    except Exception as e:
        print "Error en el llamado a la api con los parámetros:\n> url: %s"%(url)
        sys.exit()

def call_api(id, attr=""):
    url = '%s%s'%('https://api.mercadolibre.com/categories/', id)
    response = call(url)
    response['attribute'] = call(url+'/attributes')
    return response


def process(jout):
    categories = jout.get('children_categories', '')
    if categories:
        list = [ process(call_api(category.get('id'))) for category in categories]
        jout['children_categories'] = list
        return jout
    else:
        return jout

if __name__ == '__main__':
    response = call_api(sys.argv[1])
    jout = process(response)
    print json.dumps(jout, sort_keys=False, indent=4, separators=(',', ': '), encoding="utf-8", ensure_ascii=False)