import hashlib
import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Concatenar atributos para el hash [cite: 50, 54]
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + \
                       str(self.previous_hash) + str(self.nonce)
        # Retornar hash en formato hexadecimal [cite: 51, 52, 54]
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Para el punto 4.2.6 (Minería)
    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Bloque minado: {self.hash}")