import time
from enum import Enum


class Ops(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"


ops_fcn = {
    Ops.AND: lambda x, y: x and y,
    Ops.OR: lambda x, y: x or y,
    Ops.XOR: lambda x, y: x ^ y,
}


class Solution:
    def __init__(self):
        self.valid_ops = [op.value for op in list(Ops)]
        self.states = {}
        self.ops = {}
        self.regs = set()

    def get_state(self, reg):
        if reg in self.states:
            return self.states[reg]
        reg1, op, reg2 = self.ops[reg]
        s1 = self.get_state(reg1)
        s2 = self.get_state(reg2)
        return ops_fcn[Ops(op)](s1, s2)

    def get_regs(self):
        return set(self.ops.keys()) | set(self.states.keys())

    def get_number_starting_with_char(self, char):
        regs = list(
            reversed(sorted([reg for reg in self.get_regs() if reg[0] == char]))
        )
        res = [self.get_state(reg) for reg in regs]
        return int("".join([str(x) for x in res]), 2)

    def solve(self, filepath):
        result1, result2 = [], set()
        f = open(filepath, "r")
        _input = f.read().split("\n\n")
        self.states = {
            s.split(": ")[0]: int(s.split(": ")[1]) for s in _input[0].split("\n")
        }
        for op in _input[1].split("\n"):
            source, dest = op.split(" -> ")
            source = source.split(" ")
            self.ops[dest] = source

        # PART 1
        result1 = self.get_number_starting_with_char("z")

        # PART 2
        # Notice that it's a Ripple Carry Adder and make sure the given
        # circuit adheres to expected construction with XOR, OR and AND gates.
        # https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder
        for reg in self.ops:
            s1, op, s2 = self.ops[reg]
            op = Ops(op)
            if op != Ops.XOR and reg[0] == "z":
                result2.add(reg)
            if op == Ops.XOR and ({s1[0], s2[0], reg[0]} & {"x", "y", "z"}) == set():
                result2.add(reg)
            if op == Ops.XOR or (op == Ops.AND and "x00" not in {s1, s2}):
                valid = {Ops.OR} if op == Ops.XOR else {Ops.AND, Ops.XOR}
                for reg2 in self.ops:
                    s12, op2, s22 = self.ops[reg2]
                    op2 = Ops(op2)
                    if (reg == s12 or reg == s22) and op2 in valid:
                        result2.add(reg)

        # The last register can be an XOR (I thnink it's because it's just the carry bit)
        max_z = sorted([reg for reg in self.get_regs() if reg[0] == "z"])[-1]
        result2 -= {max_z}
        result2 = ",".join(sorted(result2))

        return result1, result2


start = time.time()
solver = Solution()
print(solver.solve("2024/q24.txt"))
print(f"Time: {time.time() - start}")
