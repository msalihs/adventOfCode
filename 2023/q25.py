import networkx


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 1, 0
        pairs = list()
        for reading in f.read().split("\n"):
            node, nei = reading.split(": ")
            for n in nei.split(" "):
                pairs.append((n, node))
        graph = networkx.Graph(pairs)
        edges_to_remove = networkx.minimum_edge_cut(graph)
        graph.remove_edges_from(edges_to_remove)
        for count in networkx.connected_components(graph):
            result1 *= len(count)

        return result1, result2


solver = Solution()
print(solver.solve("2023/q25.txt"))
