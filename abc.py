dic={1:10, 2:20,3:30, 4:40,5:50,6:60}
key=int(input("Enter key: "))
flag=0
for k in dic:
	if k==key:
		flag=1
if flag==1:
	print("Yes key",key,"Exist")
else:
	print("No key",key,"does not Exist")