#!/usr/bin/python
from wordnik import Wordnik

word = Wordnik(api_key='1cc793b4b4ce10c19417b080bb20ecf919bdb5e01fb1eddfc')

x = ' '

while x:
    x = raw_input('\n\nplease enter a word: ')
    define = word.word_get_definitions(x)
    n = 0
    raw = 'y'
    try:
        print '\n', define[n]['text'].upper()
    except IndexError:
        print '\t\tNo Definition'.upper()
        break
    while raw[0] == 'y':
        x = raw_input('\nWould you like the next definition? (y or n): ').lower()
        if x and x[0] == 'y':
            try:
                n += 1
                print '\n', define[n]['text'].upper()
            except IndexError:
                print '\t\tno more definitions'.upper()
                continue
        else:
            break
print '\n\t\tGoodbye'

