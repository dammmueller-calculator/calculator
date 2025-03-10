import os


def xor_encrypt_decrypt(data, key):
    """Encrypt or decrypt data using XOR."""
    result = bytearray()
    key = key.encode("utf-8")  # Ensure the key is in bytes
    key_length = len(key)

    for i in range(len(data)):
        result.append(data[i] ^ key[i % key_length])

    return result


def encrypt_file(data, key, file="history.txt"):
    """Encrypt the contents of a file."""
    # Convert the data (list of strings) to bytes
    data_bytes = "\n".join(data).encode("utf-8")
    encrypted = xor_encrypt_decrypt(data_bytes, key)

    with open(file, "wb") as file:
        file.write(encrypted)


def decrypt_file(input_file, key):
    """Decrypt the contents of a file."""
    if not os.path.exists(input_file):
        return []

    with open(input_file, "rb") as file:
        data = file.read()

    decrypted_bytes = xor_encrypt_decrypt(data, key)
    # Convert decrypted bytes back to strings and split into a list
    return decrypted_bytes.decode("utf-8").split("\n")
