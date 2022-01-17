# coding=utf-8


from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time_sum = 0
        expired = 0

        for i in range(len(timeSeries)):
            if timeSeries[i] >= expired:
                time_sum += duration
            else:
                time_sum += timeSeries[i] + duration - expired
            expired = timeSeries[i] + duration
        return time_sum


if __name__ == '__main__':
    timeSeries = [1, 2]
    duration = 2
    s= Solution()
    print(s.findPoisonedDuration(timeSeries, duration))
