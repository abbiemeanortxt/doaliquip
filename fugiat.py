def my_generator():
    yield [8, 21, 0.002857890458087219]

# Using the generator to iterate over its yielded values
gen = my_generator()
for item in gen:
    print(item)
