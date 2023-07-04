import sys

step = int(sys.stdin.readline().rstrip())
for i in range(0, step) :
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print( a+b )