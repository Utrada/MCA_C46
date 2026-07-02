student=['Raj','Neet','Anchal','Jay','Shubham']

name=input("Enter Name for Check Present or Not:")
flag=0

for i in student:
    if name in i:
        flag=1
        break
    
if flag==1:
    print(name,"Is Present")
else:
    print(name,"Is Not Present")