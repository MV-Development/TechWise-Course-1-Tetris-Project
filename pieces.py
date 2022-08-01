import random
O = [['xxxxx'
      'xxxxx'
      'xooxx'
      'xooxx'
      'xxxxx']]

PIECE_NAMES = (O)
WHITE, BLACK, BLUE, RED, GREEN = (255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)
COLORS = [BLUE, RED, GREEN]

# test

class Piece():
    def __init__(self, x, y, tetro):

        self.x = x
        self.y = y

        self.tetro = tetro
        self.color = random.choice(COLORS)
        self.rotation = 0


# Orange Ricky
#   0
# 000
class OrangeRicky:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blocks = ((x + 2, y), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1))


# Blue Ricky
# 0
# 000
class BlueRicky:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blocks = ((x, y), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1))


# Cleveland Z
# 00
#  00
class CleavelandZ:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blocks = ((x, y), (x + 1, y), (x + 1, y + 1), (x + 2, y + 1))


# Rhode Island Z
#  00
# 00
class RhodeIslandZ:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blocks = ((x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 2, y))


# Hero
# 0000
class Her0:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blocks = ((x, y), (x + 1, y), (x + 2, y), (x + 3, y))


# Teewee
#  0
# 000
class Teewee:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blocks = ((x + 1, y), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1))


# Smashboy
# 00
# 00
class SmashBoy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blocks = ((x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1))
