# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2512_reward_top_k_students.py
@time: 2023-10-11 10:02:45 
"""
from typing import List
from collections import defaultdict


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        desc = defaultdict(int)
        for feedback in positive_feedback:
            desc[feedback] = 3
        for feedback in negative_feedback:
            desc[feedback] = -1
        array = [[stu_id, 0] for stu_id in student_id]
        for i, re in enumerate(report):
            temp_arr = re.split()
            for word in temp_arr:
                if word in desc:
                    array[i][1] += desc[word]
        array.sort(key=lambda x: (-x[1], x[0]))
        return [stu_id for stu_id, _ in array][:k]


if __name__ == '__main__':
    s = Solution()
    positive_feedback = ["smart", "brilliant", "studious"]
    negative_feedback = ["not"]
    report = ["this student is studious", "the student is smart"]
    student_id = [1, 2]
    k = 2
    print(s.topStudents(positive_feedback, negative_feedback, report, student_id, k))