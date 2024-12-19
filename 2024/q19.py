from functools import lru_cache


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        patterns, goals = f.read().split("\n\n")

        patterns = {p.strip() for p in patterns.split(",")}
        goals = goals.split("\n")

        @lru_cache()
        def search(s):
            if not s:
                return 1
            result = 0
            for i in range(1, len(s) + 1):
                if s[:i] in patterns:
                    result += search(s[i:])
            return result

        for goal in goals:
            n = search(goal)
            if n:
                result1 += 1
                result2 += n

        return result1, result2


solver = Solution()
print(solver.solve("2024/q19.txt"))
