#Bruteforce approach to regex 
def search(pattern, text):
	flag = False
	for i in range(len(text)):
		if flag == False:
			new_flag = []
			count = 0
			for j in range(len(pattern)):
				if i >= len(text):
					break
				
				if(pattern[j] == text[i]):
					new_flag.append(True)
				else:
					new_flag.append(False)
				i += 1
			for k in new_flag:
				if(k == True):
					count += 1
			if count == len(new_flag):
				flag = True
		else:
			return [True, i - 1, i + (len(pattern) - 1)]
	return [False]