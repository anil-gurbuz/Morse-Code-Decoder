class WordAnalyser:
    def __init__(self):
        self.words = {}

    def __str__(self):
        string=""
        for i in self.words:                               # Takes every key and its corresponding value in the dictionary
            string += i + ":" + str(self.words[i]) + "\n"  # and turns it into a string format of CharacterAnalyser class.
        return string

    def analyse_words(self, decoded_sequence):
        decoded_sequence=decoded_sequence.replace(','," ").replace('.'," ").replace('?'," ")
        # Replaces punctuations with a space. To deal with following type of a sentence "WHO AM I?I AM ANIL"
        # If user enters a punctuation with out a space, it can make module to count two words as one word.
        # Because in following steps, module distinguishes words using spaces.
        words=[]                             # List to hold every word used in decoded sequence
        words = decoded_sequence.split(' ')  # Divides the sequence due to spaces and results a list of words

        while "" in words:   # Since we changed punctuations into spaces, there may be consequent spaces in the decoded sequence.
            words.remove("") # And if this is the case, there will be empty string elements in the words list.
                             # To get rid of these empty string elements, this part of module removes empty elements in the words list.

        set_of_words=set(words)   # Creates a set using words list. If there are repeating words, it wont be duplicated in set
        set_of_words.discard(' ') # and this set will be appropriate to create a dictionary structure which needs to have every key just once.

        for i in set_of_words:   # Takes every element of set and makes it key in the dictionary and gives the value zero
            self.words[i]=0      # For every key element in the dictionary

        for i in words:          # Takes every word in the words list and adds 1 to corresponding key value in the dictionary structure.
            self.words[i] += 1

