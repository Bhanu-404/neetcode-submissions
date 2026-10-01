import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_k = float("inf")
        while low <= high:
            hours = 0
            k = low + (high - low)//2
            for p in piles:
                hours += math.ceil(p / k)
            if hours > h:
                low = k + 1
            elif hours <= h:
                high = k - 1
                min_k = min(min_k, k)
            
        return min_k