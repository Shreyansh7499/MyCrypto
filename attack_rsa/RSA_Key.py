#!/usr/bin/env python3

import gmpy
from Crypto.Util.number import *


class RSA_Key:

	def __init__(self, e, n, p = None, q = None, d = None):
		self.e = e
		self.n = n
		self.p = p
		self.q = q
		self.d = d

	def calculate_private_key(self):
		if self.d:
			return True
		elif self.p and self.q:
			phi = (self.p - 1) * (self.q - 1)
			self.d = inverse(self.e, phi)
			return True
		return False

	def decode_message(self, c):
		if self.calculate_private_key():
			print(f"Flag : { long_to_bytes(pow(c, self.d, self.n)) } ")
		else:
			print("Cannot Decode Message")

