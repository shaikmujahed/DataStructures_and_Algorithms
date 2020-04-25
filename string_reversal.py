'''Sentence Reversal
Problem
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'

Solution
We could take advantage of Python's abilities and solve the problem with the use of split() and some slicing or use of reversed:'''


def rev_word(s):

    words = []
    length = len(s)
    spaces = [' ']

    # index tracker
    i = 0

    # whlie indes less than length of string

    while i < length :

        # if element isn't a space

        if s[i] not in spaces:

            # word statrts at this index

            word_list = i

            while i < length and s[i] not in spaces:

                # get the index where word ends
                i+=1

            # append that word to the list
            words.append(s[word_list:i])

        i += 1

        # join the reversed words
    return " ".join(reversed(words))

print(rev_word('  hello join     how are you'))
print(rev_word('     space here'))





        
