n= []
while True:
    ls = [int(i) for i in input().split() if i != 'end']
    if not ls:
        break
    n.append(ls)

print(n)

ls2 = [[0 for i in range(len(n[0]))] for j in range(len(n))]
print(ls2)

for i in range(len(n)):
    for j in range(len(n[0])):
        s = 0
        for di in range(-1:2):
            for dj in ranf

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