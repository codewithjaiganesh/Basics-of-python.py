x = int(input("Marks in Maths:"))
y = int(input("Marks in Science:"))
z = int(input("Marks in English:"))
Totalmarks = x + y + z
Averagemarks = Totalmarks/3
print("Total Marks:",Totalmarks)
print("Average Marks:", Averagemarks)
if Averagemarks >= 90:
    print("Grade:A")
elif Averagemarks >=80:
    print("Grade:B")
elif Averagemarks >=70:
    print("GRade:C")
elif Averagemarks >=60:
    print("Grade:D")
elif Averagemarks >=50:
    print("Grade:E")
else:
    print("FAIL")

