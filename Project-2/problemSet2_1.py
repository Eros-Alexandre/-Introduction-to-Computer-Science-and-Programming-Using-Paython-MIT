'''Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required by the credit card company each month.
For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy - so print'''


def debtCalculation(balance,annualInterestRate,monthlyPaymentRate):
        payment = balance - balance * monthlyPaymentRate
    
        for i in range(12):
            balance = payment + annualInterestRate/12.0 * payment
            payment = balance - balance * monthlyPaymentRate
        return print('Remaining balance: ' + str(round(balance,2)))

        

        




print(debtCalculation(42,0.2,0.04))
    

