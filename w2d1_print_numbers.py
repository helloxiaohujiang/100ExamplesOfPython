# print numbers from 1 to 100 using loop
# i = 1
# while i <= 100:
#     print(i)
#     i +=1

for i in range(1,101):
    print(i, end=', ' if i < 100 else " ")