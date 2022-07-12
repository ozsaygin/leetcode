import math
import heapq


class Solution:

    def find_distance(self, x, y): 
        distance = pow(x, 2) + pow(y, 2)
        return math.sqrt(distance)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance_points = { }
        distances = [ ] 
        
        for p in points: 
        
            dist = self.find_distance(p[0], p[1])
            if dist not in distance_points: 
                distance_points[dist] = [ ]

            distance_points[dist].append(p)
            distances.append(dist)

        heapq.heapify(distances)
        
        k_min_points = [] 
        while len(k_min_points) < k: 
            dist = heapq.heappop(distances)
            points = distance_points[dist]

            for p in points: 
                k_min_points.append(p)
                
                if len(k_min_points) >= k:
                    break

        return k_min_points



         
        