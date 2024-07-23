# Create int variable swimming time
# and input "Please enter swimming time in minutes: "

# Create int variable cycling time
# and input "Please enter cycling time in minutes: "

# Create int variable running time 
# and input "Please enter running time in minutes: "

# Create variable total time to store sum of
# swimming time + cycling time + running time
# output total time taken to complete triathlon in minutes

# if total time is between 0 and 100 min
#   output "Provincial Colours"
# elif toatl time is between 101 and 105 min
#   output "Provincial Half Colours"
# elif total time is between 106 and 110
#   output "Provincial Scroll"
# else:
#   output "No award"

swimming_time = int(input("Please enter swimming time in minutes: "))
cycling_time = int(input("Please enter cycling time in minutes: "))
running_time = int(input("please enter running time in minutes: "))

total_time = swimming_time + cycling_time + running_time
print(f"Your total time taken to complete the triathlon is {total_time} minutes.")


if total_time >= 0 and total_time <= 100:
    print("Provincial Colours")
elif total_time >= 101 and total_time <= 105:
    print("Provincial Half Colours")
elif total_time >= 106 and total_time <= 110:
    print("Provincial Scroll")
else:
    print("No award")