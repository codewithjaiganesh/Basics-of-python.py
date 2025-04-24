# expecting input john
# expecting output Hello, john! 
name = input("ENTER YOUR NAME: ")
print("Hello" , name , sep=", ", end="!")

# expecting input = 5
# expecting output = " you entered : 5 "
name1 = int(input("plz enter any intger"))
print("You entered:", name1 ) 

#expecting input = 3.14 
#expecting output = "value of pi : 3.14"
name3 = float(input("pi: "))
print("Value of pi: ",name3)


#expecting input = 10 20 30 
# expecting output = Sum of inputs : 60 
a=input()
x,y,z= a.split(" ") 
sum = int(x) + int(y) + int(z)
print("sum of inputs: ",sum )

#expecting input = John , 25
#expecting output = Name : John , Age : 25
name_age = input("plz enter your name and age: ")
name,age = name_age.split(",")
print("Name:",name,",Age:",age,sep=" ")

#expecting input = 5
#expecting output ="Countdown: 5 4 3 2 1 Blast off!"
a=input("enter n:")
print("Countdown: 5 4 3 2 1" , end=" Blast off!")

#expecting input = 10,5
#expecting output = "Addition : 15 , Subraction : 5 , multiplication : 50 , Divison : 2.0"
x,y = input("enter a and b values:").split(",")
a = int(x)
b = int(y)
print("Addition:",a+b,"Subraction",a-b,"Multiplication",a*b,"Divison",a/b ,sep=",")

#expecting input = 10,5
# expecting output = "10>5:True , 10<55: False , 10==5: false , 10 !=5:true"
x,y = input().split(",")
a=int(x)
b=int(y)
print(a>b,a<b,a==b,a!=b , sep=",")

#expecting input = True,False 
#expecting output =  True and false : False , True or False : True , not True : False 
x,y=input().split(",")
print(True and False , True or False , not True )


