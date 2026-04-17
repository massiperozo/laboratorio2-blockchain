from blockchain import Blockchain
import time

# Inicializamos la blockchain (creará automáticamente el bloque génesis) [cite: 70, 96]
mi_blockchain = Blockchain()

print("\n--- INICIANDO CICLO DE MINADO INFINITO ---")

try:
    while True:
        # 1. Definimos datos para el nuevo bloque [cite: 146]
        datos = f"Transaccion numero {len(mi_blockchain.chain)}"
        
        # 2. Agregamos el bloque (esto activará la dificultad aleatoria y el minado) [cite: 143]
        mi_blockchain.add_block(datos)
        
        # 3. Obtenemos el último bloque para mostrar sus campos [cite: 74, 126]
        ultimo = mi_blockchain.get_latest_block()
        
        # 4. Mostramos los valores de los campos que conforman el bloque [cite: 147]
        print("-" * 50)
        print(f"ÍNDICE:        {ultimo.index}")
        print(f"TIMESTAMP:     {ultimo.timestamp}")
        print(f"DATOS:         {ultimo.data}")
        print(f"HASH PREVIO:   {ultimo.previous_hash}")
        print(f"NONCE:         {ultimo.nonce}")
        print(f"HASH ACTUAL:   {ultimo.hash}")
        print("-" * 50)
        
        # Pausa para poder leer los datos en la terminal [cite: 147]
        time.sleep(3) 

except KeyboardInterrupt:
    print("\nSimulación detenida por el usuario.")