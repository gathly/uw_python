#!/usr/bin/python

from wordnik import Wordnik

word = Wordnik(api_key='1cc793b4b4ce10c19417b080bb20ecf919bdb5e01fb1eddfc')

x = raw_input('\nplease enter a word: ')

while x:
    define = word.word_get_definitions(x)
    print '\n', define[0]['text']
    x = raw_input('\nplease enter a word: ')
