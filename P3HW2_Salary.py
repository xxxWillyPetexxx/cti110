#CIT-110
#P3HW2-Salary
#Joshua D. Wood
#20221027
#

#Input
#   input for employee name, hours worked and payrate. Also adds labels for description for what the
#   employee should input at each option
#Program
#   OT pay rate calculation. OT pay rate is equal to time and half so hourly pay rate divided by 2 and
#   then added to hourly pay rate to get time and a half. if else statement to calculate OT hours worked. OT
#   hours are calculated by if total hours worked are greater than 40, OT hours are equal to total hours subtracted
#   by 40. Else, OT hours are equal to 0. expression for OT pay, reg pay and total gross pay.
#Output
#   print output for employee names and labels for hrs worked, pay rate, total OT hours, OT pay, Total Reg hr pay
#   and total gross pay. 

#input variables for employee information
empl_name = input('Enter employee\'s name:  ')
hrs_worked = float(input('Enter number of hours worked:  '))
pay_rate = float(input('Enter employee\'s pay rate:  '))


ot_pay_rate = (pay_rate / 2) + pay_rate #overtime pay rate

#overtime hours worked
if hrs_worked > 40:
    ot_hrs = hrs_worked - 40
else:
    ot_hrs = 0

ot_pay = ot_hrs * ot_pay_rate #overtime seperate pay
reg_pay = pay_rate * hrs_worked #Regular Hour Pay
grs_pay = ot_pay + reg_pay #Gross Pay

print('-------------------------------------')
print('Employee name:',  empl_name)
print()
print(f"{'Hours Worked' : <15}{'Pay Rate' :<12}{'OverTime' :<12}{'OverTime Pay' :<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print('------------------------------------------------------------------------------------------')
print(f'{hrs_worked:<15.2f}{pay_rate:<12.2f}{ot_hrs:<12.1f}{ot_pay:<15.2f}${reg_pay:<14.2f}${grs_pay:<15.2f}')

