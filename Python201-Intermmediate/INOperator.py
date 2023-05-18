
    #*    i can write IN Operator to compare one thing against a list or an array 
# * i can write IN Operator to compare one thing against a list or an array 

#* names = ["killa","john","gullly"]

# * if we need to find our input name agaist a list 

#* now if we have to loop we do it as 

# for name in names:
#     if my_name == name:
#         print("THis is the name")

# but if there are thousand of item to array it seems little bit too much ,so other way is the in operator 

# "john" in names 

#* if you type all of the above in the terminal you will get answer for "jhon" in  names as True 

my_answer = "rock"
options = ["rock","paper","scissor"]
if my_answer in options :
    print("Rock is one of the possible options! ")
    #answer:Rock is one of the possible options!

my_answer = input("what is your answer !!?? ")
options = ["rock","paper","scissor"]

if my_answer in options:
    print("That option is viable option")
else:
    print("Wrong answer try again")





key = "name"
person = {
    "name": "Kalob",
    "profession": "coding teacher",
}

if key in person:
    print("Name is a valid dictionary key in the person object ")


    # // now change the key name and try if wrong will do nothing
    # *// we can also do this in tuple also in set 


thisset = {"apple", "banana", "cherry"}
myans = input("choose your answer!!")

if myans in thisset:
        print("ans is in set")


