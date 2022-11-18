class SymbolTable:
    def __init__(self):
        self.capacity = 3
        self.size = 0
        self.values = [[] for _ in range(self.capacity)]

    def hash(self, key):
        char_sum = 0

        # For each character in the key
        for character in key:
            char_sum += ord(character)

        return char_sum % self.capacity

    def resize(self, new_capacity):
        old_buckets = self.values

        self.size = 0
        self.capacity = new_capacity
        self.values = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for node in bucket:
                self.insert(node[0], node[1])

    def insert(self, key, value):
        # 0. Resize
        if self.size / self.capacity > 0.7:
            self.resize(self.capacity * 2)

        # 1. Increment size
        self.size = self.size + 1

        # 2. Compute hash value of key
        index = self.hash(key)

        if key in self.values[index]:
            return

        # Add a new node at the end of the list with provided key/value
        self.values[index].append([key, value])

    def remove(self, key):
        # 1. Compute hash
        index = self.hash(key)

        filtered = [node for node in self.values[index] if node[0] != key]

        if len(self.values) != len(filtered):
            self.values[index] = filtered
            self.size = self.size - 1

        # Resize
        if self.size / self.capacity < 0.25:
            self.resize(self.capacity * 2)

    def __contains__(self, key):
        # 1. Compute hash
        index = self.hash(key)

        return key in self.values[index]

    def find(self, key):
        # 1. Compute hash
        index = self.hash(key)

        found_value = [node for node in self.values[index] if node[0] == key]
        if found_value:
            return found_value[0]
        else:
            return None


def tests():
    st = SymbolTable()
    assert(st.size == 0)
    assert(st.capacity == 3)
    assert(st.find("A") is None)

    st.insert("A", 10)
    assert(st.find("A") == ["A", 10])

    st.insert("a", 6)
    st.insert("b", 7)
    st.insert("c", 8)

    assert(st.size == 4)
    assert(st.capacity == 6)

    st.remove("A")
    assert(st.size == 3)
    assert(st.find("A") is None)


if __name__ == '__main__':
    tests()
