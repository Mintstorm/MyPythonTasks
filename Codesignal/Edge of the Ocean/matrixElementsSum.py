def solution(matrix):
    mt = list(zip(*matrix))
    from itertools import takewhile
    return sum([sum(takewhile(lambda x: x>0, y)) for y in mt])
