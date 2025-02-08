import random
import time

walls = []
with open('walls.txt', 'r') as file:
    walls = file.read().splitlines()

with open('background.css', 'w') as file:
    file.write('/* Generated at ' + time.strftime('%Y-%m-%d %H:%M:%S') + ' */\n')
    file.write(':root {\n')
    file.write('--background-image: url("' + random.choice(walls) + '");\n')
    file.write('}\n')
