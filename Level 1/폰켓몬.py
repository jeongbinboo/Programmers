// 처음 내 풀
def solution(nums):
    answer = 0
    pkm=set(nums)
    if(len(pkm)>(len(nums)/2)):
        answer=(len(nums)/2)
    else:
        answer=len(pkm)
    return answer

// 우수 풀이
def solution(nums):
    answer=min(len(nums)/2,len(set(nums)))
    return answer
