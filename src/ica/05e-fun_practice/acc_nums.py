def sum_range(start_val, end_val):
    cnt = 0     # initialize accumulator to default value 0
    for x in range(start_val, end_val + 1):
        cnt = cnt + x     # update: add new x value to old value of cnt
    return cnt

print(sum_range(2, 4)) # adds all values in range together
print(sum_range(3, 3)) # gives same number
print(sum_range(10, 5)) # gives zero
print(sum_range(-4, -2)) # gives negative number