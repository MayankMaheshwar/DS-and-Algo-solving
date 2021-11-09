import sys
if len(sys.argv) != 2:
	raise ValueError('Please provide input file to test the code.')

path = "/home/enemy/Desktop/Projects/pythonDSA/leetcode/clootrackcode.py/"
fileName = path + sys.argv[1]

myfile = open(fileName, "r")
test_cases = int(myfile.readline())


ans = []

for _ in range(test_cases):
	entries = int(myfile.readline())
	dic={}
	for _ in range(entries):
		
		entry = myfile.readline().split(" ")
		name = entry[0]
		if name not in dic:
			dic[name]=1
		else:
			dic[name]+=1
		

	dic=sorted(dic.items(),key=lambda x:(x[0],-x[1]))
	maxtweets=dic[0][1]
	for key,value in dic:
		if value!=maxtweets:
			break
		ans.append((key,value))


for name,num_of_tweets in ans:
	print(name+" "+str(num_of_tweets))


myfile.close()