import os

with open('test.jpg', 'rb') as file:
    img = file.read()

with open('new.jpg', 'wb') as file:
    file.write(img)

os.remove('test.jpg')