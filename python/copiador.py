#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


arquivo = open(sys.argv[1], 'rb')
arquivo2 = open('copia-'+ str(sys.argv[1]), 'wb')
arquivo2.write(arquivo.read()) 
arquivo2.close()
arquivo.close()
