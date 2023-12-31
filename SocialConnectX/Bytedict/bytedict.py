class ByteDict:
    """
    Implementation for a dictionary-like data structure.
    """

    def __init__(self, size=1000):
        # Initialize the storage as a list of empty lists
        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0

    def __setitem__(self, key, value):
        # Calculate the storage index based on the key's hash
        storage_id = hash(key) % self.size
        for ele in self.storage[storage_id]:
            if key == ele[0]:  # If the key already exists, update its value
                ele[1] = value
                break
        else:
            # If the key doesn't exist, append a new key-value pair
            self.storage[storage_id].append([key, value])
            self.length += 1

    def __getitem__(self, key):
        # Calculate the storage index based on the key's hash
        storage_id = hash(key) % self.size
        for ele in self.storage[storage_id]:
            if ele[0] == key:
                return ele[1]

        # Raise a KeyError if the key doesn't exist
        raise KeyError("Key {} does not exist".format(key))

    def __delitem__(self, key):
        # Calculate the storage index based on the key's hash
        storage_id = hash(key) % self.size
        for sub_lst in self.storage[storage_id]:
            if key == sub_lst[0]:
                # Remove the key-value pair from the storage
                self.storage[storage_id].remove(sub_lst)
                self.length -= 1
                return

        # Raise a KeyError if the key doesn't exist
        raise KeyError("Key {} does not exist".format(key))

    def __contains__(self, key):
        # Calculate the storage index based on the key's hash
        storage_idx = hash(key) % self.size
        for item in self.storage[storage_idx]:
            if item[0] == key:
                return True
        return False

    def __len__(self):
        # Return the number of key-value pairs in the storage
        return self.length

    def __iterate_kv(self):
        # Helper method to iterate over all key-value pairs in the storage
        for sub_lst in self.storage:
            if not sub_lst:
                continue
            for item in sub_lst:
                yield item

    def __iter__(self):
        # Iterate over all keys in the storage
        for key_var in self.__iterate_kv():
            yield key_var[0]

    def keys(self):
        # Return an iterator over all keys in the storage
        return self.__iter__()

    def values(self):
        # Return an iterator over all values in the storage
        for key_var in self.__iterate_kv():
            yield key_var[1]

    def items(self):
        # Return an iterator over all key-value pairs in the storage
        return self.__iterate_kv()

    def get(self, key):
        try:
            # Get the value associated with the key
            return self.__getitem__(key)
        except KeyError:
            # Return None if the key doesn't exist
            return None
