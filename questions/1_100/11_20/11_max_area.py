from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer, right_pointer = 0, len(height) - 1
        max_area = 0

        while left_pointer <= right_pointer:
            cur_area = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
            max_area = max(max_area, cur_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area


if __name__ == '__main__':
    height = [2, 3, 4, 5, 18, 17, 6]
    s = Solution()
    print(s.maxArea(height))
