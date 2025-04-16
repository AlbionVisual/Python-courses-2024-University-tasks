import sys

def permutations(stroke):

    def recursion(s):

        if len(s) > 1:
            permutated = []

            for i in range(len(s)):
                permutated += [s[i] + j for j in recursion(s[:i] + s[i+1:])]
            return permutated
        
        else: return s

    return recursion(stroke)

res = permutations(sys.argv[1])
print(len(res), res)