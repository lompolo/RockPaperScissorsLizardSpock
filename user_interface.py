from game_library import choices, rules


def _user_input():
    return input().strip()


class UI:
    def __init__(self):
        self._start_text = 'Welcome to to Rock Paper Scissors Lizard Spock'
        self._rules = rules
        self._choices = [f'{c}[{n}]' for n, c in enumerate(choices)]
        self._player_0_name = ''
        self._player_1_name = ''

    def display_start(self):
        print(self._start_text)

    def show_rules(self):
        print(self._rules)

    def get_user_input(self, name):
        print(f"Player {name}'s turn")
        while True:
            print(f'Give choice {", ".join(self._choices)} or type r to get rules:')
            user_input = _user_input()
            if user_input == 'r' or user_input == 'R':
                self.show_rules()
            else:
                try:
                    user_input = int(user_input)
                except ValueError:
                    print('Check your choice')
                else:
                    return choices[user_input]

    def get_player_name(self, player_number):
        player = ''
        while not player:
            player = input(f'Give player {player_number + 1} name or give c if player is computer: ').strip()

            if player == 'c' or player == 'C':
                player = 'computer'

        if player_number == 0:
            self._player_0_name = player
        else:
            self._player_1_name = player
        return player

    def show_winner(self, winner, player_choices):
        print(f'Player {self._player_0_name} has {player_choices[0]}')
        print(f'Player {self._player_1_name} has {player_choices[1]}')
        if winner == -1:
            print('It is tie')
        elif winner == 0:
            print(f'Winner is {self._player_0_name}')
        else:
            print(f'Winner is {self._player_1_name}')

    def is_game_on(self):
        while True:
            print('Do you want to continue ([y]/n?')
            user_input = _user_input()
            if user_input == 'n' or user_input == 'N':
                return False
            return True

    def show_statistics(self, player_name, player_stats):
        print(f'{player_name} has {player_stats[0]} wins and {player_stats[1]} losses')