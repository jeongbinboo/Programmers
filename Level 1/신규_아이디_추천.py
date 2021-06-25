def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    copy1=''
    copy2=''
    
    for i in new_id:
        if i >= 'a' and i <= 'z':
            copy1+=i
        elif i >= '1' and i <= '9':
            copy1+=i
        elif i == '-' or i == '_' or i == '.':
            copy1+=i
        else:
            continue

    for i in range (len(copy1)):
        if i == len(copy1)-1:
            copy2+=copy1[i]
            break
        if copy1[i]=='.':
            if copy1[i+1]=='.':
                continue
            else:
                copy2+=copy1[i]
        else:
            copy2+=copy1[i]
    copy1=''

    if copy2[0]=='.':
        if copy2[len(copy2)-1] == '.':
            copy2=copy2[1:len(copy2)-1]
        else:
            copy2=copy2[1:len(copy2)]
    else:
        if copy2[len(copy2)-1] == '.':
            copy2=copy2[0:len(copy2)-1]
    

    if len(copy2)==0:
        copy2+='a'


    copy1=''
    if len(copy2)>=16:
        copy1=copy2[0:15]
    elif len(copy2)<=2:
        copy1=copy2
        while len(copy1) !=3:
            copy1+=copy1[len(copy1)-1]
    else:
        copy1=copy2
    
    copy2=''
    if copy1[0]=='.':
        if copy1[len(copy1)-1] == '.':
            copy1=copy1[1:len(copy1)-1]
        else:
            copy1=copy1[1:len(copy1)]
    else:
        if copy1[len(copy1)-1] == '.':
            copy1=copy1[0:len(copy1)-1]
            
    return copy1
