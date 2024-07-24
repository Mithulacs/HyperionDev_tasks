import math

while True:
        calculation = input("investment - to calculate the amount of interest you'll earn on your investment \n"
                        "bond       - to calculate the amount you'll have to pay a home loan \n"

                        "Enter either 'investment' or 'bond' fom the menu above to proceed: ")

        calculation = calculation.lower()
        # print(calculation)
      
        if calculation == "investment":
                deposit = int(input("Please enter the amount you want to deposit: £ "))
                interest_entered = int(input("Please enter interest rate, omtting the '%' sign: "))
                years_entered = int(input("Please enter number of years you plan on investing: "))

                bool_2 = True
                while (bool_2 == True):
                        interest = input("Enter 'simple'(for simple interest) or 'compound'(for compound interest): ")
                        interest = interest.lower()
                        # print(interest)
        
                        if interest == "simple":
                                simple_interest = deposit * (1 + interest_entered / 100 * years_entered) 
                                print(f"Your simple interest is £ {round(simple_interest, 2)}.")
                                bool_2 = False
                        
                        elif interest == "compound":
                                compound_interest = deposit * math.pow((1 + interest_entered /100), years_entered)
                                print(f"Your compound interest is £ {round(compound_interest, 2)}.")
                                bool_2 = False
                        else:
                                print("\nThe word you entered has not been recognised. Please read carefully the paragraph below and enter your choice.\n")  
                if (bool_2 == False):        
                        break

        elif calculation == "bond":
                house_value = int(input("Please enter your present house value: £ "))
                interest_rate = int(input("Please enter your interest rate, omitting the '%' sign: "))
                months = int(input("Please enter the number of months you plan to take to repay the bond: "))
                repayment = float((interest_rate /100)/12 * house_value) / (1 - (1 + (interest_rate /100)/12)**(- months))
                # print(repayment)
                print(f"You will have to repay £ {round(repayment,2)} each month.")
                break

        else: 
                print("\nThe word you entered has not been recognised. Please read carefully the paragraph below and enter your choice.\n")
        

    

