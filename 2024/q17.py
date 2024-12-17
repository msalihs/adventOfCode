class Solution:
    def __init__(self, debug=False):
        self.debug = debug
        self.pp = 0
        self.output = []
        self.mapping = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def combo_op(self):
        value = self.program[self.pp + 1]
        if value < 4:
            return value
        elif value == 4:
            return self.registers["A"]
        elif value == 5:
            return self.registers["B"]
        elif value == 6:
            return self.registers["C"]

    def literal_op(self):
        return self.program[self.pp + 1]

    def adv(self):
        self.registers["A"] //= 2 ** self.combo_op()

    def bxl(self):
        self.registers["B"] ^= self.literal_op()

    def bst(self):
        self.registers["B"] = self.combo_op() % 8

    def jnz(self):
        if self.registers["A"] != 0:
            self.pp = self.literal_op()
            return True
        return False

    def bxc(self):
        self.registers["B"] ^= self.registers["C"]

    def out(self):
        self.output.append(self.combo_op() % 8)

    def bdv(self):
        self.registers["B"] = self.registers["A"] // 2 ** self.combo_op()

    def cdv(self):
        self.registers["C"] = self.registers["A"] // 2 ** self.combo_op()

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        registers, program = f.read().split("\n\n")

        self.registers = {
            register.split(":")[0][-1]: int(register.split(": ")[1])
            for register in registers.split("\n")
        }
        self.program = [int(x) for x in program.split(": ")[1].split(",")]

        while self.pp < len(self.program):
            op = self.program[self.pp]
            result = self.mapping[op]()
            if (op == 3 and result is False) or op != 3:
                self.pp += 2

        result1 = ",".join([str(x) for x in self.output])

        desired_output = ",".join([str(x) for x in self.program[-2:0]])

        idx = 0

        for j in range(1, len(self.program) + 1):
            desired_output = ",".join([str(x) for x in self.program[-j:]])
            idx *= 8
            while result != desired_output:
                idx += 1
                self.registers["A"] = idx
                self.pp = 0
                self.output = []
                while self.pp < len(self.program):
                    op = self.program[self.pp]
                    result = self.mapping[op]()
                    if (op == 3 and result is False) or op != 3:
                        self.pp += 2
                result = ",".join([str(x) for x in self.output])
            print(result, idx)

        result2 = idx

        return result1, result2


solver = Solution()
print(solver.solve("2024/q17.txt"))
