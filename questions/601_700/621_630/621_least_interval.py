# coding=utf-8

from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count_data = collections.Counter(tasks)
        max_count_num = max(tasks_count_data.values())
        max_count_tasks = sum([1 for task_count_num in tasks_count_data.values() if task_count_num == max_count_num])
        least_interval = (max_count_num - 1) * (n + 1) + max_count_tasks
        return max(least_interval, len(tasks))


if __name__ == '__main__':
    c = Solution()
    array = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(c.leastInterval(array, n))
