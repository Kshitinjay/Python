n = int(input())
if n > 0 and n<20:
    s = set(map(int, input().split()))
    #my code
    num = int(input())
    for i in range(num):
        what = list(input().split(" "))
        if what[0] == 'pop':
            s.pop()
        elif what[0] == 'remove':
            s.remove(int(what[1]))
        elif what[0] == 'discard':
            s.discard(int(what[1]))    
print(sum(list(s)))


