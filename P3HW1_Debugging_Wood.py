# CTI-110
# P3HW1_Debugging_Wood
# Joshua D. Wood
# 20221023


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 1: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grade_list = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low_grade = min(grade_list)
high_grade = max(grade_list)
sum_grades = sum(grade_list)
avg_grade = sum(grade_list) / len(grade_list)

print('Results'.center(30,'-'))
print('Lowest Grade:'.ljust(20), f'{low_grade:.1f}')
print('Highest Grade:'.ljust(20), f'{high_grade:.1f}')
print('Sum of Grades:'.ljust(20), f'{sum_grades:.2f}')
print('Average:'.ljust(20), f'{avg_grade:.2f}')
print(''.center(40,'-'))
# determine letter grade for average

if avg_grade >= 90:
    print('Your grade is: A')
elif avg_grade >= 80:
    print('Your grade is: B')
elif avg_grade >= 70:
    print('Your grade is: C')
elif avg_grade >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this





