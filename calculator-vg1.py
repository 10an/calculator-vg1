from matplotlib import pyplot as plt

def sum(num1, num2):
    result= num1 + num2
    return result

deduction                = []
interest                 = []
termAmount               = []

print("Serielån kalkulator! Sånn cirka...")

""" kjøpesum                 = int(input("Sett inn beløp:\n"))
equity                   = int(input("Sett inn egenkapital:\n")) """
repaymentPeriod          = int(input("Sett inn nedbetalingstid:\n"))
loanAmount               = int(input("Sett inn ønsket beløp:\n"))
nominalInterestRate      = float(input("Sett inn nominell rente:\n")) / 100

remainingLoan            = loanAmount
annualDeduction          = loanAmount / repaymentPeriod

#Utregning
for year in range(repaymentPeriod):
    annualInterestRate = remainingLoan * nominalInterestRate
    remainingLoan -= annualDeduction
    deduction.append(annualDeduction)
    interest.append(annualInterestRate)

#Summering
total = 0
for entry in range(repaymentPeriod):
    result = sum(deduction[entry], interest[entry])
    total += int(result)
    termAmount.append(int(result))

#Visning
yr = 0
for amount in termAmount:
    yr += 1
    print("År " + str(yr) + " " + str(amount) + "kr")
print("Totalen er " + str(total) + "kr")

