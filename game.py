print("welcome to choose your own adventure game")
play = input("do you want to play this game! yes for play, no for quit\n").lower()
if play == "yes":
   print("nice let's the game")
   answer1 = input("you are walking, it started raining. what would you do head back to house or go to you destination! back for head back and go to go to the destination\n").lower()
   if answer1 == "go":
        answer3 = input("you are walking to your destination but then you suddenly hear a shouting voice! what would you do go to your destination or go to see thr voice what happened! destination for go to destination and see to get see the voice\n").lower()
        if answer3 == "destination":
            answer6 = input("you avoid that and start moving again to the destination\n")
        elif answer3 == "see":
            print("you go to see what happend the the person killed you who killed the homeless man\n")
        else:
            print("wrong option you died")

   elif answer1 == "back":
        answer2 = input(" you have started to head back to your house and then the man came to for the to stay in your house! what would you do stay him in your house or leave him outside! outside for leave him outside and stay for stay him inside\n").lower()
        if answer2 == "outside":
             answer4 = input("you left him outside and he gone but the bring more peaple with himself and started to broke th door! what would you do leave the house from the back door or call 911! 911 for call 911 and backdoor for leave for backdoor\n").lower()
             if answer4 == "911":
                print("they came in and killed you\n")
             elif answer4 == "backdoor":
                  answer5 = input("you left the house and came the house that was nearby and you can ask help or go straight! ask for the ask the help and straight to go staraight\n").lower()
                  
        elif answer2 == "stay":
             print("you let him stay in your house and he was a killer and you died! game over\n")
        else: 
            print("not a option you died\n")
   else:
    print("not a option you died\n")
else:
    print("i am very sad you don't want to play my game\n")