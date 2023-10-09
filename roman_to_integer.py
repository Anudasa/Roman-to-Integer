def roman_to_int(s):
    vocabulary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = list(s)
    new_num = []
    n = len(roman_num)
    num = 0

    for i in range(n):
        new_num.append(vocabulary[roman_num[i]])
    
    for i in range(n - 1):
        if new_num[i] < new_num[i+1]:
            new_num[i+1] = new_num[i+1] - new_num[i]
        else:
             num += new_num[i]
    num += new_num[-1]
    
    return num

while True:
    number = input('Введите римское число: ')
    print(roman_to_int(number))

    print("'Y' - To countinue \n'N' - To exit")
    decision = input()
    if decision.capitalize == 'Y':
        continue
    elif decision.capitalize == 'N':
        break
    else:
        break