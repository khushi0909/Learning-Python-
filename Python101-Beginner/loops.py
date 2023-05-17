
#TODO FOR LOOPS

#* for is used to iterate through some sort of iterable 

fav_foods = ["Pizza","Tacos","Salmon"]


for food in fav_foods:
        print(food)

        # you can do this with strings ,sets, tuples etc -try it 

        # you can also do it with the dictionary lets see 
person = {
                "name":"Kalob",
                "twitter":"@ksksksk",
                "instagram":"@owowow"
        }
for value in person:
         print(value)
for key,value in person.items():
         print(f"The key is {key} and the value is {value}")
             

# answer is :
# Pizza
# Tacos
# Salmon
# name                                    //  (printing only values )
# twitter
# instagram
# The key is name and the value is Kalob    (printing both key and values )
# The key is twitter and the value is @ksksksk
# The key is instagram and the value is @owowow

#TODO WHILE LOOPS

#* whiles loops are not like for loop ,in for loop is going to loop through every item in iterable untill it exhaust itself and then its going to silently finish 
#* and we dont need to worry about handling that sort of finish and while loop we need to take care of finish


# *             while True:
# *                    do something 

#* this can be little dangerous ,as you want to be careful with this ,but what we can do is to loop through something .untill we tell to not do ,
#* and we dont explicitly need some sort of iterable
num=0
while num <= 10:
    print(num)
    num = num + 1         #(this need to be managed by yourself,contrast to for loop and this will run untill its gonna be false)
# answer is :0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#TODO break and continue 

#* how we can break out of the loop or how we can skip some numbers in the loop

items = ["one","two","three","four","five"]

# for item in items:
#         if item == "two":       
#                 continue       # anythin below this continue is not going to get executed in the for loop
#         print(item)

        #answer one
# three
# four
# five

for item in items:
        if item == "three":       
                break           #it will completely get out of this for loop alltogether 
        print(item)

# answer:
# one
# two
num = 0
while num <=10:
        num = num + 1           #
        
        if num%2 ==0:
                continue
        print(num)

        #answer 
#         1
# 3
# 5
# 7
# 9
# 11

num = 0
while num <= 1_00_000:
        num = num + 1
        if num == 5:
                break
        print(num)

        # answer: 1 2 3 4