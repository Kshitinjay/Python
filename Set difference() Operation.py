# Enter your code here. Read input from STDIN. Print output to STDOUT

 # Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
s1 = list(map(int,input().split()))
b = int(input())
s2 = list(map(int,input().split()))

main_set1 = set(s1)
main_set2 = set(s2)
x = main_set1.difference(main_set2)
print(len(x))