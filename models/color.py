from enum import Enum

# The first class: Color

class Color(Enum):

    BLACK = "BLACK"

    WHITE = "WHITE"

    def opposite(self) -> "Color":

        if self == Color.BLACK:

            return Color.WHITE

        else:

            return Color.BLACK

    def __str__(self) -> str:

        if self == Color.BLACK:

            return "⚫️" 

        else:

            return "⚪️"


    def __rich__(self) -> str:

        if self == Color.BLACK:

            return "[black]⬤ [/black]"

        else:

            return "[white]⬤ [/white]"
