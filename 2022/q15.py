import heapq


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        beacons, sensors, distances = list(), list(), list()

        for i, reading in enumerate(readings):
            b, c = [r.split("=") for r in reading.split(":")]
            sensors.append((int(b[1].strip(", y")), int(b[2])))
            beacons.append((int(c[1].strip(", y")), int(c[2])))

        target = 2000000
        no_beacon = list()

        for (x_s, y_s), (x_b, y_b) in zip(sensors, beacons):
            distances.append(abs(x_s - x_b) + abs(y_s - y_b))
            l = distances[-1] - abs(target - y_s)
            if l > 0:
                heapq.heappush(no_beacon, (x_s - l, x_s + l))

        e = -(10**9)
        while no_beacon:
            sp, ep = heapq.heappop(no_beacon)
            if sp <= e:
                result1 += max(e, ep) - e
            else:
                result1 += ep - sp + 1
            e = max(e, ep)

        for (x_b, y_b) in set(beacons):
            if y_b == target:
                result1 -= 1

        for x in range(0, target * 2 + 1):
            y_no_beacon = list()
            for (x_s, y_s), md in zip(sensors, distances):
                l = md - abs(x - x_s)
                if l > 0:
                    heapq.heappush(y_no_beacon, (y_s - l, y_s + l))
            y = 0
            while y_no_beacon:
                s, e = heapq.heappop(y_no_beacon)
                if s <= y <= e:
                    y = e + 1
            if y < target * 2 + 1:
                result2 = x * 4000000 + y
                break

        return result1, result2


solver = Solution()
print(solver.solve("2022/q15.txt"))
