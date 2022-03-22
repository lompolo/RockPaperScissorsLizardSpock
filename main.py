from player import Player
from user_interface import UI
from random import choice
from game_library import get_winner_index,choices


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
                player_choices[i] = choice(choices)

        winner_idx = get_winner_index(player_choices)
        ui.show_winner(winner_idx, player_choices)

        "TODO: update results"
        "TODO: Ask next round"
        "TODO: show statistics before quiting"


if __name__ == '__main__':
    game_loop()
