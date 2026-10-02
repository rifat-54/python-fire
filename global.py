a="global a"

def fun():
    # a="local a"
    global a
    a=a+" test"
    print(a)

fun()
print(a)