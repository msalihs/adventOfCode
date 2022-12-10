class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1 = 0
        readings = f.read().split("\n")
        x = 1
        cycle = -20

        for reading in readings:
            instruction = reading.split(" ")
            if instruction[0] == "noop":
                cycle += 1
                if cycle % 40 == 0:
                    result1 += x * (cycle + 20)
            if instruction[0] == "addx":

                if (cycle + 1) % 40 == 0:
                    result1 += x * (cycle + 21)
                if (cycle + 2) % 40 == 0:
                    result1 += x * (cycle + 22)
                x += int(instruction[1])
                cycle += 2

        x = 1
        crt = []
        cycle = 0
        for reading in readings:
            instruction = reading.split(" ")
            n = 2 if instruction[0] == "addx" else 1
            for _ in range(n):
                pixel = "#" if (x - 1) <= (cycle % 40) <= (x + 1) else "."
                crt.append(pixel)
                cycle += 1
            if instruction[0] == "addx":
                x += int(instruction[1])

        i = 0
        print("Result of part 2 is: ")
        while i < len(crt):
            print(" ".join(crt[i : i + 40]))
            i += 40

        return result1


solver = Solution()
print(solver.solve("2022/q10.txt"))
