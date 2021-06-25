def solution(lottos, win_nums):
    answer = []
    corr=0
    rank=[6,6,5,4,3,2,1]
    for i in win_nums:
        if i in lottos:
            corr+=1
            
    return [rank[corr+lottos.count(0)],rank[corr]]
