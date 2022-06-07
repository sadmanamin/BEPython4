

def second_func(func):
    print("Second function running")
    def inside_function():
        
        # print(func)
        func()
        print("This is second function")

    return inside_function

@second_func
def first_func():
    print("This is my first function")


print(first_func)
first_func()