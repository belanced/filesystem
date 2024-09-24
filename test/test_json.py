#!/usr/bin/env python

import os, sys
FILE = os.path.abspath(__file__)
WS = os.path.abspath(os.path.join(FILE, '../..'))
sys.path.append(WS)

import filesystem as fs
import argparse

if __name__ == '__main__':
    data = {'test': '테스트'}

    fs.dump_json('test.json', data)