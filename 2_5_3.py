ls = [int(i) for i in input().split()]
ls2 = []
# print(ls.count(3))
for i in ls:
    if ls.count(i) > 1 and i not in ls2 :
        ls2.append(i)
    else:
        continue
ls2 = sorted(ls2)
print(*ls2)
    

