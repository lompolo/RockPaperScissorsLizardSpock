class Player:
    def __init__(self, name):
        self._name = name
        self._wins = 0
        self._loses = 0

    def get_name(self):
        return self._name

    def get_score(self):
        return self._wins, self._loses

    def add_score(self, wins, loses):
        self._wins += wins
        self._loses += loses

    def reset_score(self):
        self._wins = 0
        self._loses = 0
