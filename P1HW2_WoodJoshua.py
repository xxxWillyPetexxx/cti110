#This program calculates and dipslays travel expenses
#20220925
#CTI-110 P1HW2 - Travel Expenses
#Joshua D. Wood
#

#brief discription of program for user
print('This program calculates and displays travel expenses')
print()

#Input starting Budget value
Budget_Val = int(input('Enter Budget:'))
print()

#Input Travel Destination
Travel_Dest = input('Enter your travel destination:')
print() 

#Input expected Gas value
Gas_Val = int(input('How much do you think you will spend on gas?'))
print()

#Input for approximate Logging price
Logging_Price = int(input('Approximately, how much will you need for accomodation/hotel?'))
print()

#Input for Food value
Food_Val = int(input('Last, how much do you need for food?'))
print()

#Output for Travel Expenses
print('------------Travel Expenses-----------')
print('Location:',  Travel_Dest)
print('Initial Budget:',  Budget_Val)
print()
print('Fuel:',  Gas_Val)
print('Accomodation:',  Logging_Price)
print('Food:',  Food_Val)
print()
Remain_Bal = int(Budget_Val - Gas_Val - Logging_Price - Food_Val)
print('Remaining Balance:', Remain_Bal)
      
