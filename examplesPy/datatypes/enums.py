from enum import Enum

# snippet: enums
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

if __name__ == '__main__':
    myColor: Color = Color.RED
    if myColor == Color.GREEN:
        print("RED is GREEN?")
    else:
        print("RED is not Green!")
# snippet: /enums