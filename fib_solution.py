def solution(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return solution(number - 1) + solution(number - 2)