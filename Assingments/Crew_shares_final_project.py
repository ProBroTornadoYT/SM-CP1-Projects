# CREW SHARES CODE SM

import random

#the story

print("Yondu Udonta and his crew arrive at the Iron Lotus after several weeks of plundering various places around the galaxy. The crew has been in space for nearly six months and they are ready for a night of celebration. Yondu doesn't want to divvy up the plunder just yet, so he gives each crew member other than himself and Peter 3 units and sends them off to the Iron Lotus. After the crew has gone, he and Peter count what's left and decide how to split it up among the crew. Yondu takes 13% of the total. He then gives Peter 11% of what's left. The next morning, Yondu divides the remaining amount evenly among all of the crew, including Yondu and Peter. The crew does not know that Yondu and Peter have already taken a cut.")

#for some little white space

print("")
print("")
print("")

#Amt. of pirates

while True:                                                                                    #A loop to ensure that the user inputs a number for pirates
    try:
        pirates = input("How many pirates on the ship? (excluding yondu and Peter)").strip() #Asking the user for the number of pirates on the ship
        if not pirates.isdigit():
            print("Pirates must be a number")                                                #checking if the input is a number or not
            continue
        pirates = int(pirates)                                                                #Converting the input to an integer
        total_crew = pirates + 2                                                              #adding yondu and Peter to the total crew
        print("There are " + str(total_crew) + " members on board")                           #final output of the total crew
        break 
    except ValueError:                                                                       #if something goes wrong with the input, it will print an error message and ask for the input again
        print("Invalid input")

#for some little white space

print("")
print("")
print("")
 
#math time!

money_plundered= random.randint(500,5000)                                                                                      #generating a random number between 500 and 5000 to represent the amount of money plundered
print("They actually have "+ str(money_plundered) +" units of plundered money")                                                 #printing the amount of money plundered

money_after_3_units= money_plundered - (pirates) * 3                                                                            #money after giving 3 units to each pirate
print("Since youndu and quill gave 3 units to each member they total plunder is now at"+ str(money_after_3_units)+".")           #printing the amount of money left after giving 3 units to each pirate

#for some little white space

print("")
print("")
print("")
 
yondu_money_stolen = round(13/100 * (money_after_3_units), 2)                                                                                #yondu takes 13% of the total money after giving 3 units to each pirate
print("Now in the dead of the night yondu came and took 13% of the plunder which come upto a whopping "+str(yondu_money_stolen)+"UNITS!")     #printing how much he took

#for some little white space

print("")
print("")
print("")

peter_money_stolen = round(11/100 * (money_after_3_units - yondu_money_stolen), 2)                                                                           #peter takes 11% of the total money after giving 3 units to each pirate and after yondu took his share
print("After youndu's theft peter comes in the dead of the night and takes 11% of the left money which comes upto " + str(peter_money_stolen) + "UNITS!")    #printing how much he took

#for some little white space

print("")
print("")
print("")
# 67 TH line!!!!!!!!!!!!!!!!!!!!!!!

remaining_plunder = money_after_3_units - yondu_money_stolen - peter_money_stolen                                                                              #calculating the remaining plunder after yondu and peter took their shares

print(f"THE GREAT DAY OF SPLITTING HAS ARRIVED AND TOTAL PLUDER IS {remaining_plunder} !!! TIME TO SPLIT EACH PERSON GETS:")                                    #spiltting the remaining plunder among the crew
 
crew_share = round((remaining_plunder / total_crew) + 3, 2)                                      # splitting the remaining plunder among the crew and adding 3 units to each crew member's share not taking into account they must have spent it on food and driks

#Total money each got.

print(str(crew_share))

yondus_total_share = round(yondu_money_stolen + crew_share, 2)
print("Youndu got " + str(yondus_total_share))

peters_total_share = round(peter_money_stolen + crew_share, 2)
print("Peter got " + str(peters_total_share))

