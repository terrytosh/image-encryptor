class XorEncryptor:
    def __init__(self):
        self.key = 0x5A # Example encryption key

    def encrypt(self, data):
        encrypted_data = bytes([b ^ self.key for b in data])
        return encrypted_data