from itertools import product

class Solution:
    def __init__(self):
        pass

    def parse_file(self, filepath):
        activeNodes = set()
        f = open(filepath, "r")
        for i, line in enumerate(f.readlines()):
            activeNodes |= {(i, j) for j, c in enumerate(line.strip("\n")) if c == '#'}
        return activeNodes

    def solve(self, filepath):
        result1, result2 = 0, 0

        def play(dimension, iterations):
            if dimension < 2: return -1
            activeNodes = [tuple([x,y] + [0]*(dimension-2)) for (x,y) in self.parse_file(filepath)]
            cycle = 0
            delta = [-1, 0, 1]
            
            while cycle < iterations:
                cycle += 1
                activatedNodes = set()
                counts = dict()
                for node in activeNodes:
                    for deltas in product(delta, repeat=dimension):
                        neighbor = tuple([x+dx for x,dx in zip(node, deltas)])
                        if sum([abs(x) for x in deltas]) == 0:
                            counts[neighbor] = counts.get(neighbor, 0)
                        else:
                            counts[neighbor] = counts.get(neighbor, 0) + 1
                for node, count in counts.items():
                    if (node in activeNodes and (count == 2 or count == 3)) or (node not in activeNodes and count == 3):
                        activatedNodes.add(node)
                activeNodes = activatedNodes.copy()
            return len(activeNodes)

        result1 = play(3,6)
        result2 = play(4,6)

        return result1, result2
        
solver = Solution()
print(solver.solve("2020/q17.txt"))
