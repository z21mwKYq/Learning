ls = [int(i) for i in input().split()]
ls2 = []
end_of_list = len(ls)- 1
if len(ls) ==1:
    print(ls[0])
else:
    for i in range(len(ls)):
        if i == 0:
            ls2.append(int((ls[i+1] + ls[-1])))
        elif i == end_of_list:
            ls2.append(int(ls[i-1]+ls[0]))
        else:
            ls2.append(int(ls[i-1] + ls[i+1]))
    print(*ls2)
