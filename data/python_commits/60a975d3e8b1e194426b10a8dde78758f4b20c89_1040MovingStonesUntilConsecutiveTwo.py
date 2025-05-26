class Solution:
    def numMovesStonesII(stones):
        stones.sort()
        i, n, low = 0, len(stones), len(stones)
        total = len(stones)
        sSum = stones[-1] - stones[0] + 1 - total
        high = sSum - min(stones[1] - stones[0] -1, stones[-1] - stones[-2] - 1)
        if (stones[total-2] - stones[0] + 1) == total - 1:
            low = min(stones[total-1] - stones[total-2] - 1, 2)
            return [high, low]
        if (stones[total-1] - stones[1] + 1) == total - 1:
            low = min(stones[1] - stones[0] - 1, 2)
            return [high, low]
        
        for j in range(n):
            while stones[j] - stones[i] > n:
                i += 1
            low = min(low, n - (j - i + 1))
        return [low, high]

stones = [7,4,9]
ans = Solution.numMovesStonesII(stones)
print(ans)  # Output: [1,2]
    
    