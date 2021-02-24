# s = input('Введите строку ')
# print(s.find('b'))
# num = 1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         num +=1

#     else:
        
#         print(s[i] + str(num), end='')
#         num = 1
#         print(s[i+1] + str(num), end='')
        






message = str(input())
cnt = 1
x = 1
j = message[x:x+1]
for i in message:
    if i in j:
        cnt += 1
    else:
        print(i, end='')
        print(cnt, end='')
        cnt = 1
    x += 1
    j = message[x:x+1]