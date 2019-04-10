import string

#
from nltk.stem.isri import ISRIStemmer

isri = ISRIStemmer()




text = "على قيادة المؤتمر الشعبي العام قراءة رسالة الشعب جيدا من خلال احتشاد ميدان السبعين ، والتي تعني تحمل مسؤليته"

words = text.split()

new_words = []

for word in words:
	#stem word
	new_word = isri.stem(word)
	#print("."+new_word+".")

	#dont append if stemming turns it into whitespace/""
	if new_word != "":
		new_words.append(new_word)

#return this
new_text = ' '.join(new_words)

print(new_text)