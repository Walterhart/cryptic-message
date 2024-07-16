import string

def generate_mapping():
    """
    Generates the encoding and decoding dictionaries.
    """
    keys = string.ascii_lowercase + string.digits + string.punctuation + ' '
    values = keys[-1] + keys[0:-1]
    dict_e = dict(zip(keys, values))
    dict_d = dict(zip(values, keys))
    return dict_e, dict_d

def encode_message(message, dict_e):
    """
    Encodes the message .
    """
    return ''.join([dict_e.get(letter, letter) for letter in message.lower()])

def decode_message(message, dict_d):
    """
    Decodes the message .
    """
    return ''.join([dict_d.get(letter, letter) for letter in message.lower()])

def is_valid_message(message):
    """
    Validates that the message contains only valid characters.
    """
    valid_chars = set(string.ascii_lowercase + string.digits + string.punctuation + ' ')
    return all(char in valid_chars for char in message.lower())

def cryptic():
    """
    A simple encryption and decryption function based on character shifting.
    """
    dict_e, dict_d = generate_mapping()
    
    while True:
        msg = input('Enter message to be encoded or decoded: ')
        if msg.lower() == 'exit ':
            print("Exiting the program.")
            return
        if is_valid_message(msg):
            break
        else:
            print("Invalid message. Please use only letters, numbers, space, and punctuations.")

    while True:
        mode = input('Type "encode" to encode or "decode" to decode: ').strip().lower()
        if mode == 'exit':
            print("Exiting the program.")
            return
        if mode in ['encode', 'decode']:
            break
        else:
            print("Invalid input. Please type 'encode' to encode or 'decode' to decode.")

    if mode.lower() == 'encode':
        new_msg = encode_message(msg, dict_e)
    else:
        new_msg = decode_message(msg, dict_d)

    return new_msg.capitalize()

print(cryptic())
