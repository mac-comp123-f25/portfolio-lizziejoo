def smallest_diff(x, y, z):
    print('smallest_diff inputs:', x, y, z)
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    print(diff1, diff2, diff3, 'return value:', min_diff)
    return min_diff

smallest_diff(32, 43, 90)
smallest_diff(3, 9, 5)

print(smallest_diff(32, 43, 90))
print(smallest_diff(3, 9, 5))
