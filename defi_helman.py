# defi helman
from cryptography.hazmat.primitives.asymmetric import dh

# Generate a Diffie-Hellman parameters object with a larger key size (e.g., 2048 bits)
parameters = dh.generate_parameters(generator=2, key_size=2048)

# Generate private and public keys for Alice and Bob
alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()

bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()

# Calculate the shared secret key on both sides
alice_shared_key = alice_private_key.exchange(bob_public_key)
bob_shared_key = bob_private_key.exchange(alice_public_key)

# The shared secrets should be the same
print("Shared Secret (Alice):", int.from_bytes(alice_shared_key, "big"))
print("Shared Secret (Bob):", int.from_bytes(bob_shared_key, "big"))


