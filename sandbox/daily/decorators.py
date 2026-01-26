# @time_dec # decorator is not globally available
# TODO: find a way to share decorators across project
import time


def time_dec(base_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        a = 123
        base_func(a, *args, **kwargs)
        end = time.time()
        print(f"Function '{base_func.__name__}' executed in {end - start:.10f} seconds")
        print(f"1nd decorator executed {time.time()}")
    return wrapper

@time_dec
def func_(a):
    print(f"Inside func_ with a={a}")

func_()

# @time_dec is a syntax 
# that literally does: 
# func_ = time_dec(func_)


# decorator x times runner
def time_dec_x_times(x):
    def decorator(base_func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(x):
                base_func(*args, **kwargs)
            end = time.time()
            print(f"Function '{base_func.__name__}' executed {x} times in {end - start:.10f} seconds")
        return wrapper
    return decorator

@time_dec_x_times(5)
def func_2():
    print("Inside func_2")

func_2()