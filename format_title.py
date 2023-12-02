# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: format_title
@time: 2021/12/27 10:10 上午
@desc: 
"""
import datetime
import logging
import os.path
from typing import List

logging.basicConfig(level=logging.INFO)

PYTHON_PATH = "/Users/guoxiaorui/python-project/leetcode_practice_xiaorui/questions"
GO_PATH = "/Users/guoxiaorui/go/leetcode"
JAVA_PATH = "/Users/guoxiaorui/leetcode_java/src/leetcode/"


def execute(title: str, num: int, language: str):
    formatted_title = format_title(title, num, language)
    file_path_list = generate_file_path(formatted_title, num, language)
    create_dir(file_path_list, language)


def format_title(title: str, num: int, language: str) -> str:
    if language == "java":
        return format_title_java(title, num)
    else:
        return format_title_python(title, num, language)


def format_title_python(title: str, num: int, language: str) -> str:
    s_arr = list(title)
    for index, _ in enumerate(s_arr):
        if s_arr[index].isupper():
            s_arr[index] = s_arr[index].lower()
        elif s_arr[index] == "-":
            s_arr[index] = '_'
    ans = f"{num}_" + "".join(s_arr)
    ans = ans + ".py" if language == "python" else ans + ".go"
    logging.info(ans)
    return ans


def format_title_java(title: str, num: int) -> str:
    s_arr = list(title)
    for i in range(len(s_arr)):
        if i == 0 or s_arr[i - 1] == "-":
            s_arr[i] = s_arr[i].upper()
    s_tmp = "".join(s_arr).replace("-", "")
    ans = "leetcode_" + str(num) + "_" + "".join(s_tmp)
    ans += ".java"
    logging.info(ans)
    return ans


def generate_file_path(title: str, num: int, language: str) -> List[str]:
    ans = []
    prefix = "leetcode_" if language == "java" else ""
    # 百
    hundred = num // 100
    if hundred:
        ans.append(prefix + str(hundred) + "01_" + str(hundred + 1) + "00")
    else:
        ans.append(prefix + "1_" + str(hundred + 1) + "00")
    # 十
    ten = num // 10
    ans.append(prefix + str(ten) + "1_" + str(ten + 1) + "0")
    # 标题
    ans.append(title)
    logging.info(ans)
    return ans


def create_dir(file_path_list: List[str], language: str):
    if language == "python":
        path = PYTHON_PATH
    elif language == "go":
        path = GO_PATH
    else:
        path = JAVA_PATH

    for index, file_path in enumerate(file_path_list):
        path = os.path.join(path, file_path)
        if index < len(file_path_list) - 1:
            if not os.path.exists(path):
                os.mkdir(path)
                if language == "python":
                    init_file_path = os.path.join(path, "__init__.py")
                    create_file(init_file_path, language)
        else:
            create_file(path, language)


def create_file(file_path: str, language: str):
    f = open(file_path, 'w')
    file_pre = []
    if language == "python":
        file_pre = ["# -*- coding:utf-8 -*-\n", '"""\n', '@author: guoxiaorui\n',
                    f'@file: {file_path.split("/")[-1]}\n',
                    f'@time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} \n', '"""\n']
    elif language == "go":
        # package = file_path.split("/")[-2]
        # package_arr = list(package)
        # package_arr[0] = '_'
        # file_pre = [f'{"package " + "".join(package_arr)}']
        file_pre = ['package main']
    elif language == "java":
        # package leetcode.leetcode_1601_1700.leetcode_1621_1630;
        package = "package leetcode." + file_path.split("/")[-3] + "." + file_path.split("/")[-2] + ";"
        java_class_name = file_path.split("/")[-1].split(".")[0]
        file_pre = [f"{package}\n", "\n", f"public class {java_class_name} " + "{\n", "\n", "}\n"]
    f.writelines(file_pre)
    f.close()

def random_num(a):
    import random
    from collections import defaultdict

    success_count = 0
    fail_count = 0
    max_success = 0
    max_fail = 0
    max_fail_count = 0
    count = defaultdict(int)

    for i in range(a):
        num = random.randint(0, 99)
        if num < 22:
            success_count += 1
            count[1] += 1
            max_fail = max(max_fail, count[0])
            if count[0] >= 10:
                max_fail_count += 1
            count[0] = 0
        else:
            fail_count += 1
            count[0] += 1
            max_success = max(max_success,count[1])
            count[1] = 0

    print(f"success_count={success_count}, fail_count={fail_count}")
    print(f"max_success={max_success}, max_fail={max_fail}")
    print(f"max_fail_count={max_fail_count}")


if __name__ == '__main__':
    num = 1093
    title = "car-pooling"
    execute(title, num, "python")

    # execute(title, num, "go")
    # execute(title, num, "java")

