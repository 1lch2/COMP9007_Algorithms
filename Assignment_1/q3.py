import math
from typing import List

class Solution:
    def findPopular(self, points: List[tuple], r: float) -> tuple:
        res = [0 for _ in range(len(points))] # Store the number of points within r distance.

        for i in range(len(points)):
            for j in range(len(points)):
                if j == i: # Skip the same point
                    continue

                d = self.computeDistance(points[i], points[j])
                if d <= r: # Add to result if the point is valid
                    res[i] += 1
        
        return res.index(max(res))



    def computeDistance(self, pi: tuple, pj: tuple) -> float:
        """Assuming it runs in O(1) time.
        """
        return math.sqrt((pi[0] - pj[0])**2 + (pi[1] - pj[1])**2)


if __name__ == "__main__":
    points = [(0, 3), (3, 2), (1, 2), (1, 1)]
    r = math.sqrt(2) + 1e-6

    S = Solution()
    res = S.findPopular(points, r)

    print(res)