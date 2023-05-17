import random 

while True:

    my_answer = input("Choose:rock,paper,scissors:  ")
    my_answer = my_answer.lower()

    if my_answer == "quit":
        break
    if my_answer != "rock" and my_answer!="paper" and my_answer != "scissor":
        print("please choose a correct answer---> ")
        continue
    computer_answer = random.choice(["rock","paper","scissor"])
    print(f"Computer choose:{computer_answer}")

    if my_answer == computer_answer:
        print("you tied")
        continue
    elif my_answer == "paper" and computer_answer == "rock" :
         print("YOU WIN!")
         break
    elif my_answer == "rock" and computer_answer == "scissor":
        print("YOU WIN!")
        break
    elif my_answer == "scissor" and computer_answer =="paper":
        print("YOU WIN!")
        break
    else:
        print("You lose .Try again!")
        


