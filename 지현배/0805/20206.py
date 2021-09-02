def sol():
    A, B, C = map(int, input().split())
    X1, X2, Y1, Y2 = map(int, input().split())
    
    if B == 0:
        x = -C / A
        if X1 < x < X2:
            return 'Poor'
        return 'Lucky'

    y_x1 = -(X1 * A + C) / B
    y_x2 = -(X2 * A + C) / B
    if Y1 < y_x1 < Y2:
        return 'Poor'
    if Y1 < y_x2 < Y2:
        return 'Poor'

    if A == 0:
        y = -C / B
        if Y1 < y < Y2:
            return 'poor'
        return 'Lucky'

    x_y1 = -(Y1 * B + C) / A
    x_y2 = -(Y2 * B + C) / A
    if X1 < x_y1 < X2:
        return 'Poor'
    if X1 < x_y2 < X2:
        return 'Poor'

    return 'Lucky'

print(sol())