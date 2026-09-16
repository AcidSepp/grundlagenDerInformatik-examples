# snippet: universal_halts
def universal_halts(p) -> bool:
    for i in I:
        p(i)
    return True
# snippet: /universal_halts