name=input("Enter name: ")
age=int(input("Enter age: "))
import datetime
now =datetime.datetime.now()
Birth=(int(now.year))-age-1
y=Birth+100
print("Hey {} ! You'll turn 100 years old in {}".format(name,y))