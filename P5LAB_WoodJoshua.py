days_in_feb = False

input_year = int(input())

def days_in_feb(user_year): 
    if user_year % 400 == 0: 
        return True
    
    elif user_year % 4 == 0 and user_year % 100 != 0:
        return True
    
    else:
        return False

if days_in_feb(input_year):
    print(input_year, 'has 29 days in February.')
    
else:
    print(input_year, 'has 28 days in February.')
