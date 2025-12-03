from .task3 import isCollisionRect

def intersectionAreaRect(rect1, rect2):
    if not isCollisionRect(rect1, rect2):
        return 0.0
    
    (ax1, ay1), (ax2, ay2) = rect1
    (bx1, by1), (bx2, by2) = rect2
    
    intersect_x1 = max(ax1, bx1)
    intersect_y1 = max(ay1, by1)
    intersect_x2 = min(ax2, bx2)
    intersect_y2 = min(ay2, by2)
    
    width = max(0, intersect_x2 - intersect_x1)
    height = max(0, intersect_y2 - intersect_y1)
    
    return width * height