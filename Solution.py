# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
for _ in range(int(input())):
    x = set(map(int,input().split()))
    if A.issuperset(x) != True or len(A) == len(x):
        print(False)
        break
else:
    print(True)
