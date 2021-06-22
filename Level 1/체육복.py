def solution(n, lost, reserve):
    answer = 0
    same=[]
    pos=reserve
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]==reserve[j]: 
                same.append(lost[i])
    for i in range(len(same)):
        lost.remove(same[i])
        reserve.remove(same[i])
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if(reserve[i]-1 == lost[j] or reserve[i]+1 == lost[j]):
                del lost[j]
                break
                
    answer=n-len(lost)
    return answer
