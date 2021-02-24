# n = int(input())
# ls = [str(i) * i for i in range(1, n+1)]
# s = "".join(ls)[:n]
# print(s)
# for i in s:
#     if i == s[-1]:
#         print(int(i))
#         break    
#     print(int(i), end=' ')
# #TODO   

n = int(input())
v = []
for i in range(1, n+1):
    v += [str(i)] * i
print(v)

print(" ".join(v[:n]))