import sys

def min(x1,x2):
    if(x1<x2):
        return x1
    return x2

A1 = int(sys.stdin.readline())
A2 = int(sys.stdin.readline())
A3 = int(sys.stdin.readline())

t1 = (A2 << 1) + (A3 << 2)
t2 = (A1 << 1) + (A3 << 1)
t3 = (A1 << 2) + (A2 << 1)

print(min(t3,min(t1,t2)))


