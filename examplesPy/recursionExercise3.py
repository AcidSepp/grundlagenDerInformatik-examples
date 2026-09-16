def my_function(x: int) -> int:
    if x > 0:
        return my_function(x // 3)
    else:
        return 1
