'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # check word[0] and the [1] to see if it matches 'th'

    # if the word is less than 2 letters then return the th counter finder
    if len(word) < 2:
        return 0
    # if yes then counter +=1 and remove the the [0] index
    if word[0] + word[1] == 'th':
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
    # else recursive call
