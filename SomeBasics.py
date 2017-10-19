#Question2
"""
    Number of pupils: 176 | Number of 5 a side teams: 35 | Number of pupils left out: 1
    Number of pupils: 489 | Number of 5 a side teams: 97 | Number of pupils left out: 4
    Number of pupils:  77 | Number of 5 a side teams: 15 | Number of pupils left out: 2
"""
for i in range(0, 3):
    while True:
        try:
            number_of_pupils = int(input('Please enter the number of pupils participating'))
        except ValueError:
            print('That is not a valid number of pupils, please try again')
            continue
        else:
            break

    if number_of_pupils < 0:
        print('There cannot be negative number of pupils')
    else:
        teams = number_of_pupils // 5
        pupilsLeftOut = number_of_pupils % 5
        print('The number of 5 a side teams is ' + str(teams))
        print('The number of pupils left out is ' + str(pupilsLeftOut))

#Question7
name = input('Hello, who are you?')
print ('Hello, ' + name + '. It is good to meet you.')

