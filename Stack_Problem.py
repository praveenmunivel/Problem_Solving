def solve(str):
    n = len(str)
    str2 = []
    count = 0
    for i in range(n):
        if(len(str2) ==0 or str2[-1] == str[i]):
            str2.append(str[i])
        else:
            count +=1 
            str2.pop()
    if(count%2 == 0):
        print("B")
    else:
        print("A")
s = "kkaak"
solve(s)
