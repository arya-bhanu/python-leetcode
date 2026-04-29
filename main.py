class MyHashSet:
    def __init__(self):
        self.sets = set()
        return

    def add(self, key: int) -> None:
        self.sets.add(key)

    def remove(self, key: int) -> None:
        self.sets.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.sets
