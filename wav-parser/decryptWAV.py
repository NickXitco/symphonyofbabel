from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'SymphonyOfBabel_'


with open('test_files/ams_encrypted', "rb") as f:
    ciphertext = f.read()


iv = "SymphonySymphonySymphony"
cipher = AES.new(key, AES.MODE_CBC, iv=b"SymphonyOfBabel_")
pt = cipher.decrypt(ciphertext)

with open('test_files/ams_decrypted.wav', "wb") as f:
    f.write(pt)

