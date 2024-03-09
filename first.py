# a = 29
# prime = True
# for i in range(2, a):
#     if(a%i==0):
#         prime = False
# if(prime):
#     print("It is prime")
# else:
#     print("Not prime")

# fibonacci
a = 0
b = 1
print(a)
print(b)
for i in range(1, 10):
    c = a+b
    print(c)
    a = b
    b = c
