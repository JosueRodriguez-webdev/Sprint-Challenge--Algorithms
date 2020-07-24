'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
counter = {
    0: 0
}

th_finder = {'th': 0}


def count_th(word):
    # check word[0] and the [1] to see if it matches 'th'

    # if the word is less than 2 letters then return the th counter finder
    if len(word) < 2:
        result = th_finder['th']
        th_finder['th'] = 0
        return result
    # if yes then counter +=1 and remove the the [0] index
    if word[0] + word[1] == 'th':
        th_finder['th'] += 1
        count_th(word[1:])
    else:
        count_th(word[1:])
    # else recursive call


trial = count_th("abcthxyz")
print(trial)

trial2 = count_th("caathjs")
print(trial2)
