# Second class
from color import Color

class Pawn:

    def __init__(self, color: Color):

        self.color = color


    def __str__(self):

        return f"{self.color}"

    def __rich__(self) -> str:

        return self.color.__rich__()

#pawn1 = Pawn(Color.BLACK)
#pawn2 = Pawn(Color.WHITE)

#print(pawn1)
#print(pawn2)
