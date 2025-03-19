def solution(numbers, k):
    if (1+(k-1)*2)%len(numbers) == 0:
        return len(numbers)
    else: return (1+(k-1)*2)%len(numbers)