#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Debug Logging
# 2015-07-29 15:39:41

import logging
logging.basicConfig(level=logging.INFO)


s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
