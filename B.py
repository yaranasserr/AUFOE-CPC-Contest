number=input()
#convert it to array of numbers
arr = list(map(int, number))
arr1 = arr[1:] + [arr[0]]
arr2 = arr[2:] + [arr[0]] + [arr[1]]
#convert the array to numbers 
num = int(''.join(map(str, arr)))
num1= int(''.join(map(str, arr1)))
num2 = int(''.join(map(str, arr2)))
answer=num+num1+num2
print(answer)