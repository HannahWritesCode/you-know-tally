import transcript

# tests leading and trailing spaces, percentage_of_total_words, total_words, total_sentences
string1 = " Hey there, centaurs. "
print("\""+ string1.lstrip().rstrip() + "\"\n")
print("Number of words in string: " + str(transcript.total_words(string1)))
print("Number of sentences in string: " + str(transcript.total_sentences(string1)))
print("Percentage of phrase the word 'centaurs' makes up: " + str(round(transcript.percentage_of_total_words(string1, "centaurs"), 2)) + "%")
print("Percentage of phrase the words 'Hey there' makes up: " + str(round(transcript.percentage_of_total_words(string1, "Hey there"), 2)) + "%\n")

# tests case sensitivity, ? and ! punctuation
# tests most_times_in_one_sentence, sentence_with_most with result sentence first 
string2 = "Bye, bye, boys! Have fun storming the castle! Think it'll work? It'll take a miracle. B'bye!"
print("\""+ string2 + "\"\n")
print("Number of words in the string: " + str(transcript.total_words(string2)))
print("Number of sentences in the string: " + str(transcript.total_sentences(string2)))
print("Number of times the phrase 'bye' is used in the string: " + str(transcript.phrase_count(string2, 'bye')))
print("Number of times the phrase 'Bye|bye' is used in the string: " + str(transcript.phrase_count(string2, 'Bye|bye')))
print("Most times the phrase 'bye' is used in one sentence: " + str(transcript.most_times_in_one_sentence(string2, 'bye')))
print("Most times the phrase 'Bye|bye' is used in one sentence: " + str(transcript.most_times_in_one_sentence(string2, 'Bye|bye')))
print("Sentence with most occurences: \"" + str(transcript.sentence_with_most(string2, 'bye')) + "\"\n")

# tests odd ends of sentence punctuation !? and ?! 
string3 = "A fire!? At a sea parks?! It's the weirdest thing I've ever heard!" 
print("\"" + string3 + "\"\n")
print("Number of words in the string: " + str(transcript.total_words(string3)))
print("Number of sentences: " + str(transcript.total_sentences(string3)) + "\n")

# tests case sensitivity, odd percentage_of_total_words cases, sentence_with_most with result sentence last, ellipses punctuation 
string4 = "Knock knock... Knock knock knock."
print("\"" + string4 + "\"\n")
print("Number of sentences in the string: " + str(transcript.total_sentences(string4)))
print("Percentage of string the phrase 'knock' makes up: " + str(transcript.percentage_of_total_words(string4, 'knock')) + "%")
print("Percentage of string the phrase 'Knock' makes up: " + str(transcript.percentage_of_total_words(string4, 'Knock')) + "%")
print("Percentage of string the phrase 'Knock|knock' makes up: " + str(transcript.percentage_of_total_words(string4, 'Knock|knock')) + "%")
print("Percentage of string the phrase 'knock knock' makes up: " + str(transcript.percentage_of_total_words(string4, 'knock knock')) + "%")
print("Percentage of string the phrase 'Knock Knock' makes up: " + str(transcript.percentage_of_total_words(string4, 'Knock Knock')) + "%")
print("Percentage of string the phrase 'Knock knock|knock knock' makes up: " + str(transcript.percentage_of_total_words(string4, 'Knock knock|knock knock')) + "%")
print("Percentage of string the phrase 'ding dong' makes up: " + str(transcript.percentage_of_total_words(string4, 'ding dong')) + "%")
print("Most times the phrase 'Knock|knock' is used in one sentence: " + str(transcript.most_times_in_one_sentence(string4, 'Knock|knock')))
print("Sentence with most occurences: \"" + str(transcript.sentence_with_most(string4, 'Knock|knock')).lstrip()+ "\"")

