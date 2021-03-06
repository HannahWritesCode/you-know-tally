# you-know-tally
A python module I wrote to analyze a professor's lecture transcripts and his usage of the filler phrase "you know." 

## transcript.py
The module itself is transcript.py. Feel free to use it to you know, analyze your favorite book, lecture, copypasta, or whatever. 

It contains the following functions: 
- total_words(text) - Returns the total number of words in a text file or string. 
- total_sentences(text) - Returns the total number of sentences in a text file or string. 
- most_times_in_one_sentence(text, phrase) - Returns the highest number of times a given phrase (string or regex) appears in one sentence of a text file or string. 
- sentence_with_most(text, phrase) - Returns the sentence that contains that highest number of times a given phrase appears in a text file or string. 
- phrase_count(text, phrase) - Returns the number of times a given phrase appears in a text file or string. 
- percentage_of_total_words(text, phrase) - Returns a float representing the percentage of total words a given phrase makes up in the text file or string. 

## you_know_tally.py
**The results...**  

"You know" was said 6765 times over the course of this class.  
That's about 752 times per lecture.  

Each lecture was about 2.5 hours long.  
So we're looking at about 338.25 times per hour and 5.64 times per minute.  

There were 165440 words said in this class over the course of the quarter.   
The two-word phrase "you know" made up 12.27% of those words.  

There were 7270 sentences spoken in lectures this quarter.  
It was said an average of 0.93 times per sentence.  
Once it was said 14 times in one sentence! That sentence was...  

_"And we've got to break up the silos between, you know, developers and operations that are often have been at war with one another, and got to get everybody to kind of keep your eye on the prize, which is satisfying customers, and let's all work together, you know, to, to do that, and to do it, you know, while we improve the speed, you know, of our operation, and then, you know, then you start looking at how to go faster, I mean, once you get some of the low hanging fruit out of the way, which is like, you know, the silos, you find, well, gee, you know, we can't really go as fast as we want unless we start automating, you know, some of these functions and so automation, things like continuous integration, continuous delivery, are really important, you know, to be able to have a good DevOps, you know, system, and then measurement where you're, you know, measuring what's happening with your infrastructure, and with your applications, so you can improve, you know, if you don't, if you don't measure know what's going on, you know, or talk to customers, you can think everything's fine, and, you know, and it's not, and then sharing the idea of continuous improvement."_  

![word cloud](word_cloud.png)

Word cloud made with [wordart.com](https://wordart.com).  
Transcripts generated from Zoom recordings using [otter.ai](https://otter.ai).  
