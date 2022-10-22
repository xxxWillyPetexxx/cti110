#This program calculates and dipslays travel expenses
#20221008
#CTI-110 P2HW1 - Travel 
#Joshua D. Wood
#
#
#Input
#Create input variables for starting travel budget, destination, and expenses.
#   expenses include expected gas cost, logging cost and food cost
#   converts inputs to either float or string.
#Program
#Starting with the initial budget, the program calculates the remaining budget after all
#   expenses have been subtracted. 
#   all expenses will be subtracted from the initial budget to produce the remaining balance
#Output
#Prints initial budget, destination and each expense inputed along with labels.
#   Prints remaing balance after program calculates how much money is left over after
#   all expenses have been subtracted

#Title of Program
print('This program calculates and displays travel expenses')
print()

#Creates input variables for program
Budget_Val = float(input('Enter Budget: '))
print()
Travel_Dest = input('Enter your travel destination: ')
print() 
Gas_Val = float(input('How much do you think you will spend on gas? '))
print()
Logging_Price = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
Food_Val = float(input('Last, how much do you need for food? '))
print()

#_____MAIN PROGRAM______

#Sets width value for alignment
width = 40

#Creates variable to add $ and decimal place for input values
Budget_Val_Ed = f'${Budget_Val:.1f}'
Gas_Val_Ed = f'${Gas_Val:.1f}'
Logging_Price_Ed = f'${Logging_Price:.1f}'
Food_Val_Ed = f'${Food_Val:.1f}'

#Print order and alignment code
print('Travel Expenses'.center(width,'-'))
print('Location:'.ljust(20),  Travel_Dest)
print('Initial Budget:'.ljust(20),  Budget_Val_Ed)
print('Fuel:'.ljust(20),  Gas_Val_Ed)
print('Accomodation:'.ljust(20),  Logging_Price_Ed)
print('Food:'.ljust(20),  Food_Val_Ed)
print(''.center(width,'-'))
print()

#Output variable for remaining travel expense balance after expenses
Remain_Bal = float(Budget_Val - Gas_Val - Logging_Price - Food_Val)
Remain_Bal_Ed = f'${Remain_Bal:.1f}'
print('Remaining Balance:'.ljust(20), Remain_Bal_Ed)
      
