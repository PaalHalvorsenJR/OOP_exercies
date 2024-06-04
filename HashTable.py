import random 

class HashTable:
    def __init__(self, capacity, primeNumber):
        self._capacity = capacity
        self._primeNumber = primeNumber
        self._scale = random.randint(1,1000)
        self.table = [None] * capacity

    def hash_function(self, key):
        hash = (key * self._scale) % self._primeNumber % self._capacity
        print(f"key: {key}, hash: {hash}")
        return hash

password = 123456789

new_key = HashTable(10, 22)

hash_value = new_key.hash_function(password)

print(f"Hash value: {hash_value}")



