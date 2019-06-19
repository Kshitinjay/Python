n = int(input())
li = []
s = set()
for i in range(0,n):
    x = input()
    li.append(x)
for j in li:
    s.add(j)
print(len(s))
