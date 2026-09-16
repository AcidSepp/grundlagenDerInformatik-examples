from __future__ import annotations
import typing


# snippet: list
class IntList:
    def __init__(self, element: typing.Optional[int], rest: typing.Optional[IntList]):
        self.first = element
        self.rest = rest

    # snippet: /list
    def __str__(self):
        result: str = "["
        current: IntList = self
        while current is not None and current.first is not None:
            result = result + str(current.first) + ","
            current = current.rest
        return result + "]"

    # snippet: empty
    def is_empty(self) -> bool:
        return self.first is None

    # snippet: /empty

    # snippet: last
    def last(self: IntList) -> int:
        if self.rest is None:
            return self.first
        else:
            return self.rest.last()

    # snippet: /last

    # snippet: end
    def end(self: IntList) -> IntList:
        if self.is_empty():
            return self
        current: IntList = self
        while not current.rest.is_empty():
            current = current.rest
        return current

    # snippet: /end

    # snippet: length
    def length(self: IntList) -> int:
        if self.first is None:
            return 0
        if self.rest is None:
            return 1
        return 1 + self.length()

    # snippet: /length

    # snippet: append
    def append(self: IntList, element: int) -> IntList:
        ending: IntList = self.end()
        ending.rest = IntList(element, IntList(None, None))
        return self

    # snippet: /append

    # snippet: concat
    def concat(self: IntList, second: IntList) -> IntList:
        ending: IntList = self.end()
        ending.rest = second
        return self

    # snippet: /concat

    # snippet: contains
    def contains(self: IntList, to_search: int) -> bool:
        if self.first == int:
            return True
        if self.first is None or self.rest is None:
            return False
        return self.rest.contains(to_search)

    # snippet: /contains

    def __eq__(self, other: IntList):
        if self.is_empty() and other.is_empty():
            return True
        if self.first != other.first:
            return False
        return self.rest == other.rest


# snippet: sort
def sort(to_be_sorted: IntList) -> IntList:
    # empty lists are already sorted
    if to_be_sorted.is_empty():
        return to_be_sorted

    # first step
    sorted_list = IntList(to_be_sorted.first, IntList(None, None))
    to_be_sorted = to_be_sorted.rest

    # insert elements until no elements are to be inserted
    while not to_be_sorted.is_empty():
        sorted_list = insert(sorted_list, to_be_sorted.first)
        to_be_sorted = to_be_sorted.rest

    return sorted_list


# snippet: /sort

# snippet: insert
def insert(sorted_target: IntList, element: int) -> IntList:
    if sorted_target.first > element:
        return IntList(element, sorted_target)

    current: IntList = sorted_target.rest
    previous: IntList = sorted_target

    while not current.is_empty():
        if current.first > element:
            new: IntList = IntList(element, current)
            previous.rest = new
            return sorted_target

        if current.first < element:
            previous = current
            current = current.rest

    sorted_target.append(element)
    return sorted_target


# snippet: /insert

# snippet: main
if __name__ == '__main__':
    my_list = IntList(188, IntList(5, IntList(3, IntList(None, None))))
    my_empty_list = IntList(None, None)

    print(my_list.contains(188))
