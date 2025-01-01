from collections import defaultdict
import time


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        pairs = [line.strip("\n").split("-") for line in f.readlines() if line]
        graph = defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        # PART 1
        all_3_node_sets = set()
        for node in graph:
            for nei in graph[node]:
                for second_nei in graph[nei]:
                    if second_nei != node and node in graph[second_nei]:
                        all_3_node_sets.add(tuple(sorted([node, nei, second_nei])))

        result1 = len([x for x in all_3_node_sets if any(["t" == y[0] for y in x])])

        # PART 2
        largest_set = set()
        queue = list(graph.keys())
        seen = set()
        while queue:
            node = queue.pop()
            if node in seen:
                continue
            curr = set(graph[node]) | {node}
            for nei in graph[node]:
                res = (set(graph[nei]) | {nei}) & curr
                for second_nei in set(graph[nei]) & set(graph[node]):
                    res = (set(graph[second_nei]) | {second_nei}) & res
                seen |= res
                if len(res) >= len(largest_set):
                    largest_set = res

        result2 = ",".join(sorted(largest_set))
        return result1, result2


start = time.time()
solver = Solution()
print(solver.solve("2024/q23.txt"))
print(f"Time: {time.time() - start}")
