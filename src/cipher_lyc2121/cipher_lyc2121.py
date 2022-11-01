def cipher(text, shift, encrypt=True):
    """
    replaces each letter by some fixed number
    of positions down the alphabet to ultimately create a cipher.

    Parameters
    ----------
    text : string
    A string you would like to cipher
    shift: integer
    The fixed number of positions down the alphabet to go
    encrypt: True or False
    Value for whether you would like to encrypt or decrypt.

    Returns
    ---------
    An encrypted or decrypted string

    Examples
    ---------
    >>>from cipher_lyc2121 import lyc2121
    >>> cipher('Potato', 2, encrypt=True)
    'Rqvcvq'
    """
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
