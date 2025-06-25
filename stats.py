#count words of a book string
def get_num_words(book):
        word_list  = book.split()
        num_words = len(word_list)
        return num_words

#Count characters in a dictionary
def get_num_characters(book):
	new_word_list = book.lower()
	counter = {}
	for i in new_word_list:
		counter [i] = counter.get(i,0) + 1
	return counter

def sort_dic_list(new_word_list):

	def sort_on(ln):
		return ln["num"]

	counter_list  = []

	for char, num in new_word_list.items():
		new_dic =	 {"char":char,
			 "num":num}
		counter_list.append(new_dic)

	counter_list.sort(reverse=True, key=sort_on)

	return counter_list
