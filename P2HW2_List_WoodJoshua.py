# CTI-110
# P2HW2 - List
# Joshua D. Wood
# 20221012
#
#
#Creates inputs variables for six grades.
#   Input converted to floats to allow decimal places.
#Program creates grade list from inputs.
#   Grade list is then used to find the min grade, max grade,
#   sum of grades and average grade.
#Output prints min, max, sum of and average grade.
#   Each output recieves a description stating its purpose such 
#   as 'Lowest Grade', 'Highest Grade' etc...
#

#Program Inputes: Grades
grade_mod1 = float(input('Enter grade for Module 1: '))
grade_mod2 = float(input('Enter grade for Module 2: '))
grade_mod3 = float(input('Enter grade for Module 3: '))
grade_mod4 = float(input('Enter grade for Module 4: '))
grade_mod5 = float(input('Enter grade for Module 5: '))
grade_mod6 = float(input('Enter grade for Module 6: '))

#Create grade list and formula to calculate min, max, sum and average
grade_list = [grade_mod1, grade_mod2, grade_mod3, grade_mod4, grade_mod5, grade_mod6]
low_grade = min(grade_list)
high_grade = max(grade_list)
sum_grades = sum(grade_list)
avg_grade = sum(grade_list) / 6

#Output w/descriptions for min, max, sum and average.
print('Results'.center(30,'-'))
print('Lowest Grade:'.ljust(20), f'{low_grade:.1f}')
print('Highest Grade:'.ljust(20), f'{high_grade:.1f}')
print('Sum of Grades:'.ljust(20), f'{sum_grades:.2f}')
print('Average:'.ljust(20), f'{avg_grade:.2f}')
print(''.center(40,'-'))
