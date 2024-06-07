import re


def is_subsequence(substring, string):
    words = substring.split()
    pattern = '.*'.join(map(re.escape, words))
    match = re.search(pattern, string)
    return bool(match)
