





# f = open("file.txt")


answer = ['1. A' , '2']

# print("readlines Return list ")
# lines =  f.readlines()
# print(lines)
# print(answer)

# a=int(lines[0])
# b=int(answer[0])

# for i in lines:
# 	if a==b:
# 		a=int(lines[0])+1
# 		b=int(answer[0])+1
# 		print("h")
# 	else:
# 		print("Not =")

l1=[1, '1.a' , 2]
l2=[1, 'a' , 2]

if l1==l2:
	print("Equal")
else:
	print("Not Equal")

# f.close()
for i in answer:
	f=open("file.txt")
	student_ans = f.readlines()	
	a=str(answer)
	b=str(student_ans)

	if a==b:
		print("Corr")
	else:
		print("Not Corr")

	# print(type(b))
	# print(type(a))
	f.close()


