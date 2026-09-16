def my_function(x: int) -> int:
    if x > 50:
        return my_function(x // 3 + 1)
    if x > 100:
        return my_function(x // 4 + 2)
    else:
        return 1
