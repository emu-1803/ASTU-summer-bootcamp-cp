class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        last_heater_index = len(heaters) - 1
        left_heater, right_heater = 0, 0
        max_radius = 0

        for house in houses:
            while right_heater < last_heater_index and house > heaters[right_heater]:
                left_heater, right_heater = right_heater, right_heater + 1
            
            distance_left = abs(heaters[left_heater] - house)
            distance_right = abs(heaters[right_heater] - house)
            max_radius = max(max_radius, min(distance_left, distance_right))
        
        return max_radius