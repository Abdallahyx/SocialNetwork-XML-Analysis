from compression.compressor import XIPCompressor

data = XIPCompressor().compress_binary(r"C:\Users\abdel\OneDrive\Desktop\DSA-Project\compression\sample.xml")


print(XIPCompressor().decompress_binary(data).decode())