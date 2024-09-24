#imports
import requests
import sys

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

#stores the links 
links = []

def extract_links(text):

	pattern1 = "<a"
	pattern2 = "</a>"

	start = search(pattern1, text)
	end = search(pattern2, text)

	if(start[0] and end[0]):

		new_text = text[end[2]:len(text)]

		output = ""

		for i in range(start[1], end[2]):
			output += text[i]

		pattern_href1 = "href"
		pattern_href2 = ">"

		start = search(pattern_href1, output)
		end = search(pattern_href2, output)
		
		new_output = ""

		for i in range(start[2], end[1]):
			new_output += output[i]

		final_output = ""

		for i in new_output:
			if(i == "=" or i == "'" or i == " " or i == '"'):
				continue
			final_output += i

		links.append(final_output)
		return new_text
	else:
		return False
#main function
def main():
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        text = response.text
    elif response.status_code > 399:
        print("Error:",response.status_code)
	return

    while(True):
        if text == False:
            break
        text = extract_links(text)

    for link in links:
        print(link)	

#calling main function
main()
