class Solution:
    def __init__(self):
        pass

    def parse_file(self, filepath):
        f = open(filepath, "r")
        rules, messages = dict(), list()
        for line in f.readlines():
            line = line.strip("\n")
            if ":" in line:
                k, v = line.split(": ")
                if "a" in v:
                    rules[int(k)] = "a"
                elif "b" in v:
                    rules[int(k)] = "b"
                else:
                    rules[int(k)] = [
                        [int(a) for a in rule.split(" ")] for rule in v.split(" | ")
                    ]
            elif len(line) > 2:
                messages.append(line)
        return rules, messages

    def solve(self, filepath):
        result1, result2 = 0, 0
        rules, messages = self.parse_file(filepath)

        def verify_message(r, m):
            if not m and not r:
                return True
            elif not m or not r:
                return False
            rule = rules[r[0]]

            if "a" in rule or "b" in rule:
                if m[0] in rule:
                    return verify_message(r[1:], m[1:])
                else:
                    return False

            for x in rule:
                if verify_message(x + r[1:], m):
                    return True

            return False

        ruleToMatch = [0]
        result1 = sum(verify_message(ruleToMatch, message) for message in messages)
        rules[8] = [[42], [42, 8]]
        rules[11] = [[42, 31], [42, 11, 31]]
        result2 = sum(verify_message(ruleToMatch, message) for message in messages)

        return result1, result2


solver = Solution()
print(solver.solve("2020/q19.txt"))
