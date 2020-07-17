# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, direction, n_to, s_to, e_to, w_to):
        self.direction = direction
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def player_direction(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 'e':
            return self.e_to
        elif direction == 's':
            return self.s_to
        elif direction == 'w':
            return self.w_to
        else:
            return None
