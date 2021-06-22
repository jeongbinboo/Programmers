def solution(nums):
    answer = 0
    pkm=set(nums)
    if(len(pkm)>(len(nums)/2)):
        answer=(len(nums)/2)
    else:
        answer=len(pkm)
    return answer
