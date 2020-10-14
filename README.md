# Mycrypto
A CTF helper for cryptography

# Usage
	
## RSA
    mycrypto.attack_rsa(e, n, c = None, attack_types = None)
    
    where:
        e = public exponent
        n = modulus
        c = ciphertext (Plaintext will only be shown if the attack is successful)
        attack types = list of attacks which need to be performed. If empty it will try all possible attacks. 
     
    The function returns the private key (d)  if the attack is successful. 

# Example
<pre><code>
from mycrypto import *

d = mycrypto.attack_rsa(e = 3, n = 35, c = None, attack_types = ['fermat', 'wiener'])

</code></pre>


<b> Attacks Implemented</b>
1. Weiner Attack
2. Fermat Factoring Attack

## Other Utils

### Quadratic Residue

	mycrypto.is_quadratic_residue (n)


### Continued fraction

	mycrypto.get_continued_fraction_list (p, q)


### Read key file
	
	mycrypto.read_key(path)

### Read Certificate file
	
	mycrypto.read_certificate(path)


### Extended GCD
	
	mycrypto.extended_gcd(a, b)

	We know:
		ax + by = gcd(a, b)
	
	This function returns gcd(a,b), x , y 