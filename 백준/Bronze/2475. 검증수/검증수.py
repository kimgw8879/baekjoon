score = list(map(int, input().split()))
a=score[0]**2
b=score[1]**2
c=score[2]**2
d=score[3]**2
e=score[4]**2
total = (a+b+c+d+e)%10
print(total)