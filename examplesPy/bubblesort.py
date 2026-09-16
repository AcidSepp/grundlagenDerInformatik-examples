from typing import List

def bubblesort(it: List[int]) -> List[int]:
    while not is_sorted(it):
        for i, e in enumerate(it):
            if i+1 < len(it):
                current: int = it[i]
                successor: int = it[i + 1]
                if current > successor:
                    it[i+1] = current
                    it[i] = successor
            print(it)
    return it

def is_sorted(it: List[int]) -> bool:
    for i, e in enumerate(it):
        if i+1 < len(it):
            if it[i] > it[i+1]:
                return False
    return True

if __name__ == '__main__':
    my_list = [3,5,1,2,4]
    bubblesort(my_list)
