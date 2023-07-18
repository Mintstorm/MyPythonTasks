from random import randint
year=randint(1,2005)
def solution(year):
    if year%100:
        return(int((year/100)+1))
    else :
        return(int(year/100))
solution(year)

