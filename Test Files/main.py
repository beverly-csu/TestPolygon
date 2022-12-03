import json

data = {
    'Заметка №1': {
        'text': 'Это содержимое заметки',
        'tags': ['первая заметка', 'новое приложение']
    }
}


data[input('Название: ')] = {'text': input('Содержимое: '), 'tags': []}

with open('notes.json', 'w') as file:
    json.dump(data, file)