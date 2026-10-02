# def fun(b,*a):
#     print(type(b))
#     print(b)
#     print(type(a))
#     print(a)


# fun(1,2,3,4,5)

# def fun(a,b,c):
#     print(a,b,c)

# fun(b=1,a=2,c=5)

def fun(**name):
    print(name["firstname"])

fun(firstname="md",lastname="rifat")