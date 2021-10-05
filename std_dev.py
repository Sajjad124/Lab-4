


x1=int(input("Enter x1 "))
x2=int(input("Enter x2 "))
x3=int(input("Enter x3 "))
x4=int(input("Enter x4 "))
x5=int(input("Enter x5 "))

sum_of_values=0
length_of_num =5


standard_deviation(x1,x2,x3,x4,x5)
def standard_deviation(x1,x2,x3,x4,x5):
        sum_of_values=x1+x2+x3+x4+x5
        print("Sum : ",sum_of_values)
        means = sum_of_values/length_of_num
        
        sum_of_squared = (x1-means)**2+(x2-means)**2+(x3-means)**2+(x4-means)**2+(x5-means)**2
        std_dev = (sum_of_squared/length_of_num) **0.5
        print("Standard Deviation : ",std_dev)



