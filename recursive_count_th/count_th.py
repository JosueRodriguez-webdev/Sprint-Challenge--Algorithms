'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
counter = {
    0: 0
}


def count_th(word):
    print(counter[0], word)

    print(counter)
    if 'th' in word:
        remove_one_instance = word.replace('th', 'zz', 1)
        counter[0] += 1
        print(counter)
        return count_th(remove_one_instance)
    else:
        hold_count = counter[0]
        counter[0] = 0
        return hold_count
