class SentenceAnalyser:
    def __init__(self):
        self.sentence={"Clauses":0 , "Complete sentences":0 , "Questions":0}

    def __str__(self):
        string = ""
        for i in self.sentence:
            string += i + ":" + str(self.sentence[i]) + '\n'
        return string

    def analyse_sentences(self, decoded_sequence):

        decoded_sequence= decoded_sequence.replace(' ', '') # Cancels the spaces in order to recognize
        list=[]                                             # consequent punctuations that have just space between them

        for i in decoded_sequence:  # Puts all the elements of string in a list in order to mute it in following steps
            list += i

        i = 0
        while i < len(list)-1:                                                       # This while loop searches for consequent punctuations and then takes only the first occurance of the sequence
            if (list[i] in ['?', '.', ','] )and (list[i + 1] in ['?', '.', ',']) :   # Because consequent punctuations doesn't represent more than one sentence
                del(list[i+1])

            else:
                i +=1


        for i in list:  # This loop counts the occurrences of punctuations and stores their meaning in the dictionary.
            if i=='?':
                self.sentence['Questions'] +=1
            elif i=='.':
                self.sentence['Complete sentences'] +=1
            elif i==',':
                self.sentence['Clauses'] +=1


