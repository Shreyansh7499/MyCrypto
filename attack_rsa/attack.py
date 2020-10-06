#!/usr/bin/env python3

import gmpy
from .RSA_Key import RSA_Key
from .fermat_factoring import Fermat_Factoring_Attack
from .wiener import wiener_attack

Possible_attacks = ['fermat', 'wiener']

def attack_util(key, attack_type):
	
	if attack_type == 'fermat':
		return Fermat_Factoring_Attack(key)
	if attack_type == 'wiener':
		return wiener_attack(key)


def attack(e, n, c = None, attack_types = None):
	
	key = RSA_Key(e, n)

	if not attack_types:
		attack_types = Possible_attacks

	for attack_type in attack_types:
		print(f"Trying { attack_type } .. ")

		res = attack_util(key, attack_type)
		if (res["Possible"]):
			print(f"{attack_type} Successfull")
			if c:
				res["Key"].decode_message(c)
			return res["Key"]
		print(f"{ attack_type } Attack Failed :( ")