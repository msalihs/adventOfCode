class llNode:
    def __init__(self, v=0):
        self.val = v
        self.next = None


class Solution:
    def __init__(self):
        pass

    def print(self, curr, num):
        temp = curr
        toPrint = list()
        for j in range(num):
            toPrint.append(temp.val)
            temp = temp.next
        print(toPrint)

    def solve(self):
        result1, result2 = 0, 0
        n_test = [int(x) for x in "389125467"]
        n = [int(x) for x in "315679824"]

        def move(n, it):
            hmap = {x: llNode(x) for x in n}
            for x in range(len(n)):
                hmap[n[x]].next = hmap[n[(x + 1) % len(n)]]
            curr = hmap[n[0]]
            for _ in range(it):
                pick_start = curr.next
                picked_vals = [
                    pick_start.val,
                    pick_start.next.val,
                    pick_start.next.next.val,
                ]
                dest = (curr.val - 1) if curr.val != 1 else len(n)
                while dest in picked_vals:
                    dest = (dest - 1) if dest != 1 else len(n)
                curr.next = curr.next.next.next.next
                dest_node = hmap[dest]
                pick_start.next.next.next = dest_node.next
                dest_node.next = pick_start
                curr = curr.next
            return hmap[1]

        # PART 1
        pivot = move(n, 100)
        digits = []
        for i in range(len(n) - 1):
            pivot = pivot.next
            digits.append(pivot.val)
        result1 = int("".join([str(x) for x in digits]))

        # PART 2
        n += list(range(10, 10 ** 6 + 1))
        pivot = move(n, 10 ** 7)
        result2 = pivot.next.val * pivot.next.next.val

        return result1, result2


solver = Solution()
print(solver.solve())
