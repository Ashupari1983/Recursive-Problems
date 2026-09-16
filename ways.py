def ways(stairs):
    if stairs<0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs-1) + ways(stairs-2)

a = int(input('Enter number of stairs: '))
print('Possible ways: ',ways(a))