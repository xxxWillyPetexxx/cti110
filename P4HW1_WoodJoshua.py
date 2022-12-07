# CTI-110
# P4HW1 - Score List
# Joshua D. Wood
# 20221112
#
#creates score and scr_num variable. creates score list to be used in program
#program creates loop to allow user to input scores depending on how many they requested0
#output is lowest, average and letter grade along with modified score list with the lowest grade removed
#


scores = 0
scr_num = 1
score_list = []
scores = int(input('How many scores do you want to enter? '))


for i in range(scores):
    num_score = int(input(f"Enter score {scr_num}#: "))

    if num_score < 0 or num_score > 100:
        print('INVALID Score entered!!!!')
        print('Score shoud be between 0 and 100')
        num_score = int(input(f"Enter score {scr_num}# again: "))
        scr_num += 1
        
    else:
        score = 0
        scr_num += 1
        score_list.append(num_score)


low_score = min(score_list)
score_list.remove(low_score)
avg_score = sum(score_list)/len(score_list)

if avg_score >= 90:
    ltr_grade = 'A'
elif avg_score >= 80:
    ltr_grade = 'B'
elif avg_score >= 70:
    ltr_grade = 'C'
elif avg_score >= 60:
    ltr_grade = 'D'
else:
    ltr_grade = 'F'

print('Results'.center(30, '-'))
print('Lowest Score'.ljust(20), ':'.center(10), f'{low_score:.1f}')
print('Modified Score List'.ljust(20), ':'.center(10), str(score_list))
print('Scores Average'.ljust(20), ':'.center(10), f'{avg_score:.2f}')
print('Grade:'.ljust(20), ':'.center(10), ltr_grade)
print(''.center(40, '-'))

