# def fun():
#     print("Hello!")

# def add(a,b):
#     print(a+b)

# def mul(a,b):
#     c=a*b
#     return c

# fun()
# add(12,12)
# multiply=mul(12,12)
# print(multiply)

# def hello():
#     print("Hello")
# abc=hello
# abc()
# abc=12
# print(abc)

# def hello():
#     print("Hello")
# num=45
# def test(arg):
#     print("Test")
#     arg()
# test(hello)

def hello():
    print("Hello")
    def test():
        print("Test")
    return test

# abc=hello()
# abc()
hello()()