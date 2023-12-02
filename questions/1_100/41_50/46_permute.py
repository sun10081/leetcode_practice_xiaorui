import itertools
import datetime
from typing import List


class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        def dfs(size, depth, path):
            if depth == size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    print(f"递归之前 {path}")
                    dfs(size, depth + 1, path)

                    used[i] = False
                    path.pop()
                    print(f"递归之后 {path}")

        size = len(nums)
        if size == 0:
            return []
        used = [False] * size
        res = []
        dfs(size, 0, [])
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                print(f"递归之前 {nums[:]}")
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                print(f"递归之后 {nums[:]}")

        n = len(nums)
        res = []
        backtrack()
        return res


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(sequence) == n:
                ans.append(sequence[:])
                return

            for i in range(n):
                if not used[i]:
                    sequence.append(nums[i])
                    used[i] = True
                    dfs()
                    sequence.pop()
                    used[i] = False

        n = len(nums)
        ans = []
        used = [False] * n
        sequence = []
        dfs()
        return ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        return [list(i) for i in itertools.permutations(nums)]


class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(sequence) == n:
                ans.append(sequence[:])
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    sequence.append(nums[i])
                    print(sequence)
                    dfs()
                    used[i] = False
                    sequence.pop()
                    print(sequence)

        n = len(nums)
        ans = []
        used = [False] * n
        sequence = []
        dfs()
        return ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        return [list(array) for array in itertools.permutations(nums)]


class Solution4:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(sequence) == n:
                ans.append(sequence[:])
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    sequence.append(nums[i])
                    dfs()
                    sequence.pop()
                    used[i] = False

        n = len(nums)
        ans = []
        sequence = []
        used = [False] * n
        dfs()
        return ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        return [list(array) for array in itertools.permutations(nums)]


class Solution5:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(sequence) >= n:
                ans.append(sequence[:])
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    sequence.append(nums[i])
                    dfs()
                    sequence.pop()
                    used[i] = False

        n = len(nums)
        ans = []
        sequence = []
        used = [False] * n
        dfs()
        return ans


class Solution6:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(sequence) == n:
                ans.append(sequence[:])
                print(f"ans append sequence {sequence}")
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    sequence.append(nums[i])
                    print(f"append nums[i] {nums[i]}, sequence={sequence}")
                    dfs()
                    used[i] = False
                    sequence.pop()
                    print(f"after pop, sequence={sequence}")

        n = len(nums)
        sequence = []
        used = [False] * n
        ans = []
        dfs()
        return ans


class Solution7:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            print(seq)
            if len(seq) == n:
                ans.append(seq[:])
                return

            for i in range(n):
                if not uesd[i]:
                    uesd[i] = True
                    seq.append(nums[i])
                    dfs()
                    seq.pop()
                    uesd[i] = False

        n = len(nums)
        seq = []
        uesd = [False] * n
        ans = []
        dfs()
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution7()
    time1 = datetime.datetime.now()
    print(s.permute(nums))
    time2 = datetime.datetime.now()
    print(f"耗时: {time2 - time1}")
