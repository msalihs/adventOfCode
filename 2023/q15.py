class Solution:
    def __init__(self):
        pass

    def get_hash(self, seq):
        curr = 0
        for c in seq:
            curr += ord(c)
            curr *= 17
            curr = curr % 256
        return curr

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        seqs = f.read().split(",")

        for seq in seqs:
            result1 += self.get_hash(seq)

        hashmap = dict()
        for i, seq in enumerate(seqs):
            if "-" in seq:
                label = seq[:-1]
                hash = self.get_hash(label)
                if hash in hashmap and label in hashmap[hash]:
                    hashmap[hash].pop(label)
            if "=" in seq:
                label, fl = seq.split("=")
                hash = self.get_hash(label)
                if hash in hashmap:
                    hashmap[hash][label] = fl
                else:
                    hashmap[hash] = {label: fl}

        for k, v in hashmap.items():
            for idx, (label, fl) in enumerate(v.items()):
                result2 += (k + 1) * (idx + 1) * int(fl)

        return result1, result2


solver = Solution()
print(solver.solve("2023/q15.txt"))
