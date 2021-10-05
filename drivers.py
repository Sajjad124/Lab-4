
b = answer_sheet = [
		'1.' , 'A' , '6.' , 'B' , '11.' , 'A' , '16.' , 'C'
		'2.' , 'A' , '7.' , 'B' , '12.' , 'A' , '17.' , 'C'
		'3.' , 'A' , '8.' , 'B' , '13.' , 'A' , '18.' , 'C'
		'4.' , 'A' , '9.' , 'B'	, '14.' , 'A' , '19.' , 'C'
		'5.' , 'A' , '10.', 'B'	, '15.' , 'A' , '20.' , 'C'
]

print("Answer Sheet : \n", answer_sheet)


		
student_answers =[]
file = open("file.txt")
a=student_answers = file.readlines()
file.close()



print("Student Answers : \n" , student_answers)

index = 0 
correct_answers = 0
wrong_answers   = 0
total_questions = 20

# for index in student_answers:
# 	print(cmp(a,b))
	
	
