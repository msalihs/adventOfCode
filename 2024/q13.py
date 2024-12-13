import numpy as np


class Machine:
    def __init__(self, A, B, P):
        self.A = A
        self.B = B
        self.P = P


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        input_ = f.read().split("\n\n")
        machines = list()

        for machine in input_:
            toparse = machine.split("\n")
            Ax = int(toparse[0].split(",")[0].split("+")[1])
            Ay = int(toparse[0].split("+")[-1])
            Bx = int(toparse[1].split(",")[0].split("+")[1])
            By = int(toparse[1].split("+")[-1])
            Px = int(toparse[2].split(",")[0].split("=")[1])
            Py = int(toparse[2].split("=")[-1])
            machines.append(Machine((Ax, Ay), (Bx, By), (Px, Py)))

        def solve_linear_system(
            machine: Machine, error: int = 0, tol: float = 10 ** -10
        ):
            A = np.array([[machine.A[0], machine.B[0]], [machine.A[1], machine.B[1]]])
            P = np.array([[machine.P[0] + error], [machine.P[1] + error]])
            res = np.matmul(np.linalg.inv(A), P).tolist()
            i, j = res[0][0], res[1][0]

            if abs(round(i) - i) < tol and abs(round(j) - j) < tol:
                return round(i) * 3 + round(j) * 1
            return 0

        # PART 1
        for m in machines:
            result1 += solve_linear_system(m)

        # PART 2
        for m in machines:
            # Much bigger tolerance is needed as rounding errors are larger due to the large numbers
            result2 += solve_linear_system(m, error=10000000000000, tol=10 ** -4)

        return result1, result2


solver = Solution()
print(solver.solve("2024/q13.txt"))
