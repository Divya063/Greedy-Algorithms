# Uses python3
import sys
n=int(input())
l=[]
l1=[10,5,1]
for i in range(len(l1)):
	while(n>0):
		if n>=l1[i]:
			n=n-l1[i]
			l.append(l1[i])
		elif(n<l1[i]):
			i=i+1
print(len(l))
