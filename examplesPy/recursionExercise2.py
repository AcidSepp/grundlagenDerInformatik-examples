def my_function(x: int) -> int:
    if x > 0:
        return 3 // my_function(x - 1)
    else:
        return 1
