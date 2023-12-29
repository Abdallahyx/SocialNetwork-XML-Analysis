
import random

from structures.bytedict import ByteDict

"""
    TODO: Class structure

"""

class XIPCompressor():
    """ an XML file compressor

        Methods: compress_binary(filename: str)
            Used to compress an XML file to binary XIP format with a greate compression ratio

                decompress_binary(filepath: str)
            Used to decompress binary XIP formatted file to an XML formatted document
    """

    __instance = None
    
    def __new__(cls):
        if (cls.__instance is None):
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        self.__lookup_table = ByteDict(256)

        self.__raw_file_data: bytes = None


    # Original data is a member in the class structure later
    def __get_replacement(self) -> bytes:
        """ Get a replacement byte and make sure it is not in the lookup table"""

        unique_byte_count = len(set(self.__raw_file_data))
        
        if (len(self.__lookup_table) == (256 - unique_byte_count)):
            raise Exception("Maximum characters reached in lookup table, maximum compression reached")

        replacement = random.randbytes(1)

        if (replacement in self.__lookup_table.keys() or replacement in self.__raw_file_data):
            replacement = self.__get_replacement()

        return replacement

    def __get_original(self, b: bytes, table: dict):
        """Check if the byte is in the lookup table and get the original byte before decompression"""

        if (b in table.keys()):
            b1: bytes = self.__get_original(table[b][0].to_bytes(), table)
            b2: bytes = self.__get_original(table[b][1].to_bytes(), table)

            return b1 + b2

        return b

    def __max_pair(self, data: ByteDict):
        max_freq: int = 0

        for key, freq in data.items():
            if (freq >= max_freq):
                max_freq = freq
                max_pair = key


        return max_pair, max_freq

    def __reconstruct_dict(self, data: bytes):
        """Used to reconstruct the lookup table from the data found in the compressed file"""

        byte_len = data[0]
        table_chunk = data[(-3 * byte_len):]

        table = ByteDict()

        for i in range(0, 3 * byte_len, 3):
            table[table_chunk[i].to_bytes()] = table_chunk[i + 1].to_bytes() + table_chunk[i + 2].to_bytes()

        return table



    def compress_binary(self, filename: str):
        """Open the file data as binary and try to compress it"""

        # Open the file in binary format
        with open(file=filename, mode="rb") as file_binary:
            self.__raw_file_data = file_binary.read()
            data_len = len(self.__raw_file_data)

        # Placeholder for the highest occuring object in the last loop
        last_pair_frequency = 0

        compressed_data = self.__raw_file_data

        while (last_pair_frequency != 1):
            pairs = ByteDict(len(compressed_data))

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
                replacement = self.__get_replacement()
            except Exception as e:
                print(e)
                break

            highest_occuring_pair, last_pair_frequency = self.__max_pair(pairs)

            # Add the random byte to the lookup table
            self.__lookup_table[replacement] = highest_occuring_pair

            # Replace two bytes with a single byte
            compressed_data = compressed_data.replace(highest_occuring_pair, replacement)
            data_len = len(compressed_data)

        replacement_length = len(self.__lookup_table).to_bytes()

        #with open(file=filename.replace(".xml", ".xip"), mode="wb") as compressed_file:
            # Write lengh of the bytes used for compression
        #    compressed_file.write(replacement_length)

        #    compressed_file.write(compressed_data)
            
            # Add the lookup table as overhead at the end of the file
        #    for key, value in self.__lookup_table.items():
        #        compressed_file.write(key + value)

        compressed_output = replacement_length + compressed_data

        for key, value in self.__lookup_table.items():
            compressed_output += (key + value)

        return compressed_output
        

    def decompress_binary(self, compressed_bytes: bytes):
        """ Decompress the file back tp its original format """

        decompressed_data = b""

        # Use the redundant information to construct dict before decompression
        reconstruction_dict = self.__reconstruct_dict(compressed_bytes)
        data_len = len(compressed_bytes) - len(reconstruction_dict) * 3

        # Iterate through every file in the compressed file and find every byte in the lookup table recursively
        for i in range(1, data_len):
            decompressed_data += self.__get_original(compressed_bytes[i].to_bytes(), reconstruction_dict)


        return decompressed_data
