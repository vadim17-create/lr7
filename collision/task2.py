def isCorrectRect(rect):
    try:
        (x1, y1), (x2, y2) = rect
        if x1 >= x2 or y1 >= y2:
            return False
        return True
    except:
        return False