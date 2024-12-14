class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        input_ = f.read().split("\n")
        robots = list()

        for line in input_:
            p = tuple(int(x) for x in line.split(" ")[0].split("=")[1].split(","))
            v = tuple(int(x) for x in line.split(" ")[1].split("=")[1].split(","))
            robots.append((p, v))

        n, m = 103, 101
        grid = [[0 for _ in range(m)] for _ in range(n)]

        # PART 1
        iter = 100
        for robot in robots:
            (px, py), (vx, vy) = robot
            px += iter * vx
            py += iter * vy
            grid[py % n][px % m] += 1

        q1, q2, q3, q4 = 0, 0, 0, 0
        for i in range(n):
            for j in range(m):
                if i < n // 2 and j < m // 2:
                    q1 += grid[i][j]
                elif i < n // 2 and j > m // 2:
                    q2 += grid[i][j]
                elif i > n // 2 and j < m // 2:
                    q3 += grid[i][j]
                elif i > n // 2 and j > m // 2:
                    q4 += grid[i][j]
        result1 = q1 * q2 * q3 * q4

        # PART 2
        iter = 600
        for i in range(iter):
            # Found clustering every 103 iterations after 75th iteration
            j = 75 + 103 * i
            grid = [[0 for _ in range(m)] for _ in range(n)]
            for robot in robots:
                (px, py), (vx, vy) = robot
                px += vx * j
                py += vy * j
                grid[py % n][px % m] += 1

            with open("output.txt", "a") as output_file:
                output_file.write(f"ITERATION {j}\n")
                for line in grid:
                    output_file.write(
                        "".join(["*" if x > 0 else "." for x in line]) + "\n"
                    )
                output_file.write("-------------------\n")

        result2 = 8006

        return result1, result2


solver = Solution()
print(solver.solve("2024/q14.txt"))
