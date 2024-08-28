#!/usr/bin/env python

import os, sys
FILE = os.path.abspath(__file__)
WS = os.path.abspath(os.path.join(FILE, '../..'))
sys.path.append(WS)

import filesystem as fs

import unittest

class TestPath(unittest.TestCase):
    def test_abspath(self):
        query = '/home/data/sample.log'
        answer = '/home/data/sample.log'

        path = fs.Path(query)
        self.assertEqual(str(path), answer)

    def test_home(self):
        query = '~/data/sample.log'
        answer = os.path.join(os.environ['HOME'], 'data/sample.log')
        
        path = fs.Path(query)
        self.assertEqual(str(path), answer)

    def test_cwd(self):
        query = None
        answer = os.getcwd()

        path = fs.Path(query)
        self.assertEqual(str(path), answer)
        
        
if __name__ == '__main__':
    unittest.main()
    
