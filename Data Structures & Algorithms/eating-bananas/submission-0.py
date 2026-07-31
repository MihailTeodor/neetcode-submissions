class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def checkNecessaryHours(rate: int) -> int:
            necessaryHours = 0 
            for pile in piles:
                necessaryHours += math.ceil(pile / rate)

            return necessaryHours

        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = l + (r - l) // 2

            curRes = checkNecessaryHours(mid)

            if curRes <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res