# Hash SHA-256 
hex_v = "bd86880a874f867a7026438b1892a0db7fe6bc80de58103764440b8782208825"

# Extraindo os primeiros 128 bits
k = hex_v[:32]

print("Chave k:", k)