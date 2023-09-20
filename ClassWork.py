# import random
# import time

# a = []
# a_bubble=[]
# a_quick=[]
# a_choise=[]
# for i in range(0,999):
#     num = random.randint(1,1000)
#     a.append(num)
#     a_bubble.append(num)
#     a_quick.append(num)
#     a_choise.append(num)

# def bubble(x):
#     for i in range(0, N-1):
#         for j in range(0, N-1-i):
#             if x[j] > x[j+1]:
#                 x[j], x[j+1] =  x[j+1], x[j]
#     return x

# def quick(x):
#    if len(x) <= 1:
#        return x
#    else:
#        q = random.choice(x)
#    l_x = [n for n in x if n < q]
#    e_x = [q] * x.count(q)
#    b_x = [n for n in x if n > q]
#    return quick(l_x) + e_x + quick(b_x)

# def choise(x):
#     n = len(x)
#     for i in range(n-1):
#         m = i
#         for j in range(i+1, n):
#             if x[j] < x[m]:
#                 m = j
#         x[i], x[m] = x[m], x[i]
#     return x

# print("массив", a)

# start_bubble = time.time()
# print("пузырек", bubble(a_bubble))
# end_bubble = time.time() - start_bubble
# print(end_bubble)
# start_quick = time.time()
# print("быстрая", quick(a_quick))
# end_quick = time.time() - start_quick
# print(end_quick)

# start_choise = time.time()
# print("выборочная", choise(a_choise))
# end_choise = time.time() - start_choise
# print(end_choise)
cm = int(input())
print(cm//100)