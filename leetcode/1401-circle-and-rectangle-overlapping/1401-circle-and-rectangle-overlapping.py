class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        dx, dy = 0, 0

        # put x and y on there ranges 
        xRange = [x1, x2]
        yRange = [y1, y2]

        # check xCenter is side the range of xRange
        if xCenter >= x1 and xCenter <= x2:
            dx = 0
        else:
            dx = min(abs(x1 - xCenter), abs(xCenter - x2))

        # check for yCenter 
        if yCenter >= y1 and yCenter <= y2:
            dy = 0
        else :
            dy = min (abs(y1 - yCenter) ,abs( yCenter - y2))

        return (dx**2 + dy**2) <= radius**2