class CharacterAnalyser:

    def __init__(self):
        self.counter = {
            'A':0, 'B':0,'C':0,'D':0,'E':0,
            'F':0, 'G':0,'H':0,'I':0,'J':0,
            'K':0, 'L':0,'M':0,'N':0,'O':0,
            'P':0, 'Q':0,'R':0,'S':0,'T':0,
            'U':0, 'V':0,'W':0,'X':0,'Y':0,
            'Z':0, '0':0,'1':0,'2':0,'3':0,
            '4':0, '5':0,'6':0,'7':0,'8':0,
            '9':0}

    def __str__(self):
        string = ""
        for i in self.counter:                              # Takes every key and its corresponding value in the dictionary
            string += i + ":" + str(self.counter[i]) +"\n"  # and turns it into a string format of CharacterAnalyser class.
        return string


    def analyse_characters(self, decoded_sequence): # Takes decoded sequence as an argument.
        for i in decoded_sequence:                  # Takes every element in the decoded_sequence
            if i in self.counter:                   # Checks whether the element in dictionary or not
                self.counter[i] +=1                 # If it is in dictionary, adds 1 to its corresponding value

