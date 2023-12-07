
import random

"""TODO: Move lookup table to a file maybe or add it to the file as overhead

    TODO: Class structure

"""


lookup_table = {}


# Original data is a member in the class structure later
def get_replacement(original_data: bytes) -> bytes:
    """ Get a replacement byte and make sure it is not in the lookup table"""

    unique_byte_count = len(set(original_data))
    
    if (len(lookup_table.items()) == (256 - unique_byte_count)):
        raise Exception("Maximum characters reached in lookup table, maximum compression reached")

    replacement = random.randbytes(1)

    if (replacement in lookup_table.keys() or replacement in original_data):
        replacement = get_replacement(original_data)

    return replacement

def max_pair(data: dict):
    max_freq: int = 0

    for key, freq in data.items():
        if (freq >= max_freq):
            max_freq = freq
            max_pair = key


    return max_pair, max_freq


def compress_binary(filename: str):
    """Open the file data as binary and try to compress it"""

    # Open the file in binary format
    with open(file=filename, mode="rb") as file_binary:
        file_data = file_binary.read()
        data_len = len(file_data)

    # Placeholder for the highest occuring object in the last loop
    last_pair_frequency = 0

    compressed_data = file_data

    while (last_pair_frequency != 1):
        pairs = {}

        # Loop through the data and make a pair-freqency dict
        for i in range(data_len - 1):
            first_iter = compressed_data[i]
            second_iter = compressed_data[i + 1]

            pair = first_iter.to_bytes() + second_iter.to_bytes()

            if (pair in pairs):
                pairs[pair] += 1

            else:
                pairs[pair] = 1
        
        try:
            replacement = get_replacement(file_data)
        except Exception as e:
            print(e)
            break

        highest_occuring_pair, last_pair_frequency = max_pair(pairs)

        # Add the random byte to the lookup table
        lookup_table[replacement] = highest_occuring_pair

        # Replace two bytes with a single byte
        compressed_data = compressed_data.replace(highest_occuring_pair, replacement)
        data_len = len(compressed_data)

    replacement_length = len(lookup_table.keys()).to_bytes()

    with open(file=filename.replace(".xml", ".xip"), mode="wb") as compressed_file:
        # Write lengh of the bytes used for compression
        compressed_file.write(replacement_length)

        compressed_file.write(compressed_data)
        
        # Add the lookup table as overhead at the end of the file
        for key, value in lookup_table.items():
            compressed_file.write(key + value)

def get_original(b: bytes):
    """Check if the byte is in the lookup table and get the original byte before decompression"""

    if (b in lookup_table.keys()):
        b1: bytes = get_original(lookup_table[b][0].to_bytes())
        b2: bytes = get_original(lookup_table[b][1].to_bytes())

        return b1 + b2

    return b
    

def decompress_binary(filename: str):
    """ Decompress the file back tp its original format """
    
    with open(file=filename, mode="rb") as file_binary:
        file_data = file_binary.read()

    decompressed_data = b""

    # Use the redundant information to construct dict
    print(lookup_table)

    print(file_data[0])
    print(file_data[-3 * file_data[0]].to_bytes())
    # Iterate through every file in the compressed file and find every byte in the lookup table recursively
    for i in range(len(file_data)):
        decompressed_data += get_original(file_data[i].to_bytes())


    with open(file=filename.replace(".xip", "_decompressed.xml"), mode="wb") as decompressed_file:
        decompressed_file.write(decompressed_data)



if (__name__ == "__main__"):
    print("Compressing...")
    compress_binary(r"C:\Users\abdel\OneDrive\Desktop\DSA-Project\compression\sample.xml")

    print("Decompressing...")
    decompress_binary(r"C:\Users\abdel\OneDrive\Desktop\DSA-Project\compression\sample.xip")
