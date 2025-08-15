from enum import Enum

class GameStatus(Enum):

    IN_PROGRESS = "IN_PROGRESS"

    FINISHED = "FINISHED"

    PAUSED = "PAUSED"

status = GameStatus.IN_PROGRESS

print(status)
print(status.value)
