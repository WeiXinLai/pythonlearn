#!/usr/bin/env python3

import gevent
from gevent.pool import Pool

pool=Pool(2)

def hello_from(n):
	print('Size of pool %s' % len(pool))

pool.map(hello_from,range(3))




