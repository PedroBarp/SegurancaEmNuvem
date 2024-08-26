from Crypto.Cipher import AES
from Crypto.Util import Counter, Padding
from binascii import hexlify, unhexlify
import os

# Dado fornecido
key = unhexlify('33A18467DB4AF474B051523A73DDA955')

# Texto claro 
plaintext = 'Pedro Henrique Dornhauser Barp'.encode('utf-8')

# Gerar um contador (IV) aleatório de 128 bits
iv = os.urandom(16)
ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))

# Adicionar padding para garantir que o tamanho seja múltiplo de 16 bytes
plaintext = Padding.pad(plaintext, 16)

# Configurando o AES em modo CTR
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

# Cifrando o texto claro
ciphertext = cipher.encrypt(plaintext)

# Convertendo IV e texto cifrado para hexadecimal
iv_hex = hexlify(iv).decode('utf-8')
ciphertext_hex = hexlify(ciphertext).decode('utf-8')

print("IV (hex):", iv_hex)
print("Texto cifrado (hex):", ciphertext_hex)