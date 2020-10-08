#!/usr/bin/env python3

import fractions
import numpy as np
import gmpy2
from Crypto.PublicKey import RSA
from asn1crypto.x509 import Certificate
import pickle

def get_continued_fraction_list (p, q):	
	res = []
	while (p != 0 and q != 0):
		frac = fractions.Fraction(p, q)
		integer_part = p//q 
		res.append(integer_part)
		frac -= integer_part
		p,q = frac.denominator, frac.numerator
	return res


def get_fraction_from_continued_frac_list(l):
	expr = fractions.Fraction(l[0], 1)
	for i in reversed(l[1:]):
		expr += i
		expr = 1/expr
	return expr.numerator, expr.denominator


def gcd(a, b):
	if a == 0:
		return b
	return gcd(b % a, a)


def extended_gcd(a, b):
	"""
	We know:
		ax + by = gcd(a, b)
	
	This function returns gcd(a,b), x , y 	
	"""

	if a == 0:
		return b, 0, 1
	gcd, x_, y_ = extended_gcd(b % a, a)

	x = y_ - (b // a) * x_
	y = x_

	return gcd, x, y


def read_key(filename):
	f = open(filename,'r')
	return RSA.importKey(f.read())


def read_certificate(filename):
	"""
	return certificate object using asn1crypto.x509
	n = cert.public_key.native["public_key"]["modulus"]
	e = cert.public_key.native["public_key"]["public_exponent"]
	"""

	with open(filename, "rb") as f:
		return Certificate.load(f.read())


def get_all_quadratic_residue (n):
	"""
	We say that an integer x is a Quadratic Residue if there exists an a such that a2 = x mod p.
	If there is no such solution, then the integer is a Quadratic Non-Residue.

	If a^2 = x then (-a)^2 = x. So if x is a quadratic residue in some finite field, then there are always two solutions for a.
	
	This Function returns a dict with residue as key and its roots as value:
	{
		key = [a, b]
	}
	Therefore a*a  mod n = key  or	 b*b  mod n = key 
	
	Complexity : O(n)
	"""
	
	res = {}
	for i in range (1, n):
		residue = i*i % n
		if residue in res:
			res[residue].append(i)	 
		else:
			res[residue] = [i]
	return res

def is_quadratic_residue(a, p):
	"""
	Euler's criterion: Let p be an odd prime and gcd(a, p) = 1, Then a 
	is a quadratic residue of p if and only if a^((p-1) / 2) = 1 (mod p).
	
	Complexity : O(1)
	"""
	return pow(a, ((p - 1) / 2), p) == 1


def get_pickle(filename):
	with open(filename, 'rb') as f:
		obj = pickle.load(f)
	return obj;

def set_pickle(filename, variable):
	with open(filename, 'wb') as f:
		pickle.dump(variable, f)

