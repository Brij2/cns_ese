#user 2 
import socket
import random

def generate_key():
    prime = 23
    primitive_root = 5
    private_key = random.randint(1, prime - 1)
    public_key = (primitive_root ** private_key) % prime
    return private_key, public_key

def send_key():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            user1_public_key = int(data.decode())
            print("\nUser 2: received User 1's public key:", user1_public_key)
            
            # Send User 2's public key to User 1
            conn.send(str(user2_public_key).encode())
            print("\nUser 2: sent their public key to User 1:", user2_public_key)
        return user1_public_key

if __name__ == "_main_":

    user2_private_key, user2_public_key = generate_key()

    host = 'localhost'
    port = 56789
    print(f"User 2:\nPublic Key:{user2_public_key}\nPrivate Key:{user2_private_key}")
    print("Receiving public key from user1...")

    user1_public_key = send_key()

    # Calculate the shared secret key for User 2
    shared_secret_key = (user1_public_key ** user2_private_key) % 23
    print("\nUser 2 : Calculated shared secret key:", shared_secret_key)