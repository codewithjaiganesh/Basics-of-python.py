class employee:
    start_time = "10_Am"
    end_time = "5_PM"

class Teachers(employee):
    def __init__(self,subject):
        self.subject = subject

t1 = Teachers("maths")
t2 = Teachers("english")

print(t1.subject,t2.subject,t1.start_time,t1.end_time)


        