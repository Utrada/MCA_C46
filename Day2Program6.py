book=[10,60,50,40]

n=len(book)

temp=0

for i in range(0,n-1):
    for j in range(0,n-i-1,1):
        if book[j]<book[j+1]:
            temp=book[j]
            book[j]=book[j+1]
            book[j+1]=temp
            
print(book)