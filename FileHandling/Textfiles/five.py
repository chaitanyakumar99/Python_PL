#append text into emp.txt file 

fp=open('emp.txt','a')
data = "Hi hello"
fp.write(data)
fp.close()