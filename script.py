import random

colors = ['red', 'green', 'blue', 'yellow', 'purple']

with open('background.css', 'w') as file:
    file.write(f'body {{ background-color: {colors[random.randint(0, 4)]}; }}')
