def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


def repeat_num(num):
    def decorator(func):
        def wrapper():
            print("方法执行前")
            for i in range(num):
                func()
            print("方法执行后")

        return wrapper

    return decorator


@repeat_num(4)
def say_hello():
    print("Hello!")


say_hello()
