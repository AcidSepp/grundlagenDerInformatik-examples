# snippet: loop_forever
def loop_forever():
    while True:
        print("Looping!")
# snippet: /loop_forever

# snippet: do_not_loop
def do_not_loop():
    print("Not Looping!")
# snippet: /do_not_loop

# snippet: halts
def halts(p) -> bool:
    ???
# snippet: /halts

# snippet: halts_semi
def halts_semi(p) -> bool:
    p()
    return True
# snippet: /halts_semi

# snippet: equal
def equal(p0, p1) -> bool:
    ???
# snippet: /equal

# snippet: my_p
def my_p():
    ???
# snippet: /my_p

# snippet: troll
def troll():
    if halts(troll):
        loop_forever()
    else:
        do_not_loop()
# snippet: /troll

if __name__ == '__main__':
# snippet: halts_loop_forever
    print(halts(loop_forever)) # should print 'False'
# snippet: /halts_loop_forever

# snippet: halts_do_not_loop
    print(halts(do_not_loop)) # should print 'True'
# snippet: /halts_do_not_loop

# snippet: halts_troll
    print(halts(troll)) # ???
# snippet: /halts_troll

# snippet: equal_to_halt_loop_forever
    equal(p, loop_forever)
# snippet: /equal_to_halt_loop_forever

# snippet: equal_to_halt_do_not_loop
    equal(p, do_not_loop)
# snippet: /equal_to_halt_do_not_loop

