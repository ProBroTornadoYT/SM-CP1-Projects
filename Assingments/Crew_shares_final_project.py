# CREW SHARES CODE SM

import random

#the story

print("Yondu Udonta and his crew arrive at the Iron Lotus after several weeks of plundering various places around the galaxy. The crew has been in space for nearly six months and they are ready for a night of celebration. Yondu doesn't want to divvy up the plunder just yet, so he gives each crew member other than himself and Peter Quill 3 units and sends them off to the Iron Lotus. After the crew has gone, he and Peter count what's left and decide how to split it up among the crew. Yondu takes 13% of the total. He then gives Peter 11% of what's left. The next morning, Yondu divides the remaining amount evenly among all of the crew, including Yondu and Quill. The crew does not know that Yondu and Quill have already taken a cut.")

#for some little white space

print("")
print("")
print("")

#Amt. of pirates

while True:
    try:
        pirates = input("How many pirates on the ship? (excluding yondu and Quill)").strip()
        if not pirates.isdigit():
            print("Pirates must be a number")
            continue
        pirates = int(pirates)
        total_crew = pirates + 2
        print("There are " + str(total_crew) + " members on board")
        break
    except ValueError:
        print("Invalid input")

#for some little white space

print("")
print("")
print("")
 
#math time!

money_plundered= random.randint(500,5000)
print("They actually have "+ str(money_plundered) +" units of plundered money")

money_after_3_units= money_plundered - (pirates) * 3
print("Since youndu and quill gave 3 units to each member they total plunder is now at"+ str(money_after_3_units)+".")

#for some little white space

print("")
print("")
print("")
 
yondu_money_stolen = round(13/100 * (money_after_3_units), 2)
print("Now in the dead of the night yondu came and took 13% of the plunder which come upto a whopping "+str(yondu_money_stolen)+"UNITS!")

#for some little white space

print("")
print("")
print("")

peter_money_stolen = round(11/100 * (money_after_3_units - yondu_money_stolen), 2)
print("After youndu's theft peter comes in the dead of the night and takes 11% of the left money which comes upto " + str(peter_money_stolen) + "UNITS!")

#for some little white space

print("")
print("")
print("")
# 67 TH line!!!!!!!!!!!!!!!!!!!!!!!

remaining_plunder = money_after_3_units - yondu_money_stolen - peter_money_stolen

print(f"THE GREAT DAY OF SPLITTING HAS ARRIVED AND TOTAL PLUDER IS {remaining_plunder} !!! TIME TO SPLIT EACH PERSON GETS:")

crew_share = round((remaining_plunder / total_crew) + 3, 2)
print(str(crew_share))

yondus_total_share = round(yondu_money_stolen + crew_share, 2)
print("Youndu got " + str(yondus_total_share))

peters_total_share = round(peter_money_stolen + crew_share, 2)
print("Peter got " + str(peters_total_share))

