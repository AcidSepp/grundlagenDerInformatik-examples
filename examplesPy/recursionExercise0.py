def my_function(x: int) -> int:
    if x > 3:
        return my_function(x - 1) + my_function(x - 2)
    else:
        return 1
