#напиши здесь свою программу
import pickle


class Pupil:
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

best_pupils = []
summ = 0
amount = 0
    
with open('pupils_large.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(' ')
        pupil = Pupil(data[0], data[1], int(data[2]))
        if pupil.mark == 5:
            best_pupils.append(pupil)
        amount += 1
        summ += pupil.mark
        # print(pupil.surname, pupil.name, '-', pupil.mark)

print('\n\nОтличники:')
for pupil in best_pupils:
    print(pupil.surname)

print('\n\nСредняя оценка класса:', summ / amount)