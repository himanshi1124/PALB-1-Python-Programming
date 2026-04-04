class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        target = total // 2

        res = []
        found = False

        def backtrack(start, path, curr_sum):
            nonlocal res, found

            if found:
                return

            # size condition
            if len(path) == n // 2 or len(path) == (n + 1) // 2:
                if curr_sum == target:
                    subset1 = path[:]
                    subset2 = arr[:]

                    for x in subset1:
                        subset2.remove(x)

                    res = [subset1, subset2]
                    found = True
                return

            for i in range(start, n):
                path.append(arr[i])
                backtrack(i + 1, path, curr_sum + arr[i])
                path.pop()

        backtrack(0, [], 0)
        return res
