def curly(n, l=0, r=0):
    if l==n and r==n:
        return ['']
    total = []
    if l>r:
        for i in curly(n, l, r+1):
            total.append('}' + i)
    if l<n:
        for i in curly(n, l+1, r):
            total.append('{' + i)
    return total

a = int(input('Enter the number of brackets: '))
print('Possible ways to close all brackets: ',curly(a))