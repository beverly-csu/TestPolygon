with open('quotes.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)

author = input('Введите автора отрывка: ')
with open('quotes.txt', 'a', encoding='utf-8') as file:
    file.write('(' + author + ')\n')

menu = input('Желаете ли вы добавить новые отрывки? (нет - остановить): ')
while menu != 'нет':
    quote = input('Введите цитату: ')
    author = input('Введите автора данной цитаты: ')
    author = '(' + author + ')'
    text = quote + '\n' + author + '\n'
    with open('quotes.txt', 'a', encoding='utf-8') as file:
        file.write(text)
    menu = input('Желаете ли вы добавить новые отрывки? (нет - остановить): ')

print('Список всех авторов:')
i = 1
with open('quotes.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        if line[0] == '(' and line[len(line) - 2] == ')':
            print(str(i) + ') ' + line[1:len(line) - 2])
            i += 1