from blockchain import Blockchain
import time

mi_blockchain = Blockchain()

while True:
    datos = "Nueva Transacción"
    mi_blockchain.add_block(datos)
    ultimo = mi_blockchain.get_latest_block()
    
    print(f"Index: {ultimo.index} | Hash: {ultimo.hash} | Prev: {ultimo.previous_hash}")
    time.sleep(2) # Pausa de 2 segundos para ver los datos