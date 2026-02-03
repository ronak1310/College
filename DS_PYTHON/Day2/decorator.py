def test(fun):
    def abcd():
        print("Good Afternoon!!")
        fun()
        print("Thanks!!")
    return abcd

@test
def hello():
    print("Hello All!!")
    print("Welcome to MU!!")

hello()