#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    #Loan calculator, ready for marking!

    # when user inputs x dollars, calculate interest rate and give weekly payment.
    # should have prompts for dollars, interest, and years
    # user inputs dollar amount
    # user inputs interest rate
    # user inputs number of years
    
    #input prompts for loan amount, interest rate, and number of years
    print("Hello! This program is made to calculate weekly loan payments.")
    print("")
    loan=input("Please input the loan amount in dollars.")
    loanAmount=float(loan)
    print("")
    interest=input("Please enter the interest rate. (%)")
    interestRate=float(interest)
    print("")
    years=input("Please enter the amount of years the loan is for.")
    numberYears=float(years)
    print("")

    #tells how much to pay in interest
    interestAmount=interestRate / 5200
    #calculates weekly payment
    weeklyPayment= interestAmount / (1 - ((1 + interestAmount) ** (-52 * numberYears))) * loanAmount
    #rounds weekly payment
    roundedWeeklyPayment=round(weeklyPayment,2)

    print("")
    print("You will have to pay",roundedWeeklyPayment,"per week.")


    # YOUR CODE ENDS HERE

main()