def my_generator():
    for num in range(50):
        yield num ** num

# yield is just like return but in generator we use yield
my_var_gen = my_generator()
all_numbers = list(my_var_gen)
print(all_numbers)

for big_num in my_generator():
    print(big_num)


#^  so one thing to keep in mind with the generator, it's a one done thing once you exhaust that generator,

# it's done.

# You have to create a new one.

# Or not create a new one.

# That's bad wording, but you have to instantiate or generate a new generator.
# Once you've created that new generator, then you can do whatever you want with it, but if you try

# to execute that generator more than once, if it's like, for example, stored in a variable.

# Is going to be exhausted that first time and only cares about performing once, it's not like a function,

# a function you can keep using over and over and over again.

# A generator is a one and done type thing.