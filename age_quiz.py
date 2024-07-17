# Create variable age and assign integer value 
# Request user age and store it as integer

age = int()
age = int(input("How old are you?: "))
if age < 13:
  print("You qualify for the kiddie discount.")
elif age == 13 or age < 21:
  print("Age is but a number.")
elif age == 21:
  print("Congrats on your 21st!")
elif age <= 39:
    print("Age is but a number.")
elif age == 40 or age < 65:
    print("You're over the hill.")
elif age == 65 or age <= 100:
    print("Enjoy your retirement!")
else:
    print("Sorry, you're dead.")
