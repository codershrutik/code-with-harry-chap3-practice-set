import datetime
now = datetime.datetime.now()

name = input("enter your name: ")

print("Dear ",name)
print("You are selected")
print ("Current date: ",now.strftime("%Y-%m-%d"))