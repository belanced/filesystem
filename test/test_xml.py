#!/usr/bin/env python

import os, sys
FILE = os.path.abspath(__file__)
WS = os.path.abspath(os.path.join(FILE, '../..'))
sys.path.append(WS)

import filesystem as fs
import argparse

def parse_args():
    parser = argparse.ArgumentParser('Xml test')
    parser.add_argument('path', type=fs.Path, help='path to a xml file.')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    path = args.path

    panrye = fs.read_xml(path)
    print(panrye)