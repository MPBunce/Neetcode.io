#Time limit exceeded
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kmin, kmax = 1, max(piles)
        res = max(piles)
        while kmin <= kmax:
            mid = (kmin + kmax) // 2

            totalTime = 0
            for n in piles:
                while n > 0:
                    n = n - mid
                    totalTime += 1

            if totalTime <= h:
                res = min(res, mid)
                kmax = mid-1
            else:
                kmin = mid+1

        return res


#Time limit accepted
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kmin, kmax = 1, max(piles)
        res = max(piles)
        while kmin <= kmax:
            mid = (kmin + kmax) // 2

            totalTime = 0
            for n in piles:
                totalTime += math.ceil( n / mid)

            if totalTime <= h:
                res = min(res, mid)
                kmax = mid-1
            else:
                kmin = mid+1

        return res
