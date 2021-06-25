def solution(v):
    res={
        
    }
    answer=[]
    for i in range(len(v)):
        for j in range(2):
            if v[i][j] in res:
                res[v[i][j]]+=1
            else:
                res[v[i][j]]=1

    for i in res:
        if res[i]%2 != 0:
            answer.append(i)
            
    if answer in v:
        tmp=answer[0]
        answer[0]=answer[1]
        answer[1]=tmp
    print (answer)
    return answer
v=[[1,5],[2,2],[1,2]]
solution(v)
