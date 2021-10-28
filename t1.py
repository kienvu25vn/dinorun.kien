
list1 = [{'make':'Nokia','model':'216','color':'Black'},{'make':'MIMAX','model':'2','color':'Gold'},{'make':'SamSung','model':'7','color':'Blue'}]
list1.sort(key= lambda x: x['color'])
print(list1)


n = int(input())
fibo = lambda x : x if x < 2 else fibo(x-1) + fibo(x-2)
for i in range(n):
	print(fibo(i),end = " ")


a = [1,2,3,4,5,6,7,8]

b = [4,7,8]
print()
ls = filter(lambda x : x in a,b)
print(list(ls))