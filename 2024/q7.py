from collections import deque


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        _input = f.read().split("\n")
        ops = {
            int(op.split(":")[0]): [int(x) for x in op.split(":")[1][1:].split(" ")]
            for op in _input
        }

        # PART 1
        def apply_ops(concatenate: bool):
            result = 0
            for target, vals in ops.items():
                res = deque([vals[0]])

                for val in vals[1:]:
                    n = len(res)
                    while n > 0:
                        curr = res.popleft()
                        if curr + val <= target:
                            res.append(curr + val)
                        if curr * val <= target:
                            res.append(curr * val)
                        if concatenate:
                            x = int("".join([str(curr), str(val)]))
                            if x <= target:
                                res.append(x)
                        n -= 1
                if target in res:
                    result += target

            return result

        return apply_ops(concatenate=False), apply_ops(concatenate=True)


solver = Solution()
print(solver.solve("2024/q7.txt"))
