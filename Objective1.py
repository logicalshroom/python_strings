# Objective 1: Product Review Analysis

#  1. Product Review Analysis
#  Task 1: Keyword Highlighter
#  
#  Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
#  So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

# Lets make a for loop to iterate over each keyword, find it, remove the slice, and make a new string with the right text.

keyword = ["good", "excellent", "bad", "poor", "average"]

for review in reviews: #For each object in the list
    for word in keyword: #For each word in the list
        if word in review.lower(): #If the word can be found in the review
            trgt_word = review.lower().find(word) #set the target word
            new_str1 = review[:trgt_word] #grab the string before
            new_str2 = review[trgt_word+len(word):] #and after
            review_cap = new_str1 + word.upper() + new_str2 #concat a new string
            print(review_cap)

#  Task 2: Sentiment Tally
#  
#  Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally(text):
    pos_count = 0 #initialize two variables
    neg_count = 0
    for sentence in text: #for every review
        for word in positive_words + negative_words: #iterate over each word in both lists
            if word in sentence.lower() and word in positive_words:
                pos_count += 1
            elif word in sentence.lower() and word in negative_words:
                neg_count += 1
    print(f"There were {pos_count} phrases used.") #print result
    print(f"There were {neg_count} phrases used.")

tally(reviews)

#  Task 3: Review Summary
#  
#  Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
#  
#  Example: "This product is really good. I'm...",

def summary(text): 
    for sentance in text: #for each item in the list
        chr_counter = 29 #set to 29 so we start iterating on the 30th character
        while sentance[chr_counter] != " ": #if the indexed character isn't a space
            chr_counter += 1 #count up
        if sentance[chr_counter] == " ": #but if it is a space
            print(sentance[:chr_counter] + "...") #print everything before the index of the counter, cat a string with the elipses
 
summary(reviews)