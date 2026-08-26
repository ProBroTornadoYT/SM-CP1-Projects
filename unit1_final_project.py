#unit1_final_project.py Shreenayan Mehta

name= input("What is your name: ").strip().title()

job= input("What is your job: ").strip()

address= input("What is your address: ").strip()

email= input("What is your email address: ").strip()

password= input("What is your password: ").strip()

print(f"Thank you, {name} Now, your personal details, like your job i.e., {job}. We also know that you live at {address}, and your email address is {email}, and its password is {password}. Now that you have given it to us, let us find some leaks of your information. \nProcessing… \nWe have found one leak on the dark web with these info- \n{name} \n{job} \n{address} \n{email} \n{password}")
