from .task2 import isCorrectRect
from .errors import RectCorrectError

def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некорректен")
    
    (ax1, ay1), (ax2, ay2) = rect1
    (bx1, by1), (bx2, by2) = rect2
    
    intersect_x = ax1 < bx2 and ax2 > bx1
    intersect_y = ay1 < by2 and ay2 > by1
    
    return intersect_x and intersect_y
