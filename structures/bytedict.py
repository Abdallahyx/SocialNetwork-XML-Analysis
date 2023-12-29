

class ByteDict():
    """
    implementation for dict
    """

    def __init__(self, size=1000):

        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0

    def __setitem__(self, key, value):
        storage_id = hash(key) % self.size
        for ele in self.storage[storage_id]:
            if key == ele[0]:  # already exist, update it
                ele[1] = value
                break
        else:
            self.storage[storage_id].append([key, value])
            self.length += 1
    
    def __getitem__(self, key):

        storage_id = hash(key) % self.size
        for ele in self.storage[storage_id]:
            if ele[0] == key:
                return ele[1]

        raise KeyError('Key {} dont exist'.format(key))

    def __delitem__(self, key):

        storage_id = hash(key) % self.size
        for sub_lst in self.storage[storage_id]:
            if key == sub_lst[0]:
                self.storage[storage_id].remove(sub_lst)
                self.length -= 1
                return

        raise KeyError('Key {} dont exist'.format(key))

    def __contains__(self, key):
  
        storage_idx = hash(key) % self.size
        for item in self.storage[storage_idx]:
            if item[0] == key:
                return True
        return False

    def __len__(self):

        return self.length

    def __iterate_kv(self):

        for sub_lst in self.storage:
            if not sub_lst:
                continue
            for item in sub_lst:
                yield item

    def __iter__(self):

        for key_var in self.__iterate_kv():
            yield key_var[0]

    def keys(self):

        return self.__iter__()

    def values(self):

        for key_var in self.__iterate_kv():
            yield key_var[1]

    def items(self):

        return self.__iterate_kv()

    def get(self, key):

        try:
            return self.__getitem__(key)
        except KeyError:
            return None
