class Decoder:
    def __init__(self):
        self.dictionary= {
   '01':'A',   '1000':'B',   '1010':'C',    '100':'D',     '0':'E',
 '0010':'F',    '110':'G',   '0000':'H',     '00':'I',  '0111':'J',
  '101':'K',   '0100':'L',     '11':'M',     '10':'N',   '111':'O',
 '0110':'P',   '1101':'Q',    '010':'R',    '000':'S',     '1':'T',
  '001':'U',   '0001':'V',    '011':'W',   '1001':'X',  '1011':'Y',
 '1100':'Z',  '11111':'0',  '01111':'1',  '00111':'2', '00011':'3',
'00001':'4',  '00000':'5',  '10000':'6',  '11000':'7', '11100':'8',
'11110':'9', '010101':'.', '110011':',', '001100':'?'}



    def __str__(self):
        string=""
        for i in self.dictionary:                           # Takes every key and its corresponding value in the dictionary
            string += i + ":" + self.dictionary[i] + "\n"   # and turns it into a string format of Decoder class.
        return string



    def decode(self,morse_code_sequence):
        coded_words = morse_code_sequence.split("***") # Divides the entered sequence into words.
        decoded = "" # Created to hold decoded part of the sequence

        for each_word in coded_words:
            coded_letters = each_word.split('*') # Divides every coded word into coded letters
            for each_letter in coded_letters:
                if each_letter in self.dictionary: # Checks if the coded letter is in predefined dictionary or not
                    decoded += self.dictionary[each_letter] # If the coded letter exist in dictionary, decodes it
                                                            # and adds it to decoded sequence holder( variable decoded)
                else:
                    return 'Invalid input, it is not defined in morse code dictionary.'# if the coded letter is not in predefined dictionary
                                                                                        # returns an error message
            decoded += ' ' # This is the end of outer 'for' loop which takes every word to decode.
                           # After decoding a word this command adds a space to decoded sequence.
        decoded = decoded.strip() # This command is executed after all the words are decoded. The command in the previous line adds a space after finishing decoding process of a word
                                  # but for the last word it shouldn't happen so this command cancels the last space.

        if decoded[len(decoded)-1] not in ["?",".",","]:                     # Checks whether the last element of decoded sequence is a punctuation or not.
            return 'Invalid input, it can not finish without a punctuation.' # If not returns an error message




        return decoded # If there is no error in previous steps, module returns to decoded sequence.

