import math
import struct
import random

with open('test_files/random.wav', mode='wb') as f:
    f.write(b"RIFF")                           # ChunkID
    f.write(struct.pack('<L', 96036))          # ChunkSize
    f.write(b"WAVE")                           # Format
    f.write(struct.pack('>L', 0x666d7420))     # Subchunk1ID
    f.write(struct.pack('<L', 0x00000010))     # Subchunk1 Size
    f.write(struct.pack('<L', 0x00010001))     # AudioFormat and NumChannels
    f.write(struct.pack('<L', 0x00003E80))     # Sample Rate
    f.write(struct.pack('<L', 0x00003E80))     # Byte Rate
    f.write(struct.pack('<L', 0x00080001))     # Bits Per Sample and Block Align
    f.write(b"data")                           # Subchunk2ID
    f.write(struct.pack('<L', 960000))         # SubchunkSize

    for i in range(int(960000 / 4)):
        f.write(struct.pack('<L', random.randint(0x00000000, 0xFFFFFFFF)))

