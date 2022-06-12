def monthlyPayment(balance,annualInterestRate):
    
    MonthlyInterest = annualInterestRate/12
    high = (balance * (1 + MonthlyInterest)**12)/12.0
    low = balance/12
    minPayment = (high + low)/2
    total = balance
    epsilon = 0.005
    while total  < -epsilon or total > epsilon:
        total = balance
        for i in range(12):
            total = total - minPayment
            total = total * (1 + (annualInterestRate/12))
        if total < -epsilon:
            high = minPayment
        else:  
            low = minPayment
        minPayment = (high + low)/2
        print(total)
            
        
    print('Lowest Payment: ' + str(round(minPayment,2)))

print(monthlyPayment(999999,0.18))