#THIS IS A COMMENT
for i in range(0,11): #this is a function
    print('python')
    print('is really good')
#the above 2 lines are an example of indentation
x= 27 #this is an expression
print('Hi, I am Jenifer. I"m',x,'years old')
print('Thank yous')
#the lines above are the statements

name= 'python' #string data type
sum= None #a variable without values

a= 23 #integer
b= 3.14 #float
sum = a+b
print(sum)
#multiple assignment- assign a single value to many variable

a=b=c=1 #single value to multiple variable
a,b=1,2 #multipe value to multiple variable
a,b=b,a #values are being swaped

# krisha investigatory project
stu=int(input("Enter the Total number of students: "))
stud_info = {}
for i in range (stu):
    name = input("Enter your name: ")
    weight=int(input("Enter your current weight: "))
    if weight <= 50:
          T_shirt = int(input("Enter your Tshirt size [numerical value only]: "))
          short = int(input("Enter your short size: "))
          mobile = int(input("Enter your mobile no. : "))
          shoes = int(input("Enter your shoes size [numerical value only]: "))
          age = int(input("How old are you?:"))
          stud_info['name'] = name
          stud_info['T_shirt'] = T_shirt
          stud_info['short'] = short
          stud_info['shoes'] = shoes
          stud_info['age'] = age
          print(stud_info)
    else:
        print("The weight must be less than 50kgs to play in under 17 tournaments!!")