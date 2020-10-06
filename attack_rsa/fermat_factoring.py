#!/usr/bin/env python3

import gmpy
from .RSA_Key import *

def Fermat_Factoring_Attack(key, limit = 100000):

	k = gmpy.sqrt(key.n)

	for i in range(limit):
		
		h2 = k*k - key.n
		
		if (h2 >= 0):	
			h = gmpy.sqrt(h2)
			if (h*h == h2):
				key.p = k + h
				key.q = k - h
				return {"Possible" : True, "Key" : key}
		k += 1

	return {"Possible" : False}