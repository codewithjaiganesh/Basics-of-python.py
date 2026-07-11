line  = 1
data = True
word = "Python"
with open("sample.txt","r") as f:
    while data:
      data = f.readline()
      if(word in data):
         print(f"the {word} found at {line}")
         print("found")
         break
      line +=1