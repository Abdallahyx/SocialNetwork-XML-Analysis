"""An XML file compressor using the XIP compression algorithm.

This class provides methods to compress an XML file to binary XIP format with a great compression ratio,
as well as decompress a binary XIP formatted file back to an XML formatted document.

Methods:
    compress_binary(filename: str) -> bytes:
        Compresses the specified XML file to binary XIP format.

    decompress_binary(compressed_bytes: bytes) -> bytes:
        Decompresses the binary XIP formatted data back to an XML formatted document.
"""