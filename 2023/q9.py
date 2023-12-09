class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        sequences = [[int(num) for num in reading.split(" ")] for reading in readings]

        def helper(seq, find_next=True):
            if not seq or (seq[0] == 0 and len(set(seq)) == 0):
                return 0
            else:
                pred = helper(
                    [seq[i] - seq[i - 1] for i in range(1, len(seq))],
                    find_next=find_next,
                )
                return (seq[-1] + pred) if find_next else (seq[0] - pred)

        for sequence in sequences:
            result1 += helper(sequence)
            result2 += helper(sequence, find_next=False)

        return result1, result2


solver = Solution()
print(solver.solve("2023/q9.txt"))
