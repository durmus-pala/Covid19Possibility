age = input("are you a cigarette addict older than 75 years old?(Yes or No) ")
chronic = input("Do you have a severe chronic disease?(Yes or No) ")
immune = input("Is your immune system too weak?(Yes or No) ")
if (age.lower() == "yes") or (chronic.lower() == "yes") or (immune.lower() == "yes"):
    print("You are in risky group")
else:
    print("You are not in risky group")