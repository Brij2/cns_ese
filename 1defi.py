#user 1
import socket
import random
import time

def generate_key():
    prime = 23
    primitive_root = 5
    private_key = random.randint(1, prime - 1)
    public_key = (primitive_root ** private_key) % prime
    return private_key, public_key

def send_key():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(str(user1_public_key).encode())
        print("\nUser 1: sent their public key to User 2:", user1_public_key)
        print("Sending...")
        time.sleep(3)

        # Receive User 2's public key
        data = s.recv(1024)
        user2_public_key = int(data.decode())
        print("\nReceiving public key from user 2...")
        print("User 1: received User 2's public key:", user2_public_key)
        return user2_public_key

if __name__ == "_main_":

    user1_private_key, user1_public_key = generate_key()

    host = 'localhost'
    port = 56789
    print(f"User 1:\nPublic Key:{user1_public_key}\nPrivate Key:{user1_private_key}")
    # Calculate the shared secret key for User 1

    user2_public_key = send_key()
    shared_secret_key = (user2_public_key ** user1_private_key) % 23
    print("\nCalculating shared secret key...")
    time.sleep(3)
    print("User 1: Calculated shared secret key:", shared_secret_key)