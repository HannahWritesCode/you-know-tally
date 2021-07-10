import transcript

file = open(r"jeff_transcript.txt", "r").read()

totalWords = transcript.total_words(file)
print("Number of total words: " + str(totalWords) + "\n")

print("You know: " + str(transcript.phrase_count(file, "You know|you know")))
print("Or whatever: " + str(transcript.phrase_count(file, " Or whatever| or whatever")))
print("You know, or whatever: " + str(transcript.phrase_count(file, "you know, or whatever")) + "\n")

print("Other common words... ")
print("Okay: " + str(transcript.phrase_count(file, "Okay|okay")))
print("Thank you: " + str(transcript.phrase_count(file, "Thank you|thank you")))
print("Scrum: " + str(transcript.phrase_count(file, "Scrum|scrum")))
print("DevOps: " + str(transcript.phrase_count(file, "DevOps")))
print("And then: " + str(transcript.phrase_count(file, "And then|and then")))
print("So: " + str(transcript.phrase_count(file, " So | so ")))
print("So anyway: " + str(transcript.phrase_count(file, "So anyway|so anyway")))
print("And: " + str(transcript.phrase_count(file, "And|and")))
print("Um: " + str(transcript.phrase_count(file, " Um| um")))
print("Yeah: " + str(transcript.phrase_count(file, "Yeah|yeah")))
print("Software': " + str(transcript.phrase_count(file, "Software|software")))

