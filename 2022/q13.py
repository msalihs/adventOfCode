import ast
import functools
import bisect


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        def helper(e1, e2):
            i = 0
            while i < len(e1) and i < len(e2):
                if type(e1[i]) == int and type(e2[i]) == int:
                    if e2[i] < e1[i]:
                        return False
                    elif e2[i] > e1[i]:
                        return True
                else:
                    if type(e1[i]) == list and type(e2[i]) == list:
                        result = helper(e1[i], e2[i])
                        if result is not None:
                            return result
                    elif type(e1[i]) == int:
                        result = helper([e1[i]], e2[i])
                        if result is not None:
                            return result
                    elif type(e2[i]) == int:
                        result = helper(e1[i], [e2[i]])
                        if result is not None:
                            return result
                i += 1
            if i < len(e1):
                return False
            if i < len(e2):
                return True

        def comp(a, b):
            return -7 if helper(a, b) else 7

        f = open(filepath, "r")
        result1, result2 = 0, 0
        pairs = list()

        for pair in f.read().split("\n\n"):
            pairs.append([ast.literal_eval(p) for p in pair.split("\n")])

        for i, pair in enumerate(pairs):
            if helper([pair[0]], [pair[1]]):
                result1 += i + 1

        dividers = [[[2]], [[6]]]
        pairs.append(dividers)

        signals = []
        for pair in pairs:
            for entry in pair:
                signals.append(entry)

        signals.sort(key=functools.cmp_to_key(comp))

        result2 = 1
        for i in range(len(signals)):
            if signals[i] == dividers[0]:
                result2 *= i + 1
            if signals[i] == dividers[1]:
                result2 *= i + 1
                break

        return result1, result2


solver = Solution()
print(solver.solve("2022/q13.txt"))
