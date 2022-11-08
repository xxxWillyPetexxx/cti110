num_1 = int(input())
num_2 = int(input())

if num_2 >= num_1:
    for i in range(num_1, num_2+1, 5):
        print(i, end=' ')
    print()
else:
    print('Second integer can\'t be less than the first.')
