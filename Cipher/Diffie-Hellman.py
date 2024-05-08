import random

def mod_exp(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def generate_private_key():
    return random.randint(2, prime - 2)

def generate_public_key(base, private_key, prime):
    return mod_exp(base, private_key, prime)

def compute_shared_secret(public_key, private_key, prime):
    return mod_exp(public_key, private_key, prime)

prime = 29
base = 55

alice_private_key = generate_private_key()
alice_public_key = generate_public_key(base, alice_private_key, prime)

bob_private_key = generate_private_key()
bob_public_key = generate_public_key(base, bob_private_key, prime)

alice_shared_secret = compute_shared_secret(bob_public_key, alice_private_key, prime)

bob_shared_secret = compute_shared_secret(alice_public_key, bob_private_key, prime)

print("Alice's private key:", alice_private_key)
print("Alice's public key:", alice_public_key)
print("Bob's private key:", bob_private_key)
print("Bob's public key:", bob_public_key)
print("Shared secret (computed by Alice):", alice_shared_secret)
print("Shared secret (computed by Bob):", bob_shared_secret)
