# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2_findAllRecipes
@time: 2021/12/25 10:33 下午
@desc: 
"""
import bisect
import collections
from typing import List
from collections import defaultdict, deque


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def dfs(ingredient: str) -> bool:
            index = -1
            for i in range(n):
                if recipes[i] == ingredient:
                    index = i
                    break
            if index == -1:
                if ingredient not in supplies:
                    return False
                else:
                    return True
            else:
                for i in ingredients[index]:
                    if not dfs(i):
                        return False
            return True

        n = len(recipes)
        ans = []
        for i in range(n):
            f = True
            for ing in ingredients[i]:
                if not dfs(ing):
                    f = False
                    break
            if f:
                ans.append(recipes[i])
        return ans


class Solution2:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def get_index(ingredient: str) -> int:
            for i in range(n):
                if recipes[i] == ingredient:
                    return i

        n = len(recipes)
        ans = []
        for i in range(n):
            flag = True
            queue = []
            for ingredient in ingredients[i]:
                if ingredient in recipes:
                    if ingredient in ans:
                        continue
                    else:
                        index = get_index(ingredient)
                        queue.append([index, ingredient])
                else:
                    if ingredient not in supplies:
                        flag = False
                        break

            while flag and queue:
                index, recipe = queue.pop(0)
                if recipe in ans:
                    continue
                else:
                    for ingredient in ingredients[index]:
                        if ingredient in recipes:
                            index = get_index(ingredient)
                            queue.append([index, ingredient])
                        else:
                            if ingredient not in supplies:
                                flag = False
                                break
            if flag:
                ans.append(recipes[i])
        return ans


class Solution3:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # 建图 记录入度
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, vs in zip(recipes, ingredients):
            for v in vs:
                graph[v].append(u)
                indegree[u] += 1

        # 将原材料作为迭代的起始点【题目已满足：给定的原材料在图中的入度均为0】
        deque = collections.deque(supplies)

        # 从原材料开始迭代，并更新indegree
        while deque:
            cur = deque.popleft()
            for nxt in graph[cur]:  # 遍历当前 cur 节点的邻居/子代节点
                indegree[nxt] -= 1
                if indegree[nxt] == 0:  # indegree=0则加入队列
                    deque.append(nxt)

        res = [rec for rec in recipes if indegree[rec] == 0]
        return res


if __name__ == '__main__':
    # recipes = ["xevvq", "izcad", "p", "we", "bxgnm", "vpio", "i", "hjvu", "igi", "anp", "tokfq", "z", "kwdmb", "g",
    #            "qb", "q",
    #            "b", "hthy"]
    # ingredients = [["wbjr"], ["otr", "fzr", "g"], ["fzr", "wi", "otr", "xgp", "wbjr", "igi", "b"],
    #                ["fzr", "xgp", "wi", "otr", "tokfq", "izcad", "igi", "xevvq", "i", "anp"], ["wi", "xgp", "wbjr"],
    #                ["wbjr", "bxgnm", "i", "b", "hjvu", "izcad", "igi", "z", "g"], ["xgp", "otr", "wbjr"],
    #                ["wbjr", "otr"],
    #                ["wbjr", "otr", "fzr", "wi", "xgp", "hjvu", "tokfq", "z", "kwdmb"],
    #                ["xgp", "wi", "wbjr", "bxgnm", "izcad", "p", "xevvq"], ["bxgnm"], ["wi", "fzr", "otr", "wbjr"],
    #                ["wbjr", "wi", "fzr", "xgp", "otr", "g", "b", "p"], ["otr", "fzr", "xgp", "wbjr"],
    #                ["xgp", "wbjr", "q", "vpio", "tokfq", "we"], ["wbjr", "wi", "xgp", "we"], ["wbjr"], ["wi"]]
    # supplies = ["wi", "otr", "wbjr", "fzr", "xgp"]

    recipes = ["bread", "sandwich", "burger"]
    ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
    supplies = ["yeast",
                "flour",
                "meat"]
    s = Solution3()
    print(s.findAllRecipes(recipes, ingredients, supplies))
