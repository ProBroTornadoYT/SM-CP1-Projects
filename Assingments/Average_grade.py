#average grade Shreenayan mehta

print("Hello user! Today we will calculate your grades average just put your grades in the feilds below!") #asking for grades

grade1 = float(input("Grade1:"))
grade2 = float(input("Grade2:"))
grade3 = float(input("Grade3:"))
grade4 = float(input("Grade4:"))
grade5 = float(input("Grade5:"))
grade6 = float(input("Grade6:"))
grade7 = float(input("Grade7:"))

print("\n") #<- for a little white space in program
print("\n") #<- for a little white space in program
print("\n") #<- for a little white space in program

print("calculating Avg. grade")

total_grade=grade7+grade6+grade5+grade4+grade3+grade2+grade1

print(round((total_grade)/7,2))
