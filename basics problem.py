#Find the area of a cricle 
radius = int(input("enter the radius of the circle: "))
a = 3.14*(radius**2)
print("Area of the circle is: ",a,sep="")
print(f"Area of the circle is: {a} ")

#solving quadratic equations
a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))
d = (b**2)-4*a*c
root1 = ((-b+(d**0.5))/2*a)
root2 = ((-b-(d**0.5))/2*a)
print(f"Roots:({root1},{root2})")

#swap values 
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
b = a+b
a = b-a
b  = b-a
print(f"value of a is:{a}")
print(f"value of b is:{b}")

#converting temperature from celsius to fahrenheit
c = int(input("enter the temperture in celsius: "))
f = (c*(9/5))+32
k = 273 + c 
print("temperture in fahrenheit: ", f)
print("temperture in kelvin: ", k)

#Basics currency converter 
USD = int(input("enter the amount:"))
EUR = float(input("enter the amount:"))
exchage = (USD*EUR)
print(f"Equivalent amount in EUR: {exchage}")

