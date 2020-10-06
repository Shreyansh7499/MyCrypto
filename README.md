# Mycrypto
A CTF helper for cryptography

# Usage

    attack_rsa.attack(e, n, c = None, attack_types = None)
    
    where:
        e = public exponent
        n = modulus
        c = ciphertext (Plaintext will only be shown if the attack is successful)
        attack types = list of attacks which need to be performed. If empty it will try all possible attacks. 
     
    The function returns the private key (d)  if the attack is successful. 

# Example
<pre><code>
from attack_rsa import *

d = attack_rsa.attack(e = 3, n = 35, c = None, attack_types = ['fermat', 'wiener'])

</code></pre>
# Attacks on RSA

## Weiner Attack

## Fermat Factoring Attack
