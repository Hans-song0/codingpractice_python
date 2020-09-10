location = [(x,y) for x in range(4) for y in range(3)]
key = list('123456789*0#')
pad = {}
for a, b in zip(key,location):
    pad[a] = b

def diff(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

   
def solution(num,hand) :
    answer = []
    lf_loc = pad['*']
    rf_loc = pad['#']
    
    for i in range(len(num)):
        if num[i] in (1,4,7):
            answer.append('L')
            lf_loc = pad[str(num[i])]
        elif num[i] in (3,6,9):
            answer.append('R')
            rf_loc = pad[str(num[i])]
        else:
            if diff(pad[str(num[i])],lf_loc) < diff(pad[str(num[i])],rf_loc):
                answer.append('L')
                lf_loc = pad[str(num[i])]    

            elif diff(pad[str(num[i])],lf_loc) > diff(pad[str(num[i])],rf_loc):
                answer.append('R')
                rf_loc = pad[str(num[i])]
            else:
                if hand == 'left':
                    answer.append('L')
                    lf_loc = pad[str(num[i])]
                else:
                    answer.append('R')
                    rf_loc = pad[str(num[i])]
                    
    return str(''.join(answer))
        
    

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right'))
