# snippet: hanoi
def hanoi(n: int, quelle: str, senke: str, speicher: str):
    if (n == 1):
        print("Move from " + quelle + " to " + senke)
    else:
        hanoi(n - 1, quelle, speicher, senke)
        print("Move from " + quelle + " to " + senke)
        hanoi(n - 1, speicher, senke, quelle)


# snippet: /hanoi

if __name__ == '__main__':
    hanoi(3, "A", "C", "B")