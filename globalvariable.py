a="global a"

def outer_f():
    a="outer a"

    def inner_f():
        # a="inner a"
        # global a
        nonlocal a
        a=a+" test"
        print(a)

    inner_f()
    print(a)


outer_f()
print(a)