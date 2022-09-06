numbers = int(input("Enter number:"))

def filter(ran):
    odd=[]
    even=[]
    for i in range(ran):
        if(i%2 ==0) and (i != 0):
            even.append(i)
        else:
            odd.append(i)
    print(f"Even list is : {even}, odd list is : {odd}")

filter(numbers)

odd_list=[]
even_list=[]
[even_list.append(i) if i%2 ==0 else odd_list.a]


