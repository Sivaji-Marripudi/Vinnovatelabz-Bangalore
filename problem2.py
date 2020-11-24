a = input()
r = []
for i in list(a):
    if i not in r:
        r.append(i)
print(''.join(r))