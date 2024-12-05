from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        rules, orders = f.read().replace("\n\n ", "\n\n").split("\n\n")
        rules_mapping = defaultdict(list)

        for rule in rules.split("\n"):
            rule = rule.split("|")
            rules_mapping[int(rule[0])].append(int(rule[1]))

        for order in orders.split("\n"):
            order = [int(x) for x in order.split(",")]

            # PART 1
            for idx, page in enumerate(order):
                if page in rules_mapping:
                    if set(rules_mapping[page]) & set(order[:idx]):
                        break
            else:
                result1 += order[len(order) // 2]
                continue

            # PART 2
            fixed_order = [order.pop(0)]
            while order:
                page = order.pop(0)
                if page in rules_mapping:
                    for curr in fixed_order:
                        if curr in rules_mapping[page]:
                            fixed_order.insert(fixed_order.index(curr), page)
                            break
                    else:
                        fixed_order.append(page)
                else:
                    fixed_order.append(page)

            result2 += fixed_order[len(fixed_order) // 2]

        return result1, result2


solver = Solution()
print(solver.solve("2024/q5.txt"))
