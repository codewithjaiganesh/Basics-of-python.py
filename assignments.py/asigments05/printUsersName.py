data = True
with open(r"D:\XboxGames\githubb\Basics-of-python.py\assignments.py\asigments05\names.txt","w") as f:
    f.writelines("Jai\nGanesh\nbhanu\nraja\ngow\n")
with open(r"D:\XboxGames\githubb\Basics-of-python.py\assignments.py\asigments05\names.txt","r+") as p:
    content = p.readlines()
    print(content)
