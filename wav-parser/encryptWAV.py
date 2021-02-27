import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = b'SymphonyOfBabel_'
cipher = AES.new(key, AES.MODE_CBC, iv=b"SymphonyOfBabel_")

with open('test_files/C418 - Excursions - 06 AMS.wav', "rb") as f:
    data = f.read()

ct_bytes = cipher.encrypt(pad(data, AES.block_size))
iv = b64encode(cipher.iv).decode('utf-8')

with open('test_files/ams_encrypted', "wb") as f:
    f.write(ct_bytes)

