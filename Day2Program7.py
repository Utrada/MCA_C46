marks=[50,30,40,60,70]

n=len(marks)
temp=0

for i in range(0,n-1):
    for j in range(0,n-i-1,1):
        if marks[j]<marks[j+1]:
            temp=marks[j]
            marks[j]=marks[j+1]
            marks[j+1]=temp

for i in range(0,3):
    print("Scolar",i+1,"Student For Scolarship Mark Is=",marks[i])