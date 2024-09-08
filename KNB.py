import random
player = input('выберете к н б: ')
list = ['к', 'н', 'б']
comp = random.choice(list)
print(comp)
if player == 'к' and comp == 'к' or player == 'б' and comp == 'б' or player == 'н' and comp == 'н':
    print('ничья')
elif player == 'б' and comp == 'к' or player == 'к' and comp == 'н' or player == 'н' and comp == 'б':
    print('вы победили')
elif comp == 'б' and player == 'к' or comp == 'к' and player == 'н' or comp == 'н' and player == 'б':
    print('победил компьютер')
else:
    print('вы ввели неверную букву')
