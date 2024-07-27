# Prompt user to enter a number
num = int(input("Please enter a number: "))
sum_num = 0  # Sum at beginning 
guesses = 0  # First guess

# Loop until number entered by user is equal to -1
while num != -1:
    # Prompt user for a number 
    num = (float(input("Please enter a number: ")))
    sum_num += num  # Add number entered to initial sum
    guesses += 1  # Guesses go up by 1 each time a number is entered

# Once the number entered is equal to -1, calculate average  
if num == -1:
    average = (sum_num) / guesses
    print(f"The average is {average}.")
