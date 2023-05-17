
#TODO: Numeric Data Type 
items = 4 

price = "19.97 "
total = items* price 

print(total)

#answer is : 19.97 19.97 19.97 19.97 

items = 4 

price = 19.97
total = items* price 

print(total)
# answer is :79.88
print(1_000_000_000) # to make it readable we can use underscores,pythin dosent care about that  )

# answer is : 1000000000

#TODO: STRING DATA TYPES

sentence ="""A sentence inm 
            here"""                 # it should be inside "" or ""
# if sentence is long and goes in new line then it should be inside """  """"
# even you want to change text,then run the file i terminal and again write sentence ="a thing here ",it will assign new sentence 
#and after that if you type sentence .      ,you can see whole lot of functions that you can perform on it ex:sentence.upper()
#also you can do ------>    type(sentence),answerwll be  <class 'str'>

print(sentence.upper())

#TODO: LIST DATA TYPES
lst = ["String",1,[34,"ddd"],"kukukkuk"]        # tis is list and store multiple values 
print(lst)              # thsi is not exactly useful becoz itwill be printing the same as we wrote 

# answer is :['String', 1, [34, 'ddd'], 'kukukkuk']

for item in lst :           #for every item in our list print all the items (looping)-will learn more in future about this 
    print("The item is :",item)

    #answer is : The item is : String
#The item is : 1
#The item is : [34, 'ddd']
#The item is : kukukkuk

#ther are different methods that can be performed on it ex:lst.remove("kukukkuk") etc 


#TODO: Dictionary Data TYPES -its actually a data structure 

person = {
    "key": "value",
    "name":"apart",
    "twitter":"@kslsklslk"

}

print(person['twitter'])
#answer is : @kslsklslk

person['instagram']= "@coding"
print(person)

# answer is : {'key': 'value', 'name': 'apart', 'twitter': '@kslsklslk', 'instagram': '@coding'}

del person ['key']
print(person)

#answer : {'name': 'apart', 'twitter': '@kslsklslk', 'instagram': '@coding'}

#you can have dictonary inside dictionary 


#TODO: TUPLE DATA TYPE
foods =('pizza','fish','fish','tomatoes')          #this iss a tuple inside ()

for food in foods :
    print("the food is:",food)


#answer:- the food is: pizza
#the food is: fish
#the food is: fish
#the food is: tomatoes


#Tuples are restrictd list 
# they are lot like list in the sense they are iterable,but difference is tuple is immutable i.e not changeable
# there are many mehods not availbale on tuples such as sort append  etc ,only very very few are available such as .count,.index 
#you ca check by intializing tuple with variable name and in terminal typing--->  variablename.    ,this will give you list of available methods 
#if you ever needs to create a list that never need to be sorted or never needs to be canged or never needs to do anything ,there comes tuple

#TODO: SET DATA TYPE 

# they kind of look like a dictionary 

# it doesnt take the key vallue pair ,it simply takes the items and the values as list does 

lst = ["varname","varname2","varname2","varname3"]
print(lst)
#answer is :['varname', 'varname2', 'varname2', 'varname3']
dictionary = {
    "key": "value"
}


# set is not going to maintain its order ,it doesnt remember ordering of list as we write 


s = {"item1","item2","item3"}
print(s)

# answer is :{'item2', 'item3', 'item1'}

# set is going to say otem 2 and item2 are exact same and treat them as one ,even if you write ittwice 
s = {"item1","item2","item2","item3"}

print(s)
#answer is :{'item1', 'item3', 'item2'}


#if you will type in terminal setnamevariable. you can see multiple methods available ,here still more methods available then tuple 


#TODO BOOLEAN DATA TYPE 

# its True or False value ,either 1 or 0  
can_code = True
if can_code == False :
    print("you can code ")

   # answer is :  "it will not print anything 
can_code = False
if can_code == False :
    print("you can code ")
#answer is : you can code

#TODO NONE DATA TYPE 

#its looks a lot like boolean,instead of lower case its upper case 

#its literally means nothing 
None

wallet = None

if wallet is None:

    print("There is nothing in my wallet ")
    wallet = 76.5

    print("ther is ",wallet)

    #ANSWERIS : There is nothing in my wallet
    #ther is  76.5

