class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result, result2 = 0, 0
        passports = dict()
        fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
        index = 0
        passports[index] = dict()

        for line in f.readlines():
            x = line.strip('\n')
            if x:
                for entry in x.split(' '):
                    key, value = entry.split(':')
                    passports[index][key] = value
            else:
                index += 1
                passports[index] = dict()
        for k in passports:
            missing = set(passports[k].keys()) ^ fields
            if not missing or (len(missing) == 1 and "cid" in missing):
                result += 1

                if (1920 <= int(passports[k]['byr']) <= 2002) and (2010 <= int(passports[k]['iyr']) <= 2020) and (2020 <= int(passports[k]['eyr']) <= 2030):
                    if ("cm" in passports[k]['hgt'] and (150 <= int(passports[k]['hgt'][0:-2]) <= 193)) or ("in" in passports[k]['hgt'] and (59 <= int(passports[k]['hgt'][0:-2]) <= 76)):
                        if len(passports[k]['hcl']) == 7 and passports[k]['hcl'][0] == '#' and all(48<=ord(c)<58 or 97<=ord(c)<103 for c in passports[k]['hcl'][1:]):
                            if passports[k]['ecl'] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                                if passports[k]['pid'].isnumeric() and len(passports[k]['pid']) == 9:
                                    result2 += 1
                                    
        return result, result2 

solver = Solution()
print(solver.solve('2020/q4.txt'))
