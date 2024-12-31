import random
blueprint = '---------'

def blueprint_to_image(blueprint):
    characters = []
    for x in blueprint:
        characters.append(x)
    for i in range(len(characters)):
        if characters[i] == '-':
            characters[i] = ' '
    return f'''
_{characters[0]}_|_{characters[1]}_|_{characters[2]}_
_{characters[3]}_|_{characters[4]}_|_{characters[5]}_
 {characters[6]} | {characters[7]} | {characters[8]}
 ''' 

def opponent_move(blueprint):
    opponent_occupation = random.randint(0,8)
    characters = []
    for x in blueprint:
        characters.append(x)
    for i in range(len(characters)):
        if characters[i] == '-':
            characters[i] = ' '
    while characters[opponent_occupation] != ' ':
        opponent_occupation = random.randint(0,8)
    else:
        characters[opponent_occupation] = opponent_shape
    print(f'''
_{characters[0]}_|_{characters[1]}_|_{characters[2]}_
_{characters[3]}_|_{characters[4]}_|_{characters[5]}_
 {characters[6]} | {characters[7]} | {characters[8]}
''')
    for i in range(len(characters)):
        if characters[i] == ' ':
            characters[i] = '-'
    return ''.join(characters)

class Tictactoe:
    def __init__(self, user_shape):
        self.user_shape = user_shape
    def lt(self, blueprint):
        print(blueprint_to_image(blueprint))
    def lm(self, blueprint):
        print(blueprint_to_image(blueprint))
    def lb(self, blueprint):
        print(blueprint_to_image(blueprint))
    def mt(self, blueprint):
        print(blueprint_to_image(blueprint))
    def mm(self, blueprint):
        print(blueprint_to_image(blueprint))
    def mb(self, blueprint):
        print(blueprint_to_image(blueprint))
    def rt(self, blueprint):
        print(blueprint_to_image(blueprint))
    def rm(self, blueprint):
        print(blueprint_to_image(blueprint))
    def rb(self, blueprint):
        print(blueprint_to_image(blueprint))
    def going_second(self, blueprint):
        print(opponent_move(blueprint))



print('\nWelcome to the Python Terminal Game of TicTacToe!\n')
enter_prompt = input('Input "c" to continue: ')
while enter_prompt != 'c':
    enter_prompt = input('Input "c" to continue: ')

print('''\nThe rules are simple. With your shape (x or o), get three in a row diagonallly, vertically, or horizontally to win. 
To input the location on the board that you would like to occupy, please reference the key below. Enjoy!''')

print('''
Key:
lt = left top
lm = left middle
lb = left bottom
mt = middle top
mm = middle middle 
mb = middle bottom
rt = right top
rm = right middle
rb = right back \n
''')

enter_prompt = input('Input "b" to begin: ')
while enter_prompt != 'b':
    enter_prompt = input('Input "b" to begin: ')

print()
for i in range(2):
    print('_ _|_ _|_ _')
print('   |   |   \n')

user_shape = input('Input "x" to start first or "o" to go second: ')
while user_shape != 'x' and user_shape != 'o':
    user_shape = input('Input "x" to start first or "o" to go second: ')
else:
    round1 = Tictactoe(user_shape)

if user_shape == 'x':
    opponent_shape = 'o'
else:
    opponent_shape = 'x'

if user_shape == 'o':
    blueprint = opponent_move(blueprint)

