def solution(s1, s2):
    s = list(set(s1))
    sum1 = 0
    for i in s:
        sum1+=min(s1.count(i),s2.count(i)) 
    return sum1

