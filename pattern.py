# Create the below star pattern using one block of code:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

stars = "*"

for i in range(1, 9):
    if (i <= 4):
        print(i * "*")
        stars = stars + "*"
    else:
        print(stars) 
        stars = stars [ : -1]            
print("*")