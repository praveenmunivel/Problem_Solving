def triplets(arr):
    n = len(arr)
    sum,sum2,count=0,0,0
    for i in range(n):
        sum = arr[0]
        arr.pop(0)
        for j in range(n-1):
            sum2 = arr[j]+arr[j-1]
            if(sum2 == sum):
                count +=1
        arr.append(sum)
    return count
T = int(input())
lst = []
for i in range(T):
    x = int(input())
    for j in range(x):
        lst.append(int(input()))
    p = triplets(lst)
    if p==0:
        print("-1")
    else:
        print(p)