while blueprint[:3] != 'xxx' and blueprint[:3] != 'ooo' and blueprint[3:6] != 'xxx' and blueprint[3:6] != 'ooo' and blueprint[6:] != 'xxx' and blueprint[6:] != 'ooo' and blueprint[0:9:3] != 'xxx' and blueprint[0:9:3] != 'ooo' and blueprint[1:9:3] != 'xxx' and blueprint[1:9:3] != 'ooo' and blueprint[2:9:3] != 'xxx' and blueprint[2:9:3] != 'ooo' and blueprint[0:9:4] != 'xxx' and blueprint[0:9:4] != 'ooo' and blueprint[2:8:2] != 'xxx' and blueprint[2:8:2] != 'ooo' and '-' in blueprint:
    location_input = input('Location to occupy: ')
    while location_input != 'lt' and location_input != 'mt' and location_input != 'rt' and location_input != 'lm' and location_input != 'mm' and location_input != 'rm' and location_input != 'lb' and location_input != 'mb' and location_input != 'rb':
        location_input = input('Location to occupy: ')
    else: 
        if location_input == 'lt' and blueprint[0] != 'x' and blueprint[0] != 'o':
            if blueprint.count('-') == 1:
                blueprint = user_shape + blueprint[1:]
                round1.lt(blueprint)
            else: 
                blueprint = user_shape + blueprint[1:]
                round1.lt(blueprint)
                blueprint = opponent_move(blueprint)
        elif location_input == 'mt' and blueprint[1] != 'x' and blueprint[2] != 'o':
            if blueprint.count('-') == 1:
                blueprint = blueprint[:1] + user_shape + blueprint[2:]
                round1.mt(blueprint)
            else:
                blueprint = blueprint[:1] + user_shape + blueprint[2:]
                round1.mt(blueprint)
                blueprint = opponent_move(blueprint)
        elif location_input == 'rt' and blueprint[2] != 'x' and blueprint[2] != 'o':
            if blueprint.count('-') == 1:
                blueprint = blueprint[:2] + user_shape + blueprint[3:]
                round1.rt(blueprint)
            else:
                blueprint = blueprint[:2] + user_shape + blueprint[3:]
                round1.rt(blueprint)
                blueprint = opponent_move(blueprint)
        elif location_input == 'lm' and blueprint[3] != 'x' and blueprint[3] != 'o':
            if blueprint.count('-') == 1:
                blueprint = blueprint[:3] + user_shape + blueprint[4:]
                round1.lm(blueprint)
            else:
                blueprint = blueprint[:3] + user_shape + blueprint[4:]
                round1.lm(blueprint)
                blueprint = opponent_move(blueprint)
        elif location_input == 'mm' and blueprint[4] != 'x' and blueprint[4] != 'o':
            if blueprint.count('-') == 1:
                blueprint = blueprint[:4] + user_shape + blueprint[5:]
                round1.mm(blueprint)
            else:
                blueprint = blueprint[:4] + user_shape + blueprint[5:]
                round1.mm(blueprint)
                blueprint = opponent_move(blueprint)
        elif location_input == 'rm' and blueprint[5] != 'x' and blueprint[5] != 'o':
            if blueprint.count('-') == 1:
                blueprint = blueprint[:5] + user_shape + blueprint[6:]
                round1.rm(blueprint)            
            else:
                blueprint = blueprint[:5] + user_shape + blueprint[6:]
                round1.rm(blueprint)
                blueprint = opponent_move(blueprint)
        elif location_input == 'lb' and blueprint[6] != 'x' and blueprint[6] != 'o':
            if blueprint.count('-') == 1:
                blueprint = blueprint[:6] + user_shape + blueprint[7:]
                round1.lb(blueprint)            
            else:
                blueprint = blueprint[:6] + user_shape + blueprint[7:]
                round1.lb(blueprint)
                blueprint = opponent_move(blueprint)
        elif location_input == 'mb' and blueprint[7] != 'x' and blueprint[7] != 'o':
            if blueprint.count('-') == 1:
                blueprint = blueprint[:7] + user_shape + blueprint[8:]
                round1.mb(blueprint)            
            else:
                blueprint = blueprint[:7] + user_shape + blueprint[8:]
                round1.mb(blueprint)
                blueprint = opponent_move(blueprint)
        elif location_input == 'rb' and blueprint[8] != 'x' and blueprint[8] != 'o':
            if blueprint.count('-') == 1:
                blueprint = blueprint[:8] + user_shape + blueprint[9:]
                round1.rb(blueprint)
            else:
                blueprint = blueprint[:8] + user_shape + blueprint[9:]
                round1.rb(blueprint)
                blueprint = opponent_move(blueprint)
        else:
                print('Location already occupied. Try again.')
                continue      
else:
    if blueprint[:3] == 'xxx' or blueprint[3:6] == 'xxx' or blueprint[6:] == 'xxx' or blueprint[0:9:3] == 'xxx' or blueprint[1:9:3] == 'xxx' or blueprint[2:9:3] == 'xxx' or blueprint[0:9:4] == 'xxx' or blueprint[2:8:2] == 'xxx':
        if user_shape == 'x':
            print('You won!\n')
        else:
            print("You lost.\n")
    elif blueprint[:3] == 'ooo' or blueprint[3:6] == 'ooo' or blueprint[6:] == 'ooo' or blueprint[0:9:3] == 'ooo' or blueprint[1:9:3] == 'ooo' or blueprint[2:9:3] == 'ooo' or blueprint[0:9:4] == 'ooo' or blueprint[2:8:2] == 'ooo':
        if user_shape == 'o':
            print('You won!\n')
        else:
            print("You lost.\n") 
    else:
        print('It\'s a tie!\n')
