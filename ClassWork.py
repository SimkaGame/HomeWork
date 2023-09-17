import random
import time

a = []

for g in range(0,99999):
    a.append(random.randint(0,100))
N = len(a)

bubble_a = a
quick_a = a
d_a = a
def bubble(x):
    for i in range(0, N-1):
        for j in range(0, N-1-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] =  x[j+1], x[j]
    return x

def quicksort(a):
   if len(a) <= 1:
       return a
   else:
       q = random.choice(a)
       s_a = []
       m_a = []
       e_a = []
       for i in a:
           if n < q:
               s_a.append(i)
           elif n > q:
               m_a.append(i)
           else:
               e_a.append(i)
       return quicksort(s_a) + e_a + quicksort(m_a)



print(a)
start_bubble = time.time()
print(bubble(bubble_a))
end_bubble = time.time() - start_bubble
print(end_bubble)

start_quick = time.time()
print(quicksort(quick_a))
end_quick = time.time() - start_quick
print(end_quick)



