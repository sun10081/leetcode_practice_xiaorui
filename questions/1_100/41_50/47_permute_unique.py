from typing import List
import itertools
import datetime


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    path.append(nums[i])
                    used[i] = True
                    print(f"递归之前 {path}")
                    dfs(nums, size, depth + 1, path, used, res)
                    path.pop()
                    used[i] = False
                    print(f"递归之后 {path}")

        size = len(nums)
        if size == 0:
            return []
        nums.sort()
        used = [False] * size
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(sequence) == n:
                ans.append(sequence[:])
                return

            for i in range(n):
                if not used[i]:
                    # i > 0 防止越界
                    # nums[i] == nums[i - 1] 选择重复项
                    # not used[i - 1] dfs到底，从后往前执行，所以当前一个重复项没有被使用时 选择前后重复项的效果相同，需要剔除
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    sequence.append(nums[i])
                    used[i] = True
                    dfs()
                    sequence.pop()
                    used[i] = False

        nums.sort()
        n = len(nums)
        ans = []
        used = [False] * n
        sequence = []
        dfs()
        return ans

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        return [list(i) for i in set(itertools.permutations(nums))]


class Solution3:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(sequence) == n:
                ans.append(sequence[:])
                return

            for i in range(n):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    sequence.append(nums[i])
                    print(sequence)
                    dfs()
                    used[i] = False
                    sequence.pop()
                    print(sequence)

        ans = []
        n = len(nums)
        sequence = []
        used = [False] * n
        nums.sort()
        dfs()
        return ans

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        return [list(array) for array in set(itertools.permutations(nums))]


if __name__ == '__main__':
    s = Solution3()
    nums = [3, 3, 0, 3]
    time1 = datetime.datetime.now()
    print(s.permuteUnique2(nums))
    time2 = datetime.datetime.now()
    print(f"耗时: {time2 - time1}")
