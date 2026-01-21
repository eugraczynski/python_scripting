# simple generator iteration using next
import time


def gen_yields():
    yield 1
    yield 2
    yield 3


gen_yields_var = gen_yields() # you cant just next(gen_yields) because gen_yields is a function, not a generator object
# print(next(gen_yields_var)) 
# print(next(gen_yields_var))
# print(next(gen_yields_var))


# iteration through generator using for loop
for value in gen_yields():
    pass # print(value)

# when useful
# the range(1000000000000000) is just an example of a long operation
# python need to store all values in memory 
# yield allows to produce items one at a time and only when requested
# saving memory and time

def long_operation():
    for num in range(10000000):
        if num % 100 == 0:
            yield num


long_op_gen = long_operation()
start = time.time()

print(next(long_op_gen)) 
print(next(long_op_gen)) 
print(next(long_op_gen))
print(next(long_op_gen)) 
print(next(long_op_gen)) 
print(next(long_op_gen)) 
print(next(long_op_gen)) 

end = time.time()
print(f"{end - start:.10f} seconds")


'''
Yield is more efficient, memory-wise, and also sometimes execution-wise. 
If you iterate over a list of 1,000,000 elements, Python has to generate the entire list and store the contents in memory before beginning the first iteration. 
With a generator (using yield), the elements are created at the time of iteration, so 1,000,000 elements don’t need to be pre-calculated first and stored in memory.

There are other benefits such as using generators with async or performing logic after certain iterations
(that generators can potentially give better control over than iterating over a list), but in my opinion the main reason for 
using them is the memory and processing considerations.'''