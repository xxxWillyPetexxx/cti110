is_leap_year = False
   
input_year = int(input())

def is_leap(year):
    if year%400 == 0: 
        return True
    
    elif year%4 == 0 and year%100 !=0:
        return True
    
    else:
        return False

if is_leap(input_year):
    print(input_year, '- leap year')
    
else:
    print(input_year, '- not a leap year')
   
