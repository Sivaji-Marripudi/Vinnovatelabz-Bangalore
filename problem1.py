a = list(map(int,input().split()))
key = int(input())
l = []
for i in range(0,len(a)-1):
    if a[i] + a[i+1] == key:
        l.append(a[i])
        l.append(a[i+1])
print(l[:2])