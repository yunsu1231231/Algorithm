N = input()
arr_left = []
arr_right = []
count = 0 
for i in range(0,len(N)-1):
    if N[i] == "(" and N[i+1] =="(":
        arr_left.append(i)
    elif N[i] == ")" and N[i+1] ==")":
        arr_right.append(i)

index = 0 
for i in arr_right:
    while index < len(arr_left) and arr_left[index] < i:
        index += 1
    count += index

print(count)