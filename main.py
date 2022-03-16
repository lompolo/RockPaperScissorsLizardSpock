from player import Player
from user_interface import UI


def game_loop():
    ui = UI()
    ui.display_start()
    ui.show_rules()
    while True:
        print(ui.get_user_input())


if __name__ == '__main__':
    game_loop()
