import datetime
import hashlib
from block import Block
import time
5
class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 2 # Nivel de dificultad para el minado
        self.create_genesis_block()

    def create_genesis_block(self):
        # El bloque genésis es el primer bloque de la cadena
        genesis_block = Block(0, "Bloque Genesis", "0")
        self.chain.append(genesis_block)
        print("Bloque Genesis creado y agregado a la cadena.")

    def get_latest_block(self):
        # Este metodo retorna el ultimo bloque de la cadena
        return self.chain[-1]
    
    def add_block(self, data):
        # 1. Obtener el hash del ultimo bloque de la cadena
        new_block = Block(len(self.chain), data, self.get_latest_block().hash)
        new_block.previous_hash = self.get_latest_block().hash

        # 2. Calcular el hash del nuevo bloque
        # Esto se hace aqui para que el hash incluya el previous_hash
        new_block.hash = new_block.calculate_hash()

        # 3. Agregar el nuevo bloque a la lista chain
        self.chain.append(new_block)
        print(f"Bloque {new_block.index} agregado a la cadena con exito.")
