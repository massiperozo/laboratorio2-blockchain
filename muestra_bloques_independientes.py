from block import Block

# Creamos dos bloques que no están conectados
bloque1 = Block(1, "Datos del Bloque 1", "0")
bloque2 = Block(2, "Datos del Bloque 2", "abcde12345")

print(f"Bloque 1 - Hash: {bloque1.hash}")
print(f"Bloque 2 - Hash: {bloque2.hash}")