#!/usr/bin/env python

import sys
from os.path import abspath, dirname
dirpath = dirname(abspath(__file__))
sys.path.append(dirpath + '/../')
from migrate.versioning.shell import main
from model import ReaderEngine

if __name__ == '__main__':
  reader = ReaderEngine()
  main(debug = 'False',
       repository = 'migrate',
       url = reader.sqlpath)
