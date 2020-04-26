# unique characters in the string

def unique_char(s):

    char = set()

    for let in s:
        # check if in the set

        if let in char:
            return False
        else:
            # add to the set
            char.add(let)

    return True
print(unique_char('abcdefghi'))
