# coding=utf-8


class MapSum:

    def __init__(self):
        self.map = {}
        self.prefixmap = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta = val - self.map[key]
        self.map[key] = val
        for i in range(len(key)):
            currprefix = key[0:i + 1]
            if currprefix in self.prefixmap:
                self.prefixmap[currprefix] += delta
            else:
                self.prefixmap[currprefix] = delta

    def sum(self, prefix: str) -> int:
        if prefix in self.prefixmap:
            return self.prefixmap[prefix]
        else:
            return 0
