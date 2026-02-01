import time
from typing import Any, Callable, Generator

def time_dec_x_times(x: int=1):
    def decorator(base_func: Callable[..., list[int] | None | Generator[list[int], Any, None]]):
        def wrapper(*args: ..., **kwargs: ...):
            start = time.time()
            for _ in range(x):
                base_func(*args, **kwargs)
            end = time.time()
            print(f"{end - start:.10f} seconds")
        return wrapper
    return decorator

@time_dec_x_times()
def compute_time() -> list[int]:
    rv: list[int] = []
    for i in range(10):
        if i % 2 == 0:
            rv.append(i)
        time.sleep(0.5)
    return rv

# compute_time()

@time_dec_x_times()
def compute_time_2():
    rv: list[int] = []
    for i in range(10):
        if i % 2 == 0:
            rv.append(i)
        time.sleep(0.5)
    yield rv

# compute_time_2()


def api():
    x = 'first action'
    yield x
    y = 'second action'
    yield y
    z = 'third action'
    yield z

# if function contains yield keyword, it becomes generator
print(type(api()))

x = api()

print(type(x))


# looping through generator
for y in x:
    print(y)

# which is equal to:
# print(next(x))
# print(next(x))
# print(next(x))

