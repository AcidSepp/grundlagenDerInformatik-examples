import re

if __name__ == '__main__':
    input: str = "blahblaahblaaah"
    for match in re.findall('aa+', input):
        print(match)
