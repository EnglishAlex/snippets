#Josephus Permutation 
#
#https://www.youtube.com/watch?v=eCDFA02SiIA


from collections import deque
import time 

def solveJ(array, k):
    d = deque(array)
    permutation = []
    while d:
        d.rotate(1-k)
        item = d.popleft()
        permutation.append(item)
    return permutation

soldiers = 30
arr = [s+1 for s in range(soldiers)]
k = 9
start = time.perf_counter()
perm = solveJ(arr, k)
stop = time.perf_counter()
print (stop-start)
