from cipher_lyc2121 import cipher_lyc2121

def test_cipher_singleword():
    actual = cipher('Potato', 2, encrypt=True)
    expected = 'Rqvcvq'
    assert actual == expected

test_cipher_singleword()
