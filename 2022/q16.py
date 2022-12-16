from collections import defaultdict, deque
import sys


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        graph = dict()
        max_flow = 0

        for i, reading in enumerate(readings):
            reading = reading.split(";")
            node = reading[0].split(" ")[1]
            flow = int(reading[0].split("=")[1])
            if "valves" in reading[1]:
                nei = reading[1].split("valves ")[1].split(", ")
            else:
                nei = [reading[1].split("valve ")[1]]
            max_flow += flow
            graph[node] = (flow, nei)

        queue = deque([("AA", 30, 0, set(), 0)])
        seen = defaultdict(dict)
        i = 0
        while queue:
            i += 1
            node, minutes, flow, opened, total = queue.popleft()
            seen[node][total] = minutes
            result1 = max(total, result1)
            if flow == max_flow:
                continue
            # Open the door and traverse
            if node not in opened and graph[node][0] > 0 and minutes > 1:
                for nei in graph[node][1]:
                    ntotal = total + (graph[node][0] * (minutes - 1))
                    if seen[nei].get(ntotal, 0) <= (minutes - 2):
                        queue.append(
                            (
                                nei,
                                minutes - 2,
                                flow + graph[node][0],
                                opened | {node},
                                ntotal,
                            )
                        )
            if minutes > 0:
                for nei in graph[node][1]:
                    if seen[nei].get(total, 0) <= (minutes - 1):
                        queue.append((nei, minutes - 1, flow, opened, total))

        print(f"It took {i} iterations for part1")

        queue = deque([(["AA", "AA"], 26, 0, set(), 0)])
        seen = defaultdict(dict)
        i = 0
        while queue:
            i += 1
            (e_node, my_node), minutes, flow, opened, total = queue.popleft()
            seen[e_node][total] = minutes
            seen[my_node][total] = minutes
            if total > result2:
                print(total, i, minutes, opened, flow, sys.getsizeof(seen))
            result2 = max(total, result2)
            if flow == max_flow:
                continue
            # Both open
            if (
                e_node != my_node
                and e_node not in opened
                and my_node not in opened
                and minutes > 1
            ):
                if graph[e_node][0] != 0 and graph[my_node][0] != 0:
                    ntotal = (
                        total
                        + (graph[e_node][0] * (minutes - 1))
                        + (graph[my_node][0] * (minutes - 1))
                    )
                    nflow = flow + graph[e_node][0] + graph[my_node][0]
                    for e_nei in graph[e_node][1]:
                        if seen[e_nei].get(ntotal, 0) <= (minutes - 2):
                            for my_nei in graph[my_node][1]:
                                if seen[my_nei].get(ntotal, 0) <= (minutes - 2):
                                    queue.append(
                                        (
                                            [e_nei, my_nei],
                                            minutes - 2,
                                            nflow,
                                            opened | {my_node, e_node},
                                            ntotal,
                                        )
                                    )
            # Only elephant opens
            if e_node not in opened and minutes > 1 and graph[e_node][0] != 0:
                ntotal = total + (graph[e_node][0] * (minutes - 1))
                nflow = flow + graph[e_node][0]
                for my_nei in graph[my_node][1]:
                    # if seen[(e_node, my_nei)].get(ntotal, 0) <= (minutes - 1):
                    queue.append(
                        (
                            [e_node, my_nei],
                            minutes - 1,
                            nflow,
                            opened | {e_node},
                            ntotal,
                        )
                    )
            # Only I open
            if my_node not in opened and minutes > 1 and graph[my_node][0] != 0:
                ntotal = total + (graph[my_node][0] * (minutes - 1))
                nflow = flow + graph[my_node][0]
                for e_nei in graph[e_node][1]:
                    # if seen[(e_nei, my_node)].get(ntotal, 0) <= (minutes - 1):
                    queue.append(
                        (
                            [e_nei, my_node],
                            minutes - 1,
                            nflow,
                            opened | {my_node},
                            ntotal,
                        )
                    )
            # Neither open
            if minutes > 0:
                for e_nei in graph[e_node][1]:
                    if seen[e_nei].get(total, 0) <= (minutes - 1):
                        for my_nei in graph[my_node][1]:
                            if seen[my_nei].get(total, 0) <= (minutes - 1):
                                queue.append(
                                    ([e_nei, my_nei], minutes - 1, flow, opened, total)
                                )
        print(f"It took {i} iterations for part2")

        return result1, result2


solver = Solution()
print(solver.solve("2022/q16.txt"))
