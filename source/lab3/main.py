import random

def is_prime(n):
    """Check if number is prime"""
    if n <= 1:
        return False
    elif n > 1:
        for number in range(2, n - 1):
            if n % number == 0:
                return False
    return True

def euler_function(p, q):
    return (p - 1) * (q - 1)

def gcd(a, b):
    """Greatest common divisor"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def generate_public_key(p, q):
    """Generate public key (e, n)
    
    Approach 1:
    e is max prime number less than p (With respect to the task)
    Approach 2:
    e is a random return value (Common case)
    
    Args:
        p (int): First prime number
        q (int): Second prime number
        
    Returns:
        tuple: (e, p * q)
    """
    e = p * q
    phi = euler_function(p, q)
    
    # Approach 1
    while not is_prime(e):
        e -=1
        
    # Approach 2
    # while True:
    #     e = random.randint(2, phi - 1)
    #     if gcd(e, phi) == 1:
    #         return (e, p * q)
        
    return (e, p * q)

def generate_private_key(p, q, e):
    """Generate private key (d, n)
    
    Itterate over k until d is integer
    
    Args:
        p (int): First prime number
        q (int): Second prime number
        e (int): Public key
        
    Returns:    
        tuple: (d, p * q)
    """
    k = 1
    phi = euler_function(p, q)
    
    while True:
        d = (k * phi + 1) / e
        if d.is_integer():
            return (int(d), p * q)
        k += 1
        
def message_to_list(message):
    """Convert message to list of indices"""
    message_list = [alphabet_dict[char] for char in message if char in alphabet_dict]
    return message_list

def list_to_message(indices_list):
    """Convert list of indices to message"""
    message = ""
    index = ''
    
    for item in indices_list:
        for key, value in alphabet_dict.items():
            if str(item) == value:
                index = key
        message += index
        
    return message

def encrypt_message(indices_list):
    """Encrypt message using public key (e, n)"""
    encrypted_message = [ int(item) ** e % n for item in indices_list ]
    return encrypted_message

def decrypt_message(indices_list):  
    """Decrypt message using private key (d, n)"""  
    decrypted_message = [ int(item) ** d % n % ALPHABET_LENGTH for item in indices_list]
    return decrypted_message

# Task 1
p = 23
q = 31

e, n = generate_public_key(p, q)
d, n = generate_private_key(p, q, e)

print(f"Public key: ({e}, {n})")
print(f"Private key: ({d}, {n})")

# Task 2
# String to store ukranian alphabet
alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ_0123456789"
ALPHABET_LENGTH = len(alphabet)

# Create a dictionary to map each character to its index
alphabet_dict = {char: str(i) for i, char in enumerate(alphabet, start=1)}

message = "СЕЙФ02"
        
indices_list = message_to_list(message)
encrypted_message = encrypt_message(indices_list)
decrypted_message = decrypt_message(encrypted_message)
decrypted_message_str = list_to_message(decrypted_message)

print(indices_list)
print(encrypted_message)
print(decrypted_message)
print(decrypted_message_str)

# Task 3
cryptogram = [468, 409, 568, 1, 286, 82, 297, 40]

decrypted_message = decrypt_message(cryptogram)
ddecrypted_message_str = list_to_message(decrypted_message)

print(decrypted_message)
print(ddecrypted_message_str)