class Solution:
    def __init__(self):
        pass

    def parse_file(self, filepath):
        lines = list()
        f = open(filepath, "r")
        for i, line in enumerate(f.readlines()):
            lines.append(line.strip("\n"))
        return lines

    def solve(self, filepath):
        result1, result2 = 0, 0
        lines = self.parse_file(filepath)

        def comp(op, num1, num2):
            if op == "+":
                return num1 + num2
            elif op == "*":
                return num1 * num2
            else:
                return max(num1, num2)

        # PART 1
        for line in lines:
            stack, res, op = list(), 0, "+"
            for c in line:
                if c.isdigit():
                    res = comp(op, res, int(c))
                elif c == "+" or c == "*":
                    op = c
                elif c == "(":
                    stack.append((res, op))
                    res, op = 0, "+"
                elif c == ")":
                    prevRes, prevOp = stack.pop()
                    res = comp(prevOp, prevRes, res)
            result1 += res

        # PART 2
        for line in lines:
            stack, res, op = list(), 0, "+"
            for c in line:
                if c == " ":
                    continue
                if c.isdigit():
                    res = comp(op, res, int(c))
                elif c == "+":
                    op = c
                elif c == "*":
                    stack.append((res, "*"))
                    res, op = 0, "+"
                elif c == "(":
                    if op == "+":
                        stack.append((res, op))
                    stack.append((res, "("))
                    res, op = 0, "+"
                elif c == ")" and stack:
                    prevRes, prevOp = stack.pop()
                    while prevOp != "(":
                        res = comp(prevOp, prevRes, res)
                        prevRes, prevOp = stack.pop()
                    while stack:
                        prevRes, prevOp = stack.pop()
                        if prevOp == "+":
                            res = comp(prevOp, prevRes, res)
                        else:
                            stack.append((prevRes, prevOp))
                            break
            while stack:
                prevRes, prevOp = stack.pop()
                res = comp(prevOp, prevRes, res)

            result2 += res

        return result1, result2


solver = Solution()
print(solver.solve("2020/q18.txt"))
