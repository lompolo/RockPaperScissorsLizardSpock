choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock']


class UI:
    def __init__(self):
        self._start_text = 'Welcome to to Rock Paper Scissors Lizard Spock'
        self._rules = '''
        The rules of the game are:
        Scissors cuts paper
        Paper covers rock 
        Rock crushes lizard 
        Lizard poisons Spock 
        Spock smashes scissors
        Scissors decapitates lizard 
        Lizard eats paper
        Paper disproves Spock 
        Spock vaporizes rock, 
        and as it always has, rock crushes scissors.
        '''
        self._choices = [f'{c}[{n}]' for n, c in enumerate(choices)]

    def display_start(self):
        print(self._start_text)

    def show_rules(self):
        print(self._rules)

    def get_user_input(self, name):
        print(f'Player {name} turn')
        while True:
            user_input = input(f'Give choice {", ".join(self._choices)} or type r to get rules: ')
            if user_input == 'r' or user_input == 'R':
                self.show_rules()
            else:
                try:
                    user_input = int(user_input)
                except ValueError:
                    print('Check your choice')
                else:
                    return user_input

    def get_player_name(self, player_number):
        player = ''
        while not player:
            player = input(f'Give player {player_number + 1} name or give c if player is computer: ').strip()

            if player == 'c' or player == 'C':
                player = 'computer'
        return player
