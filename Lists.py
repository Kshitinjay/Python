if __name__ == '__main__':
    N = int(input()) # number of commands
    list = []
    for x in range(0,N):
        uin = input().split() #single input code to take all input string,position,value.
        if uin[0] == 'insert':
            list.insert(int(uin[1]),int(uin[2]))
        elif uin[0] == 'print':
            print(list)   
        elif uin[0] == 'remove':
            list.remove(int(uin[1]))
        elif uin[0] == 'append':
            list.append(int(uin[1]))
        elif uin[0] == 'sort':
            list.sort()
        elif uin[0] == 'pop':
            list.pop()
        elif uin[0] == 'reverse':
            list.reverse()          
