def monthlyPayment(balance,annualInterestRate):
    minPayment = 0
    total = balance
    epsilon = 0.01

    while total >= epsilon:
        minPayment += 10
        total = balance
        for i in range(12):
            total = total - minPayment
            total = total * (1 + (annualInterestRate/12))
        print(total)
            
        
    print('Lowest Payment: ' + str(minPayment))

print(parcelaMensal(3329,0.2))