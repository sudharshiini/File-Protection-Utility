
from pathlib import Path
import base64
import os
import getpass

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


def generate_key(password, salt):
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1
    )

    key = kdf.derive(password.encode("utf-8"))
    return base64.urlsafe_b64encode(key)


def encrypt_file():
    filename = input("Enter file path to encrypt: ").strip().strip('"')
    path = Path(filename)

    if not path.is_file():
        print("[ERROR] File not found.")
        return

    password = getpass.getpass("Create password: ")

    if not password:
        print("[ERROR] Password cannot be empty.")
        return

    output = Path(str(path) + ".encrypted")

    if output.exists():
        print("[ERROR] Encrypted output already exists.")
        return

    try:
        data = path.read_bytes()
        salt = os.urandom(16)
        key = generate_key(password, salt)

        encrypted = Fernet(key).encrypt(data)
        output.write_bytes(b"FPU1" + salt + encrypted)

        print("[SUCCESS] File encrypted successfully!")
        print("Saved as:", output)
        print("Original file was not deleted.")

    except (OSError, ValueError) as error:
        print("[ERROR]", error)


def decrypt_file():
    filename = input("Enter encrypted file path: ").strip().strip('"')
    path = Path(filename)

    if not path.is_file():
        print("[ERROR] File not found.")
        return

    password = getpass.getpass("Enter password: ")

    output = Path(
        str(path).removesuffix(".encrypted") + ".restored"
    )

    if output.exists():
        print("[ERROR] Restored output already exists.")
        return

    try:
        content = path.read_bytes()

        if len(content) < 21 or content[:4] != b"FPU1":
            print("[ERROR] Invalid encrypted file format.")
            return

        salt = content[4:20]
        encrypted = content[20:]

        key = generate_key(password, salt)
        decrypted = Fernet(key).decrypt(encrypted)

        output.write_bytes(decrypted)

        print("[SUCCESS] File decrypted successfully!")
        print("Restored as:", output)

    except InvalidToken:
        print("[ERROR] Wrong password or damaged file.")

    except (OSError, ValueError) as error:
        print("[ERROR]", error)


def main():
    while True:
        print("\n================================")
        print("       FILE PROTECTION UTILITY")
        print("================================")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            encrypt_file()

        elif choice == "2":
            decrypt_file()

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("[ERROR] Invalid choice.")


if __name__ == "__main__":
    main()
