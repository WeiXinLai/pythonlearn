#!/usr/bin/env python3

from collections import OrderedDict

class LastUpdateOrderedDict(OrderedDict):
	def __init__(self,capacity):
		self._capacity = capacity
	
	def __setitem__(self, key, value):
		containKey = 1 if key in self else 0
		if len(self)-containKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:',last)
		if containKey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value)

FIFO=LastUpdateOrderedDict(5)
FIFO.__setitem__(1,1)
FIFO.__setitem__(2,2)
FIFO.__setitem__(3,3)
FIFO.__setitem__(4,4)
FIFO.__setitem__(23,221)
FIFO.__setitem__(6,6)
FIFO.__setitem__(7,7)
print(FIFO)




