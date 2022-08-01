O = [['xxxxx'
      'xxxxx'
      'xooxx'
      'xooxx'
      'xxxxx']]

piece_names = (O)


class Piece:
    def __init__(self, x, y, tetro):
        self.x = x
        self.y = y
        self.tetro = tetro
        self.color = random.choice(COLORS)
        self.rotation = 0


# Orange Ricky
#   0
# 000


# Blue Ricky
# 0
# 000


# Cleveland Z
# 00
#  00


# Rhode Island Z
#  00
# 00


# Hero
# 0000


# Teewee
#  0
# 000


# Smashboy
# 00
# 00
