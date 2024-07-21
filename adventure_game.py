name = input("Please type your name: ")
print("Welcom to the adventure game", name)

print("You are in a junle alone after your plane crashed")
answer = input("It's getting dark and you need to sleep. Should you sleep on ground or make a bed with leaves. Type ground/bed: ").lower()
if answer == "ground":
    print("You got bitten by a snake during your sleep and died!")
elif answer == "bed":
    print("You got good sleep and woke up to the morining sound of junlge!")
    answer = input("You are hungry should you eat random fruits in junlge or go to beach to find coconut. Type fruit/beach: ").lower()
    if answer == "fruit":
        print("You ate random fruit and it was poisonous and you died!")
    elif answer == "beach":
        print("You went to beach and found coconut which not only fed you but also quenched your thirst")
        answer = input("Now you need to save yourself from this island. You can see a buried rusted old ship into water. Should you go to the ship or wait into beach. Type ship/wait: ").lower()
        if answer == "ship":
            print("You weat into water to salvage the ship and got eaten by a shark and died!")
            print("You lost! Going into water was never a good idea.")
        elif answer == "wait":
            print("You maid a makeshift sos signal wiht stick and waited on beach")
            answer = input("Night is coming. You need to decided wether to start a fire or sleep in dark. Type dark/fire: ").lower()
            if answer == "dark":
                print("You saw a faint light flick on the horizon. You screamed for help but were unsuccessful in gaining it's attention and died to random animal")
            elif answer == "fire":
                print("You saw a faint light flick on the horizon. You decided to light a stick on fire and waved it in air. The light noticed you it was a ship and got saved and returned home.")
                print("Congratulation! You completed the game.")
            else:
                print("You decided to do nothing and died.")
                print("You lost! You need to be a little more decisive")
        else:
            print("You decided to do neither and head back into junle and died when night hit!")
            print("You lost! Try different path next time")
    else:
        print("You decided to do nothing and died from dehydration")
        print("You lost! Try different path next time")
else:
    print("You got mad due to lack of sleep and died to an animal!")
    print("You lost! Try different path next time")

