class Solution:
    def __init__(self):
        pass
    

    def int_to_snafu(self, n):
        mapping = {0:'0', 1:'1', 2:'2', -1:'-', -2:'='}
        result = []
        while n:
            result.append(mapping[(n+2)%5 - 2])
            n -= (n+2) % 5 - 2 
            n //= 5
        return ''.join(reversed(result))


    def snafu_to_int(self, number):
        result = 0
        for i, digit in enumerate(number):
            n = 0
            if digit == '=':
                n = -2
            elif digit == '-':
                n = -1
            else:
                n = int(digit)
            result += pow(5, len(number)-i-1) * n
        return result

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        numbers = [list(r) for r in f.read().split("\n")]

        for number in numbers:
            result1 += self.snafu_to_int(number)
        result1 = self.int_to_snafu(result1)
        
        return result1, result2


solver = Solution()
print(solver.solve("2022/q25.txt"))
