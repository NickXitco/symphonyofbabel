from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

INPUT_FILE = "test_files/quizzed.wav"

key = b"SymphonyOfBabel_"
cipher = AES.new(key, AES.MODE_CBC, iv=b"SymphonyOfBabel_")

with open(INPUT_FILE, "rb") as f:
    header = f.read(44)
    data = f.read()

ct_bytes = cipher.encrypt(pad(data, AES.block_size))
iv = b64encode(cipher.iv).decode('utf-8')

performerName = ct_bytes[:100].decode("cp437")
songTitle = ct_bytes[100:200].decode("cp437")
date = int.from_bytes(ct_bytes[200:208], "big")
trackNumber = int.from_bytes(ct_bytes[208:210], "big")
image = ct_bytes[210:960000]

print(f"PerformerName ({len(performerName)}): {performerName}")
print(f"SongTitle ({len(songTitle)}): {songTitle}")
print(f"Date: {date}")
print(f"Track: {trackNumber}")

cipher = AES.new(key, AES.MODE_CBC, iv=b"SymphonyOfBabel_")
pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)

with open('test_files/quizzed_decrypted.wav', "wb") as f:
    f.write(header)
    f.write(pt)

