# File Protection Utility

## VirtualWorks Cyber Security Internship – Task 4

### Project Description
A Python-based file encryption and decryption utility that protects file contents using password-based encryption.

### Features
- Encrypts files using Fernet authenticated encryption
- Derives encryption keys from passwords using Scrypt
- Generates a random salt for each encryption
- Decrypts files using the correct password
- Detects incorrect passwords or damaged encrypted files
- Preserves original files

### Technologies Used
- Python 3
- Cryptography Library
- Visual Studio Code

### Installation

Install the required dependency:

```bash
python -m pip install cryptography
```

### How to Run

```bash
python file_protection.py
```

Select one of the options:

1. Encrypt File
2. Decrypt File
3. Exit

### Example Encryption

Input file: `sample.txt`

Encrypted output: `sample.txt.encrypted`

### Example Decryption

Encrypted input: `sample.txt.encrypted`

Restored output: `sample.txt.restored`

### Testing
The utility can be tested using a sample text file. Verify that the restored contents match the original file.

### Security Notes
- Do not share encryption passwords.
- Losing the password may make the encrypted data unrecoverable.
- The original file is retained after encryption.
- This is an educational project and has not undergone a professional security audit.

### Internship Details
VirtualWorks Cyber Security Internship

Task ID: task4