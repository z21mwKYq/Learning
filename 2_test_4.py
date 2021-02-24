n= []
while True:
    ls = [int(i) for i in input().split() if i != 'end']
    if not ls:
        break
    n.append(ls)
print(n)

# for i in range(3):
#     ls = [int(i) for i in input().split()]
#     if ls[0] == 'end':
#         break
#     # print(ls)
#     n.append(ls)
#     print(n)
# ls = [1,2,3,4]
# dd = [5, 6, 7, 8]
# ls.append(dd)
# print(ls)