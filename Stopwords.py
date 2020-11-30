from spacy.lang.en import English

# Load the English part of speech monitoring moduel
nlp = English()

text = open('content_output.txt')
doc = nlp(text.read())
# nlp object is used to create a document with language annotations.

token_list = []  # Use token for word segmentation and build word list
for token in doc:
    token_list.append(token.text)

from spacy.lang.en.stop_words import STOP_WORDS  # Import stop word dictionary from spacy's library

filtered_word = []

for word in token_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:  # Remove the stop words in the dictionary and create a new word list by filtering the results
        filtered_word.append(word)

print(filtered_word)

output = open('content_output_filtered.txt', mode='a', encoding='utf-8')  # Output the result as a new txt file
print(filtered_word, file=output)
#输出的是个列表