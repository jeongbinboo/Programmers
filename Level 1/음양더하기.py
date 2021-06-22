def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]=='true':
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    return answer

absolutes=[4,7,12]
signs=['true','false','true']
print(solution(absolutes,signs))
