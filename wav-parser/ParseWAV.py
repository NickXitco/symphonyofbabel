import struct
fileName = 'test_files/random.wav'


def text_read(file_object, num_bytes):
    return str(f.read(num_bytes), 'utf-8')


def num_read(file_object, num_bytes):
    bytes_read = file_object.read(num_bytes)
    return int.from_bytes(bytes_read, byteorder='little', signed=False)


with open(fileName, mode='rb') as f:
    ChunkID = text_read(f, 4)
    ChunkSize = num_read(f, 4)
    Format = text_read(f, 4)

    Subchunk1ID = text_read(f, 4)
    Subchunk1Size = num_read(f, 4)
    AudioFormat = num_read(f, 2)
    NumChannels = num_read(f, 2)
    SampleRate = num_read(f, 4)
    ByteRate = num_read(f, 4)
    BlockAlign = num_read(f, 2)
    BitsPerSample = num_read(f, 2)

    PCM = True if AudioFormat == 1 else False

    if not PCM:
        quit(1)

    Subchunk2ID = text_read(f, 4)
    Subchunk2Size = num_read(f, 4)

    # assert ChunkSize == 36 + Subchunk2Size
    # assert ChunkSize == 4 + 8 + Subchunk1Size + 8 + Subchunk2Size
    # assert ByteRate == SampleRate * NumChannels * (BitsPerSample / 8)
    # assert BlockAlign == NumChannels * (BitsPerSample / 8)

    NumSamples = int(Subchunk2Size / (NumChannels * (BitsPerSample / 8)))
    SecondsInSong = int(NumSamples / SampleRate)
    HoursInSong = int(SecondsInSong / 60 / 60)
    SecondsInSong -= HoursInSong * 60 * 60
    MinutesInSong = int(SecondsInSong / 60)
    SecondsInSong -= MinutesInSong * 60

    print(f'Number of Channels: {NumChannels}')
    print(f'Sample Rate: {SampleRate} samples/second')
    print(f'Byte Rate: {ByteRate} bytes/second')
    print(f'Block Align: {BlockAlign} bytes/sample')
    print(f'Bytes per indv. Sample: {int(BitsPerSample / 8)} bytes/sample/channel')
    print(f'Number of Samples: {NumSamples}')
    print(f'Song Length: {HoursInSong:02}:{MinutesInSong:02}:{SecondsInSong:02}')

    print(f'Seconds per KB: {(1000 / ByteRate):.03} s')
    print(f'KB per second: {(ByteRate / 1000)} KB')
    print(f'Bits per second: {(ByteRate * 8)} bits/s')


    # Rest of sound data below
