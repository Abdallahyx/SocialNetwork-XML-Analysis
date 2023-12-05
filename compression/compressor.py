
import random
import string

"""TODO: Move it to a file maybe and add more than just uppercase characters to differ between data in the file
    but in the meanwhile this works

    TODO: Class structure

"""


lookup_table = {}


def get_replacement():
    """ Get a replacement byte and make sure it is not in the lookup table"""
    
    if (len(lookup_table.items()) == 26):
        raise Exception("Maximum characters reached in lookup table")

    replacement = random.choice(string.ascii_uppercase)

    if (replacement in lookup_table.keys()):
        replacement = get_replacement()

    return replacement

def max_pair(data: dict):
    max_freq: int = 0

    for key, freq in data.items():
        if (freq >= max_freq):
            max_freq = freq
            max_pair = key


    return max_pair, max_freq


def compress_text(filename: str):
    """Open the file data as text and try to compress it"""

    # Open the file in text format
    with open(file=filename, mode="r") as file_binary:
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

            pair = first_iter + second_iter

            if (pair in pairs):
                pairs[pair] += 1

            else:
                pairs[pair] = 1

        highest_occuring_pair, last_pair_frequency = max_pair(pairs)
        
        try:
            replacement = get_replacement()
        except Exception as e:
            print(e)
            break

        # Add the random byte to the lookup table
        lookup_table[replacement] = highest_occuring_pair

        # Replace two characters with a sigle byte
        compressed_data = compressed_data.replace(highest_occuring_pair, replacement)
        data_len = len(compressed_data)

    print(compressed_data)
    print(lookup_table)


    with open(file=filename.replace(".xml", ".xip"), mode="w") as compressed_file:
        compressed_file.write(compressed_data)

compress_text("./sample.xml")