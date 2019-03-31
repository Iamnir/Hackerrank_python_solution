# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X=input().split()
print (*[sum(x)/float(X) for x in zip(*[list(map(float, input().split())) for _ in range(int(X))])],sep='\n')
