def my_function(x: int) -> int:
    if x > 3:
        return my_function(3) + my_function(5)
    elif x == 4:
        return my_function(x - 1) + 4
    elif x < 2:
        return my_function(x - 1) - 2
    else:
        return 1
