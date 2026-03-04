class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        position2car = {}
        for i in range(len(position)):
            time.append((target - position[i]) / speed[i])
            position2car[position[i]] = i

        pos2car_sorted = sorted(position2car.items(), reverse = True, key = lambda x: x[0])
        fleets = 0
        prev_car_time = 0
        for pos, car in pos2car_sorted:
            if prev_car_time == 0:
                prev_car_time = time[car]
                fleets += 1
                continue
            else:
                if time[car] > prev_car_time:
                    fleets += 1
                    prev_car_time = time[car]
                    
        return fleets

        # O(n) - time
        # O(n) - space