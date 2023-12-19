from collections import deque


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        conditions, parts = f.read().split("\n\n")
        parts = [
            {c.split("=")[0]: int(c.split("=")[1]) for c in part[1:-1].split(",")}
            for part in parts.split("\n")
        ]
        workflows = dict()

        for condition in conditions.split("\n"):
            k, v = condition.split("{")
            v = v[:-1].split(",")
            for i, cond in enumerate(v):
                if len(cond.split(":")) < 2:
                    v[i] = cond
                    continue
                cat = cond[0]
                op = cond[1]
                val, next_ = cond[2:].split(":")
                v[i] = (cat, op, int(val), next_)
            workflows[k] = v

        for idx, part in enumerate(parts):
            curr = "in"
            while curr not in {"A", "R"}:
                prev = curr
                for conds in workflows[curr]:
                    if isinstance(conds, str):
                        curr = conds
                        break
                    (cat, op, val, next_) = conds
                    if (op == "<" and part[cat] < val) or (
                        op == ">" and part[cat] > val
                    ):
                        curr = next_
                        break
                # if prev == curr:
                #     raise ValueError(f"No next state found for {idx}, {part}, {curr}")

            if curr == "A":
                result1 += sum(part.values())

        seen = set()
        queue = deque(
            [("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]
        )
        while queue:
            state, cons = queue.popleft()
            seen.add(state)
            if state == "A":
                combinations = 1
                for ll, ul in cons.values():
                    combinations *= ul - ll + 1
                result2 += combinations
            elif state != "R":
                for conds in workflows[state]:
                    if isinstance(conds, str):
                        queue.append((conds, cons.copy()))
                        continue
                    (cat, op, val, next_) = conds
                    t = cons.copy()
                    ll, ul = t[cat]
                    if op == "<":
                        t[cat] = (ll, min(ul, val - 1))
                    else:
                        t[cat] = (max(ll, val + 1), ul)
                    queue.append((next_, t))
                    ll, ul = cons[cat]
                    if op == ">":
                        cons[cat] = (ll, min(ul, val))
                    else:
                        cons[cat] = (max(ll, val), ul)
        return result1, result2


solver = Solution()
print(solver.solve("2023/q19.txt"))
