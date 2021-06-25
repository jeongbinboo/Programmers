def solution(participant, completion):
    answer = ''
    flag=0
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer=participant[i]
            flag=1
            break
    if flag==0:
        answer=participant[len(participant)-1]
    return answer
