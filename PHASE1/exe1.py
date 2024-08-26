from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Dados fornecidos (convertidos para bytes)
key = bytes.fromhex('240B31B44A27BEC5062B3A74C63271A4')
ciphertext = bytes.fromhex('EF794476D605765572683CE849FBD4555CE8EC1382019662E277F31B8035E285787C1DA9D2CC5B3441F5CB900C41BA70902A932209C3966B83FB4387ABBC95E0')
iv = bytes.fromhex('C4AB0DF3D808D72AAADBC68206483B18')

# Criar o objeto de cifra AES em modo CBC
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decifrar o texto
plaintext = cipher.decrypt(ciphertext)

# Remover o padding
plaintext = unpad(plaintext, AES.block_size)

# Converter para string UTF-8
plaintext_str = plaintext.decode('utf-8')

# Texto claro
print(plaintext_str)
