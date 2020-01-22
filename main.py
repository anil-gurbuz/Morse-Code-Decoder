from decoder_29628792 import Decoder
from character_29628792 import CharacterAnalyser
from word_29628792 import WordAnalyser
from sentence_29628792 import SentenceAnalyser

def get_input():
    encoded = input("Enter a sequence of morse code: ")

    if encoded.count("***") == 0 : # To ensure every input has at least one set of "***"
        print( "Invalid input, there should be at least one set of three consecutive '*'")
        return False
    if encoded[len(encoded)-6 : len(encoded)] not in ["001100", "010101","110011"]: # To ensure input ends with a punctuation
        print( "Invalid input, every input must end with a punctuation.")
        return False
    coded_words = encoded.split("***")

    for each_word in coded_words:   # To ensure every letter is defined in the dictionary
        coded_letters = each_word.split('*')
        for each_letter in coded_letters:
            if each_letter not in Decoder().dictionary:
                print("Invalid input, it is not defined in the dictionary")
                return False

    return encoded




def choice():   # To create a menu for the user to choose which level of analyse will be made.
    choice = input("If you want to analyse characters: press c then enter \n"
                   "if you want to analyse words: press w then enter \n"
                   "if you want to analyse sentences: press s then enter \n"
                   "if you want to analyse all: press a then enter \n")
    return choice





def main ():
    decoder = Decoder()                         # Instances for all classes
    character_analyser = CharacterAnalyser()
    word_analyser = WordAnalyser()
    sentence_analyser = SentenceAnalyser()

    one_more_entry=True         # created to get input from user until he/she terminates
    all_decoded_strings = ""    # stores all valid, decoded sequences to show total occurrences when the program is terminated

    while one_more_entry == True:
        in_put = get_input()

        if in_put != False:    # Ignores input before decode it. If get_input() returns False, There is an error and program tries to get one more input
            decoded=decoder.decode(in_put)
            all_decoded_strings += decoded # Adds all valid, decoded sequences to show total occurrences when the program is terminated
            print(decoded)   # To show every decoded sequence for every input.
            ch=choice()      #User menu to choose analyses
            if ch=="c":
                character_analyser.analyse_characters(decoded)
                print("Number of characters decoded \n",character_analyser)
            elif ch=='w':
                word_analyser.analyse_words(decoded)
                print("Number of words decoded \n",word_analyser)
            elif ch=="s":
                sentence_analyser.analyse_sentences(decoded)
                print("Number of senteces decoded \n",sentence_analyser)
            elif ch=="a":
                sentence_analyser.analyse_sentences(decoded)
                word_analyser.analyse_words(decoded)
                character_analyser.analyse_characters(decoded)
                print(character_analyser)
                print(word_analyser)
                print(sentence_analyser)


            terminate = input("if you want to terminate, please press t then enter, if not just enter ")
            if terminate =="t":
                break


    totalc=CharacterAnalyser()  # New instances of classes to store and show total occurrences.
    totalw=WordAnalyser()       # We need to create new instances because pre defined ones stores occurences for every entry
    totals=SentenceAnalyser()   # And restarts for every input

    totalc.analyse_characters(all_decoded_strings)
    totalw.analyse_words(all_decoded_strings)
    totals.analyse_sentences(all_decoded_strings)

    print("Total number of character occurrences \n", totalc)
    print("Total number of word occurrences \n", totalw)
    print("Total number of sentences occurrences \n", totals)


if __name__ == '__main__':
    main()