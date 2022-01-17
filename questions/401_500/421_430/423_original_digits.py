# coding=utf-8

from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        """
        s包含的字母
        ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]

        0 zero z可唯一确定
        1 one times(n) - count(7) -count(9) * 2
        2 two w可唯一确定
        3 three times(h) - count(8)
        4 four u可唯一确定
        5 five times(f) - count(4)
        6 six x可唯一确定
        7 seven times(v) - count(5)
        8 eight g可唯一确定
        9 nine times(i) - count(5) -count(6) - count(8)

        :param s:
        :return:
        """
        times = Counter(s)
        count = [0] * 10
        count[0] = times["z"]
        count[2] = times["w"]
        count[4] = times["u"]
        count[6] = times["x"]
        count[8] = times["g"]
        count[3] = times["h"] - count[8]
        count[5] = times["f"] - count[4]
        count[7] = times["v"] - count[5]
        count[9] = times["i"] - count[5] - count[6] - count[8]
        count[1] = times["n"] - count[7] - count[9] * 2

        return "".join(str(x) * count[x] for x in range(10))


if __name__ == '__main__':
    s = "nnei"
    so = Solution()
    print(so.originalDigits(s))

