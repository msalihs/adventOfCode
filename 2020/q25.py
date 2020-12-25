class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        pubkey1, pubkey2 = [int(key.strip("\n")) for key in f.readlines()]
        loop1, loop2 = None, None
        mod = 20201227
        x, subj, count = 1, 7, 0

        while loop1 == None or loop2 == None:
            count += 1
            x = (x * subj) % mod
            if x == pubkey1:
                loop1 = count
            if x == pubkey2:
                loop2 = count

        assert pow(pubkey2, loop1, mod) == pow(pubkey1, loop2, mod)

        return pow(pubkey2, loop1, mod)


solver = Solution()
print(solver.solve("2020/q25.txt"))
