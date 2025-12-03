from .task2 import isCorrectRect
from .task3 import isCollisionRect
from .errors import RectCorrectError

def intersectionAreaMultikect(rectangles):
    if len(rectangles) < 2:
        return 0.0
    
    for i, rect in enumerate(rectangles):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Прямоугольник {i+1} некорректен")
    
    total_area = 0.0
    
    # Попарные пересечения
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if isCollisionRect(rectangles[i], rectangles[j]):
                (x1, y1), (x2, y2) = rectangles[i]
                (x3, y3), (x4, y4) = rectangles[j]
                
                left = max(x1, x3)
                right = min(x2, x4)
                bottom = max(y1, y3)
                top = min(y2, y4)
                
                width = max(0, right - left)
                height = max(0, top - bottom)
                total_area += width * height
    
    return total_area