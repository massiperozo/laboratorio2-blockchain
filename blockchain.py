import datetime
import hashlib
import random
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 2 # Nivel de ceros iniciales requeridos [cite: 67, 96]
        self.create_genesis_block()

    def create_genesis_block(self):
        # El bloque 0 siempre tiene previous_hash "0" [cite: 72]
        genesis_block = Block(0, "Bloque Genesis", "0")
        self.chain.append(genesis_block) 

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        # Cambiamos el valor de self.difficulty aleatoriamente para este bloque
        self.difficulty = random.randint(1, 4) 
        print(f"\n[SISTEMA] Dificultad aleatoria establecida en: {self.difficulty}")

        # Creamos el bloque con el hash del último bloque de la cadena [cite: 78, 130]
        new_block = Block(len(self.chain), data, self.get_latest_block().hash)
        
        # El nonce empezará a subir dentro de mine_block hasta hallar el hash 
        new_block.mine_block(self.difficulty)
        
        # Agregamos el bloque ya minado a la lista [cite: 80, 134]
        self.chain.append(new_block)
        print(f"Bloque {new_block.index} agregado con éxito.")