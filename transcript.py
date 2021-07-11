
"""
This module can be used to analyze a text file or string of transcribed spoken or written word. 

Begin by opening a text file::
    
    text = open(r"example.txt", "r").read()
"""

import re

def total_words(text):
    """
    Finds and returns the total number of words in the text. 

    Args:
        text: The string or txt file to be analyzed. 

    Returns:
        int: Number of words. 

    """
    # remove potential leading and trailing spaces in text
    text = text.lstrip().rstrip() 
    totalWords = 0

    for line in text.split(" "):
        totalWords+=1

    return totalWords

def total_sentences(text):
    """
    Finds and returns the total sentences of words in the text. 

    Args:
        text: The string or txt file to be analyzed. 

    Returns:
        int: Number of sentences. 
    
    """
    sentences = re.split(r'[|?!|!?|.|!|?|...]+', text)

    return len(sentences) - 1 

def most_times_in_one_sentence(text, phrase):
    """
    Returns the highest number of times a given phrase appears in one sentence.

    Args:
        text: The string or txt file to be analyzed.
        phrase (str): A string or regular expression (case sensitive)

    Returns:
        int: Most times a phrase appears in one sentence. 

    """
    mostTimes = 0
    sentences = re.split(r'[|?!|!?|.|!|?|...]+', text)

    for i in sentences: 
        if len(re.findall(phrase, i)) > mostTimes:
            mostTimes = len(re.findall(phrase, i)) 

    return mostTimes

def sentence_with_most(text, phrase):
    """
    Returns a sentence in the text with the most appearances of a given phrase. 

    Args:
        text: The string or txt file to be analyzed.  
        phrase (str): A string or regular expression (case sensitive)

    Returns:
        str: Sentence with the most appearances of a given phrase, 
        or None if no sentence with that phrase is found. 

    """
    mostTimes = 0
    sentenceWithMost = ""
    sentences = re.split(r'[|?!|!?|.|!|?|...]+', text)

    for i in sentences: 
        if len(re.findall(phrase, i)) > mostTimes:
            mostTimes = len(re.findall(phrase, i)) 
            sentenceWithMost = i

    if sentenceWithMost == "":
        return None
    else:
        return sentenceWithMost

def phrase_count(text, phrase): 
    """
    Counts the number of times a given phrase appears in the text. 

    Args:
        text: The string or txt file to be analyzed.
        phrase (str): A string or regular expression (case sensitive)

    Returns:
        int: Number of times the phrase appears in the text. 

    """
    count = 0
    
    for line in re.findall(phrase, text):
        count+= 1

    return count

def percentage_of_total_words(text, phrase):
    """
    Determines the percentage of total words a given phrase makes up in the text. 

    Args:
        text: The string or txt file to be analyzed.
        phrase (str): A string or regular expression (case sensitive)

    Returns:
        float: A decimal number representing a percentage. 

    """
    wordsInPhrase = 0
    totalWords = total_words(text)
    count = phrase_count(text, phrase)

    for line in phrase.split(" "):
        wordsInPhrase+= 1

    return count*wordsInPhrase/totalWords * 100

