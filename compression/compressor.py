
import random

"""TODO: Move it to a file maybe and add more than just uppercase characters to differ between data in the file
    but in the meanwhile this works

    TODO: Class structure

"""


lookup_table = {}


# Original data is a member in the class structure later
def get_replacement(original_data: bytes) -> bytes:
    """ Get a replacement byte and make sure it is not in the lookup table"""
    
    if (len(lookup_table.items()) == 255):
        raise Exception("Maximum characters reached in lookup table")

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

    # Open the file in text format
    with open(file=filename, mode="rb") as file_text:
        file_data = file_text.read()
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
            c = input()
        except Exception as e:
            print(e)
            break

        highest_occuring_pair, last_pair_frequency = max_pair(pairs)

        # Add the random byte to the lookup table
        lookup_table[replacement] = highest_occuring_pair
        print(lookup_table)


        # Replace two bytes with a single byte
        compressed_data = compressed_data.replace(highest_occuring_pair, replacement)

        data_len = len(compressed_data)

    print(compressed_data)
    print(lookup_table)


    with open(file=filename.replace(".xml", ".xip"), mode="wb") as compressed_file:
        compressed_file.write(compressed_data)

def decompress_binary():
    pass

compress_binary(r"C:\Users\abdel\OneDrive\Desktop\DSA-Project\compression\sample.xml")