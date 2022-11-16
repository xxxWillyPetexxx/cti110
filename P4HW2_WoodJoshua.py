# CTI-110
# P4HW2 - Salary Calculator
# Joshua D. Wood
# 20221115
#
##Input
#    creates while loop to run employee name input and based off of response,
#   either keeps cycling through loop or with "None", ends program with summary of inputs
#Program
#   While statement to initiate loop. sets employee name variable. Starts IF statement for emp_name entry.
#   OT pay rate calculation. OT pay rate is equal to time and half so hourly pay rate divided by 2 and
#   then added to hourly pay rate to get time and a half. if else statement to calculate OT hours worked. OT
#   hours are calculated by if total hours worked are greater than 40, OT hours are equal to total hours subtracted
#   by 40. Else, OT hours are equal to 0. expression for OT pay, reg pay and total gross pay.
#Output
#   print output for employee names and labels for hrs worked, pay rate, total OT hours, OT pay, Total Reg hr pay
#   and total gross pay. 
#   if employee enters "None", print output of total employees entered, total OT pay from entries, total Reg pay from entries,
#   and total GRS pay entries.

empl_name = 0
total = 0
ot_list = []
reg_list = []
grs_list = []

while empl_name != '':
    empl_name = input('Enter employee\'s name or "None" to terminate:  ')
    if empl_name == 'None':
        print()
        print(f"Total number of employee\'s entered: {total}")
        print(f"Total amount payed for overtime: ${sum(ot_list):.2f}")
        print(f"Total amount payed for regular hours: ${sum(reg_list):.2f}")
        print(f"Total amount payed for gross: ${sum(grs_list):.2f}")
        print()
        break
        
    
    else:
        hrs_worked = float(input(f"How many hours did {empl_name} work?  "))
        pay_rate = float(input(f"What is {empl_name} pay rate? "))
        total += 1
        if hrs_worked > 40:
            ot_hrs = hrs_worked - 40
        else:
            ot_hrs = 0
        reg_hrs = hrs_worked - ot_hrs #reg hours worked
        ot_pay_rate = 1.5 * pay_rate #overtime pay rate
        ot_pay = ot_hrs * ot_pay_rate #overtime seperate pay
        reg_pay = pay_rate * reg_hrs #Regular Hour Pay total
        grs_pay = ot_pay + reg_pay #gross pay total
        ot_list.append(ot_pay)
        reg_list.append(reg_pay)
        grs_list.append(grs_pay)
        print()
        print('Employee name:',  empl_name)
        print()
        print(f"{'Hours Worked' : <15}{'Pay Rate' :<12}{'OverTime' :<12}{'OverTime Pay' :<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
        print('------------------------------------------------------------------------------------------')
        print(f'{hrs_worked:<15.2f}{pay_rate:<12.2f}{ot_hrs:<12.1f}{ot_pay:<15.2f}${reg_pay:<14.2f}${grs_pay:<15.2f}')
        print()


        



