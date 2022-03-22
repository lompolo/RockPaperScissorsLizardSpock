choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock']

winning_choices = {
    choices[0]: [choices[2], choices[3]], # rock crushes scissor and lizard
    choices[1]: [choices[0], choices[4]], # paper covers rock and disproves Spock
    choices[2]: [choices[1], choices[3]], # scissors cuts paper and decapitates lizard
    choices[3]: [choices[1], choices[4]], # lizard eats paper and poisons Spock
    choices[4]: [choices[0], choices[2]] # Spock vaporizes rock and smashes scissors
}

rules = '''
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


def get_winner_index(users_choices):
    print(users_choices)
    if users_choices[0] == users_choices[1]:
        return -1
    if users_choices[1] in winning_choices[users_choices[0]]:
        return 0
    return 1