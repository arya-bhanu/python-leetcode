from typing import List

# using unassigned store


class MyHashMap:

    store: List[int]

    def __init__(self):
        self.store = [None] * 10
        return

    def put(self, key: int, value: int) -> None:
        if key >= len(self.store):
            neededLength = key + 2 - len(self.store)
            self.store = self.store + [None] * neededLength
        self.store[key] = value
        return

    def get(self, key: int) -> int:
        if key < len(self.store) and self.store[key] is not None:
            return self.store[key]
        return -1

    def remove(self, key: int) -> None:
        if key < len(self.store):
            self.store[key] = None
        return


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 100)
obj.put(2, 200)
obj.put(1000, 120000)
param_2 = obj.get(1)
obj.remove(2)

print(obj.get(1))
print(obj.get(2))
print(obj.store)
