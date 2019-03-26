#!/usr/bin/env python3
from hashtable import StringHashtable, GuidHashtable, ImageHashtable
import sys


def main():
    # create the string hashtable
    ht1 = StringHashtable()
    for line in open('strings.txt'):
        line = line.strip()
        ht1.set(line.lower(), line)
    print('String hash table:')
    print(repr(ht1))
    print()

    print('String lookups:')
    print(ht1.get('indian meal moth'))
    print(ht1.get('orb-weaving spiders (banded garden spider)'))
    print()

    print('Deletes')
    ht1.remove('indian meal moth')
    ht1.remove('orb-weaving spiders (banded garden spider)')
    print('String hash table (after removing two items):')
    print(repr(ht1))
    print()



    # create the guid hashtable
    ht2 = GuidHashtable()
    for line in open('guids.txt'):
        line = line.strip()
        ht2.set(line.lower(), line)
    print('Guid hash table:')
    print(repr(ht2))
    print()

    print('Guid lookups:')
    print(ht2.get('00000158691797bd77464883000a001800388ccf'))
    print(ht2.get('00000158691797bd7746488c000a001991ef0003'))
    print()

    print('Guid hash table (after removing two items):')
    ht2.remove('00000158691797bd77464883000a001800388ccf')
    ht2.remove('00000158691797bd7746488c000a001991ef0003')
    print(repr(ht2))
    print()


    # create the image hashtable
    ht3 = ImageHashtable()
    for line in open('images.txt'):
        line = line.strip()
        ht3.set(line, line)
    print('Image hash table:')
    print(repr(ht3))
    print()

    print('Image lookups:')
    print(ht3.get('document.png'))
    print(ht3.get('security_keyandlock.png'))
    print()

    print('Image hash table (after removing two items):')
    ht3.remove('document.png')
    ht3.remove('security_keyandlock.png')
    print(repr(ht3))
    print()


###  Bootstrap  ###
if __name__ == '__main__':
    main()
