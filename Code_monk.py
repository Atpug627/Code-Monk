from collections import deque

def monk_test(size_of_Array,rotations,A):
  if len(A) == size_of_Array:
    de = deque(A)
    de.rotate(rotations)
    A = list(de)
    return A

T = int(input())
while T:
  size_of_Array, rotations = map(int,input().split(" "))
  A = list(map(int,input().split(" ")))
  print(*monk_test(size_of_Array, rotations,A))
  T = T - 1
  if T == 0:
    break