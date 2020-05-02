x = int(input())
count=0
amount = 100
while(amount<x):
    amount=int(amount*(1+0.01))
    count+=1
print(count)