def curly(n, l=0, r=0):
    if l==n and r==n:
        return 1
    total = 0
    if l>r:
        total += curly(n, l, r+1)
    if l<n:
        total += curly(n, l+1, r)
    return total

a = int(input('Enter the number of brackets: '))
print('Possible ways to close all brackets: ',curly(a))