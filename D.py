x1, y1=map(int, input().split())
x2, y2=map(int, input().split())
x3,y3=map(int, input().split())
Xaxis=[x1,x2,x3]
Yaxis=[y1,y2,y3]
result=[]
#creating dictionary for counting number of apperance to each digit
#return the coordinate with value =1 , as each coordinate must appear twice
digit_count = {}
for digit in Xaxis:
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1
# print the keys with value 1
for key, value in digit_count.items() :
    if value == 1:
        result.append(key)  
        
digit_count_y = {}
for i in Yaxis:
    if i in digit_count_y:
        digit_count_y[i] += 1
    else:
        digit_count_y[i] = 1
# print the keys with value 1
for key, value in digit_count_y.items():
    if value == 1:
        result.append(key)   
            
print(*result)