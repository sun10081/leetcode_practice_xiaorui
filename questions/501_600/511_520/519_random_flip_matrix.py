import random
from typing import List


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self) -> List[int]:
        x = random.randint(0, self.total - 1)
        self.total -= 1
        idx = self.map.get(x, x)
        self.map[x] = self.map.get(self.total, self.total)
        return list(divmod(idx, self.n))

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()


if __name__ == '__main__':
    s = Solution(3, 1)
    print(s.flip())
    print(s.flip())
    print(s.flip())
    print(s.reset())
