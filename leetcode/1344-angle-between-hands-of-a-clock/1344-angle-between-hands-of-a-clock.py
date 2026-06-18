class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        tetha_minute = 6 * minutes
        tetha_hour = (hour % 12) * 30 + minutes*0.5

        diff =  abs(tetha_minute - tetha_hour)
        return min(diff , 360 - diff)