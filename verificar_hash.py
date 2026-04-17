from block import Block

# 1. Creamos el bloque Génesis manualmente (Bloque 0)
genesis = Block(0, "Bloque Genesis", "0")

# 2. Extraemos la cadena de texto exacta que se hasheó
# Nota: Debe ser EXACTAMENTE la misma concatenación de tu método calculate_hash
cadena_a_verificar = str(genesis.index) + str(genesis.timestamp) + str(genesis.data) + \
                     str(genesis.previous_hash) + str(genesis.nonce)

print("--- DATOS DEL BLOQUE 0 ---")
print(f"Cadena concatenada: {cadena_a_verificar}")
print(f"Hash generado por Python: {genesis.hash}")