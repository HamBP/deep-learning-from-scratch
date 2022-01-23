def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 1

    if x1 * w1 + x2 * w2 > theta:
        return 1
    else:
        return 0