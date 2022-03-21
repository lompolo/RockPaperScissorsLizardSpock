from player import Player
from user_interface import UI, choices
from random import randint


def game_loop():
    ui = UI()
    ui.display_start()
    ui.show_rules()
    players = [Player(ui.get_player_name(0)), Player(ui.get_player_name(1))]
    player_choices = ['', '']

    while True:
        for i, player in enumerate(players):
            if player.get_name() != 'computer':
                player_choices[i] = ui.get_user_input(player.get_name())
            else:
                player_choices[i] = randint(0, len(choices))

        print(player_choices)


if __name__ == '__main__':
    game_loop()
