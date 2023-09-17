import random
import time

a = []
b = []
c = []
d = []
for g in range(0,99999):
    a.append(random.randint(0,100))
N = len(a)

def bubble(x):
    for i in range(0, N-1):
        for j in range(0, N-1-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] =  x[j+1], x[j]
    return x
start = time.time()
print(bubble(a))
end - time.time()
print(end)