import numpy as np
import time
from numba import njit
import numba

@njit
def _inc(ids):
    for i in range(len(ids)):
        ids[i]+=1
        ids[i]%=18
        if ids[i]:
            break
    return ids

@njit
def _is_valid(length,ids):
    for i in range(length-1):
        if ids[i]//3==ids[i+1]//3:
            return False
        if ids[i]//6==ids[i+1]//6 and (ids[i]//3)%2:
            return False
    for i in range(length-2):
        if ids[i]//6==ids[i+1]//6 and ids[i]//3==ids[i+2]//3:
            return False
    return True    

@njit
def _increment(length,ids):
    ids = _inc(ids)
    while not _is_valid(length,ids):
        ids = _inc(ids)
    return ids

@njit
def gen_algs(n):
    ids = np.array(([0,3,6]*int(n/3+1))[:n], dtype = numba.u1)
    start = np.array(([0,3,6]*int(n/3+1))[:n], dtype = numba.u1)
    algs = np.zeros((18*15**(n-1),n), dtype = numba.u1)
    algs[0] = ids.copy()
    _increment(n, ids)
    i = 1
    while not (ids==start).all():
        algs[i] = ids.copy()
        i += 1
        _increment(n,ids)    
    
    return algs[:i]
    
gen_algs(1)

all_algs = []
t = time.time()
times = []
for n in [1,2,3,4,5,6]:
    ti = time.time()
    all_algs.append(gen_algs(n))
    times.append(time.time()-t)
print(times,sum(times))
tot = 0
for algs in all_algs:
    tot += len(algs)
print(all_algs)