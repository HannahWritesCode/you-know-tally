import transcript

file = open(r"jeff_transcript.txt", "r").read()

# Total number of times "you know" was said over the quarter
tally = transcript.phrase_count(file, "You know|you know")
print('"You know" was said ' + str(tally) + " times over the course of this class.")

# Average frequency per lecture, per hour, per minute
print("That's about " + str(round(tally/9)) + " times per lecture.\n")
print("Each lecture was about 2.5 hours long.")
print("So we're looking at about " + str(round(tally/8/2.5, 2)) + " times per hour and " + str(round(tally/8/2.5/60, 2)) + " times per minute.\n")

# Percentage of total words "you know" makes up across all lectures
totalWords = transcript.total_words(file)
print("There were " + str(totalWords) + " words said in this class over the course of the quarter.")
print('The two-word phrase "you know" made up ' + str(round(transcript.percentage_of_total_words(file, "You know|you know"), 2)) + "% of those words.\n")

# Average number of times per sentence 
totalSentences = transcript.total_sentences(file)
mostTimesInOneSentence = transcript.most_times_in_one_sentence(file, "You know|you know")
sentenceWithMost = transcript.sentence_with_most(file, "You know|you know")
print("There were " + str(totalSentences) + " sentences spoken in lectures this quarter.")
print('It was said an average of ' + str(round(tally/totalSentences, 2)) + ' times per sentence.')

# Sentence with most "you knows" 
print("Once it was said " + str(mostTimesInOneSentence) + " times in one sentence! That sentence was... \n")
print('"' + sentenceWithMost.lstrip() + '."')

