#!/usr/bin/env python3

import fractions
import numpy as np
import gmpy2
from .utils import *

def check_integral_root_wiener(n, phi):
	b = n - phi + 1
	return gmpy2.is_square((b // 2) ** 2 - n)


def wiener_attack(key):
	cont_frac_list = get_continued_fraction_list(key.e, key.n)

	for i in range(len(cont_frac_list)):

		k, d = get_fraction_from_continued_frac_list(cont_frac_list[:i + 1])	

		if ((d % 2 == 0) or (k == 0) or ( ((key.e*d - 1) % k) != 0) ):
			continue
		
		phi = (key.e*d - 1) // k

		if (check_integral_root_wiener(key.n , phi)):
			key.d = d
			return {"Possible" : True, "Key" : key}
	
	return {"Possible" : False}
