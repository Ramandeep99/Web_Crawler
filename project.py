

# Scrapping a website content and finding the frequency of each word
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


# Scrapper function
def start(url):

	# empty list to store the contents of the website fetched from our web-crawler
	wordlist = []
	source_code = requests.get(url).text

	# BeautifulSoup object which will ping the requested url for data
	soup = BeautifulSoup(source_code, 'html.parser')
	
	# Text in given web-page is stored under
	# the <div> tags with class <entry-content>
	for each_text in soup.findAll():
		content = each_text.text

		# use split() to break the sentence into
		# words and convert them into lowercase
		words = content.lower().split()

		for each_word in words:
			wordlist.append(each_word)
		clean_wordlist(wordlist)
	# print(wordlist)

# Function removes any unwanted symbols
def clean_wordlist(wordlist):

	clean_list = []
	for word in wordlist:
		# regex to remove symbols
		symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

		for i in range(len(symbols)):
			word = word.replace(symbols[i], '')

		if len(word) > 0:
			clean_list.append(word)
	create_dictionary(clean_list)

# Creates a dictionary containing each word's frequency
def create_dictionary(clean_list):
	word_count = {}

	for word in clean_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

	# operator.itemgetter() takes one
	# parameter either 1(denotes keys)
	# or 0 (denotes corresponding values)

	for key, value in sorted(word_count.items(),
					key = operator.itemgetter(1)):
		print ("% s : % s " % (key, value))



# Driver code
if __name__ == '__main__':
	url = "https://www.google.com/"
	# starts crawling and prints output
	start(url)

