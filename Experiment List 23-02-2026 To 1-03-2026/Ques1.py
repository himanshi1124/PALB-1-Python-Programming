class Solution:
    def minSwaps(self, s1, s2):
        c01 = 0
        c10 = 0

        for a, b in zip(s1, s2):
            if a == '0' and b == '1':
                c01 += 1
            elif a == '1' and b == '0':
                c10 += 1

        # If total mismatches is odd → impossible
        if (c01 + c10) % 2 != 0:
            return -1

        # Pair mismatches
        swaps = (c01 // 2) + (c10 // 2)

        # If one of each remains
        if c01 % 2 == 1:
            swaps += 2

        return swaps
