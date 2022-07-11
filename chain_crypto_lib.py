from Crypto.Cipher import DES
from Crypto.Hash import MD5
from binascii import unhexlify

class DES_tool:

    def __init__(self, key):
        self.alg = DES.new(key)

    def encrypt(self, plain):
        while len(plain) % 8 != 0:
            plain = plain + "~"
        return self.alg.encrypt(plain).hex()

    def decrypt(self, cipher):
        return self.alg.decrypt(unhexlify(cipher)).decode('utf-8')

class MD5_tool:
    def hash_text(self,text):
        h = MD5.new()
        h.update(text.encode('utf-8'))
        return h.hexdigest()
