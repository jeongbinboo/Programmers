def solution(numbers, hand):
    answer = ''
    lefthand=[0,0] 
    righthand=[2,0]
    keypad={
        '1':[0,3],'2':[1,3],'3':[2,3],
        '4':[0,2],'5':[1,2],'6':[2,2],
        '7':[0,1],'8':[1,1],'9':[2,1],
        '*':[0,0],'0':[1,0],'#':[2,0]
    }
    i=0
    for i in range(len(numbers)):
        left=0
        right=0
        if(numbers[i]==1 or numbers[i]==4 or numbers[i]==7):
            answer+='L'
            lefthand=keypad[str(numbers[i])]
        elif(numbers[i]==3 or numbers[i]==6 or numbers[i]==9):
            answer+='R'
            righthand=keypad[str(numbers[i])]
        else:
            left=abs(keypad[str(numbers[i])][0]-lefthand[0])+abs(keypad[str(numbers[i])][1]-lefthand[1])
            right=abs(keypad[str(numbers[i])][0]-righthand[0])+abs(keypad[str(numbers[i])][1]-righthand[1])
            if(left>right):
                answer+='R'
                righthand=keypad[str(numbers[i])]
            elif(right>left):
                answer+='L'
                lefthand=keypad[str(numbers[i])]
            else:
                if(hand=='left'):
                    answer+='L'
                    lefthand=keypad[str(numbers[i])]
                else:
                    answer+='R'
                    righthand=keypad[str(numbers[i])]
     
    return answer
