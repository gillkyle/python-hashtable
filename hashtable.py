#!/usr/bin/env python3
import os
import os.path
import binascii
from collections import namedtuple
from io import StringIO
from functools import reduce


# a named tuple to hold an individual key and value
# this Node "object" is never seen outside this class
# (e.g. get() returns the value, not the full Node)
Node = namedtuple("Node", ('key', 'value'))

# This is super small because we want to test the loading and print for debugging easier
NUM_BUCKETS = 10

# return a value between 0-9


def mod(value):
    return value % 10


class Hashtable(object):
    '''
    An abstract hashtable superclass.
    '''

    def __init__(self):
        self.buckets = []
        for i in range(0, 10):
            self.buckets.append([])

    def set(self, key, value):
        '''
        Adds the given key=value pair to the hashtable.
        '''
        # TODO: store the value by the hash of the key
        node = Node(key, value)
        self.buckets[self.get_bucket_index(key)].append(node)
        return

    def get(self, key):
        '''
        Retrieves the value under the given key.
        Returns None if the key does not exist.
        '''
        # TODO: get the value by the hash of the key
        records = self.buckets[self.get_bucket_index(key)]
        return next(record.value for record in records if record.key == key)

    def remove(self, key):
        '''
        Removes the given key from the hashtable.
        Returns silently if the key does not exist.
        '''
        # TODO: remove the value by the hash of the key

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        # leave this method as is - write your code in the subclasses
        raise NotImplementedError(
            'This method is abstract!  The subclass must define it.')

    ##################################################
    # Helper methods

    def __repr__(self):
        '''Returns a representation of the hash table'''
        buf = StringIO()
        for i, bkt in enumerate(self.buckets):
            for j, node in enumerate(bkt):
                buf.write('{:>5}  {}\n'.format(
                    '[{}]'.format(i) if j == 0 else '',
                    node.key,
                ))
        return buf.getvalue()


######################################################
# String hash table

class StringHashtable(Hashtable):
    '''A hashtable that takes string keys'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        # TODO: hash the string and return the bucket index that should be used
        ascii_codes = [ord(c) for c in key]
        # sum the ascii codes
        sum_codes = reduce(lambda a, b: a + b, ascii_codes)
        return mod(sum_codes)


######################################################
# Guid hash table

COUNTER_CHARS = (16, 24)


class GuidHashtable(Hashtable):
    '''A hashtable that takes GUID keys'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        # TODO: hash the string and return the bucket index that should be used


######################################################
# Image hash table
NUM_CHUNKS = 8


class ImageHashtable(Hashtable):
    '''A hashtable that takes image name keys and creates the hash from (some of) the bytes of the file.'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        # TODO: hash the string and return the bucket index that should be used
