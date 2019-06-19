def average(array):
    s = set(array)
    l = len(s)
    Sum = sum(s)
    x = Sum/l
    return x

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)