main_list = input('Introduce the main list of numbers: ')
main_list = main_list.split()

a_list = input('Type in A set: ')
a_list = a_list.split()

b_list = input('Type in B set: ')
b_list = b_list.split()

happiness = 0

for item in main_list:
    if item in a_list:
        happiness += 1
    elif item in b_list:
        happiness -= 1

print('Your happiness is: ', happiness)
