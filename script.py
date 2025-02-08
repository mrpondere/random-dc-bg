import random

walls = []
with open('walls.txt', 'r') as file:
    walls = file.read().splitlines()

with open('background.css', 'w') as file:
    file.write(':root {\n')
    file.write('--background-image: url("' + random.choice(walls) + '");\n')
    file.write('}\n')
