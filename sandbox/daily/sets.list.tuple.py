# LIST
# ordered
# mutable
list_ = ['a', 'b', 'c', 'a']


# TUPLE
# ordered
# immutable - once created, can't be changed
# don't have append or remove methods
tuple_ = ('a', 'b', 'c', 'a')

# if you try changing it's value
# tuple_[1] = 's'
# we get error 
# TypeError: 'tuple' object does not support item assignment


# SET - drops duplicates upon creation
# Unordered - can't index it, have no positional arguments, you can't [0] them
# trying to update with index compiler throws error
# TypeError: 'set' object is not subscriptable
set_ = {'a', 'b', 'c', 'a'} 

# mutable 
set_.add('z')
set_.remove('z')



