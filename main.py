import sys


#filepath as input and return the file as a string

def get_book_text(filepath):

#open a file from the defined filepath which is delivered as an argument to the function
#Return the read file as a string which is saved in the variable file_contents

	with open(filepath) as f:
		file_contents = f.read()
		return file_contents


from stats import get_num_words
from stats import get_num_characters
from stats import sort_dic_list

#main fucntion which will use get_book_text

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	text = get_book_text (book_path)
	num_words = get_num_words(text)
	no_letters = get_num_characters(text)
	sorted_report = sort_dic_list(no_letters)
	print ("============ BOOKBOT ============")
	print ("Analyzing book found at ...")
	print ("----------- Word Count ----------")
	print (f"Found {num_words} total words")
	print ("--------- Character Count -------")
	#print (f"{no_letters}")
	for dic_item in sorted_report:
		character = dic_item["char"]
		count = dic_item["num"]
		if character.isalpha():
			print (f"{character}: {count}")
	print ("============= END ===============")

if __name__ == "__main__":
	main()

	
