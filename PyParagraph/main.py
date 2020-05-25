## Python scrip that reads a text file and counts the number of words and sentences.
## It also tells the average letters per word and the average words per sentence.

# import modules
import os
import re

# Paths to the different text files to be analyzed
text_file_1_path = os.path.join("Texts", "raw_data_paragraph_1.txt")
text_file_2_path = os.path.join("Texts", "raw_data_paragraph_2.txt")
special_text_file_path = os.path.join("Texts", "special_text.txt")
special_text_2_file_path = os.path.join("Texts", "special_text_2.txt")

# Initialize variables
words_count = 0
sentences_count = 0
letters_words_count = 0
sentence_length = 0
	
with open(text_file_2_path, mode="r") as text_file:
	text_data = text_file.read()

	# list all words and count them
	all_words = text_data.split()
	words_count = len(all_words)

	# find all sentences (or what they look like sentences) and count them.
	regexpr = re.compile(r"([A-Z][^\.!?]*[\.!?])", re.M) # sentence
	sentences = regexpr.findall(text_data)
	sentences_count = len(sentences)

	# count letters in each word and add them together
	for word in all_words:
		letters_words_count += len(word)

	# count words in each sentence and add them together
	for sentence in sentences:
		all_sentence_words = sentence.split()
		sentence_length += len(all_sentence_words)

	# calculate the average of letter per word and words per sentence
	avg_letters_in_word = letters_words_count/words_count
	avg_sentence_length = sentence_length/sentences_count

# Print in console the original text and the result of the analysis
print('Original Text:')
print('-----------------')
print(text_data)
print('-----------------\n')

print('Paragraph Analysis')
print('-----------------')
print(f'Approximate Word Count: {words_count}')
print(f'Approximate Sentence Count: {sentences_count}')
print(f'Average Letter Count: {avg_letters_in_word:.2f}')
print(f'Average Sentence Length: {avg_sentence_length:.2f}')