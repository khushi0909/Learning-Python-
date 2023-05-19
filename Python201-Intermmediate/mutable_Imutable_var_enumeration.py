# i.e changeable vs unchangeable 
#^ When you are working with certain variables ,certain things are immutable or changeable and some things are immutable 
#^ so,for example you might be thinking that  a string is mutable ,it actually not its not changeable 

#^ so if we have some sort of string such as 

string = "The fox jumped over the cow"

#^ Here, whats happening behind the scene is ,string with fox line is taking that particular string and jamming in to a little piece of memory on your computer
#^ now behind the scenes we cannot change it whatsoever,so if you do 

print(string.upper())
print(string)

# and lets print regular string 

#^ you will see that one line is upper case line and other is the regular string and what we actually see is string taking all of this,turning in to uppercase but its not restoring it to particular variable 

#^ what it is actually doing is holding in memory and then lettign you use it 
string = "overwritten "

#^ So, if you try to overwrite it with other string ,what it do is it hold a piece of memory for both 

#^ Another example
#^  even though individual string is immutable, list is mutable ,means you can append etc 

names = ["Kalob", "Jacob", "Gully", "Amanda"]
names.append("Rhubarb")
print(names)


#^ here we are not doing names =names.append("Rhubarb")
#^ ['Kalob', 'Jacob', 'Gully', 'Amanda', 'Rhubarb']
#^ unlike string list didnt saved it as old list or as in string we can say it didnt save it as uppercase 

#^ list set that variable with new strings


#* -------------- Enumerations ----------------------  (It gives list of tuple or tuple )

#^we are going to loop through  some sort of list and we are going to get the index from it so we cpuld create a list ,lets say 

animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]
for animal in enumerate(animals):
    print(animal)

#^ without enumerate we will ge simple list as Gully Rhubarb Zeohyr Henry 
# ^ but when we use enumerate we will get a tuple in a king of list with numbers 1 2 3 ...

# (0, 'Gully')
# (1, 'Rhubarb')
# (2, 'Zephyr')
# (3, 'Henry')


for index, animal in enumerate(animals):
     print(index,animal)

# 0 Gully
# 1 Rhubarb
# 2 Zephyr
# 3 Henry
for index, animal in enumerate(animals):
     print(animal)

# Gully
# Rhubarb
# Zephyr
# Henry
for index, animal in enumerate(animals):
    print(f"{index+1}.\t{animal}")

# 1.      Gully
# 2.      Rhubarb
# 3.      Zephyr
# 4.      Henry
# 
for index, animal in enumerate(animals):
    if index % 2 == 0:
        continue

    print(f"{index+1}.\t{animal}")
# 2.      Rhubarb
# 4.      Henry