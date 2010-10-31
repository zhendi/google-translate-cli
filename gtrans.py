#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,json,urllib

url_string = 'http://ajax.googleapis.com/ajax/services/language/'

def detect(text):
    query = dict(v='1.0', q=text)
    file = urllib.urlopen(url_string+'detect?%s' % urllib.urlencode(query))
    result = json.loads(file.read())
    return result['responseData']['language'] if result['responseData'] else None

def translate(text):
    source = detect(text) 
    target = ['en','zh-CN'][source == 'en']
    query = dict(v='1.0', q=text,langpair = '%s|%s' % (source, target))
    file = urllib.urlopen(url_string+'translate?%s' % urllib.urlencode(query))
    result = json.loads(file.read())
    return result['responseData']['translatedText'] if result['responseData'] else None

def main():
    if len(sys.argv) == 1:
        info = '''
            usage: python gtrans.py word
            '''
        print info
    else:
        text = ' '.join(sys.argv[1:])
        print translate(text)

if __name__ == '__main__':
    main()
