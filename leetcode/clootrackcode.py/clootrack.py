import sys
if len(sys.argv) != 2:
	raise ValueError('Please provide input file to test the code.')

path = "/home/enemy/Desktop/Projects/pythonDSA/leetcode/clootrackcode.py/"
fileName = path + sys.argv[1]

myfile = open(fileName, "r")
test_cases = myfile.readline()




for _ in range(test_cases):
	entries = myfile.readline()
	dic={}
	for _ in range(len(entries)):
		
		entry = myfile.readline().split(" ")
		name = entry[0]
		tweet_names.append(entry[0])
		

	test_count += 1

	uniq_names = [pref_names.split()[0] for pref_names in tweet_names]
	times = Counter(uniq_names)

	repeat = times.values() 

	for element in set(repeat):
	dupl = ([(key, value) for key, value in sorted(times.items()) if value == element])

	if len(dupl) > 1:
		for (key, value) in dupl:
			print (key,'',value)

	max_value = max(times.values())
	temp_max_result = [(key, value) for key, value in sorted(times.items()) if value == max_value]

	if temp_max_result != dupl:
		for (key,value) in temp_max_result:
			print (key,'',value)



myfile.close()