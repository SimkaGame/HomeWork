from pprint import pprint
s = str(input())
s1 = s.split()
a = {}
while True: 
    if len(s1)>=10:
        for i in s1:
            if i not in a:
                a[i]=1  
            else:
                a[i]+=1
        pprint(a)
        break
    else:
        print('Строка меньше 10 символов')
        s = str(input())
        s1 = s.split()