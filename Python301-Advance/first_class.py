class Animal:
    property_1 = "Something"

the_animal = Animal()
print(the_animal.property_1)

#^ --Class Properties--

class Animal:
    #^ property can be dictionary 
    this_is_a_property = {
        'key_1':'Value1'
    }
    #^property can be list 

    this_list = ['Kane','Kalob','Gully']

the_animal = Animal()
print(the_animal.this_is_a_property)
# {'key_1': 'Value1'}
print(the_animal.this_is_a_property['key_1'])
# Value1

print(the_animal.this_list)
# ['Kane', 'Kalob', 'Gully']
print(the_animal.this_list[2])
# Gully

# ^ Now when it comes to assigning the peoperties automatically we can do that with a thing called dundar .double underscore method we will see it later

#^ We can also access the class by directly its name instead of throwing it in to a variable 

print(Animal.this_list)
['Kane', 'Kalob', 'Gully']

 #  ^    ---CLASS METHODS--- 

class Animal:
     this_is_a_property = {
        'key_1':'Value1'
    }
    
     this_list = ['Kane','Kalob','Gully']

     def this_is_a_method(self):
         print(self.this_list)

the_animal =Animal()

the_animal.this_is_a_method()
# ['Kane', 'Kalob', 'Gully']

#
#^ on a standard method inside of a class ,its first parameter is always self ,in js its this 
#^ self is used inside the class but outside the class we can completely ignore it 
#^ As the_aniaml is a class object ,it going to have acess to everythin inside of a class 
#^ with self we have access to methods an dproperties inside the class 
#^ here self is referring to the Animal class that we are working in 


#^ We an also define properties using methods -we can create a class variable ,based on a class function


class Animal:
     this_is_a_property = {
        'key_1':'Value1'
    }
    
     this_list = ['Kane','Kalob','Gully']

     def add_name(self, name):
        self.this_list.append(name)
        return self.this_list

     def this_is_a_method(self):
         print(self.this_list)

     @property
     def get_gully(self):
         return self.this_list[2]
         

the_animal =Animal()

the_animal.this_is_a_method()
gully = the_animal.get_gully
print("The cutest gatoof all the time is ",gully)
#^ property is basically a decorator ,saying even though this is an executable object or we call it callable ,treat it as if it is not a callable ,treat it as a standard property
#^when property is used paranthesis is not there ->  gully = the_animal.get_gully

the_animal.add_name("Rhubarb")
print(the_animal.this_list)

# ['Kane', 'Kalob', 'Gully', 'Rhubarb'] 