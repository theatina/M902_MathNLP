import argparse

#Exercises
class Exercises:
    
    def ex_1_1(self, sentence="Μια παπια μα ποια παπια; Μια παπια με παπια."):
        #Set of all the characters of the sentence
        A = set(sentence)
        
        #Number of different characters (cardinal number of character set)
        cardinal_number_A = len(A)
        print("\nA = " + str(A))
        print("\nΠληθικός αριθμός συνόλου A: " + str(cardinal_number_A) + "\n")
    
    def ex_1_2(self, sentence="Δεν προλαβαίνω ποτέ δεν προλαβαίνω"):
        #Splitting the sentence to get the set of all the words
        words = sentence.split(" ")
        A = set(words)
        
        #Find the number of words in the set (cardinal number of the word set)
        cardinal_number_A = len(A)
        print("\n A = " + str(A))
        print("\nΠληθικός αριθμός συνόλου A: " + str(cardinal_number_A) + "\n")

    #making use of capital letters, in order not to have to deal with the two s 's, "σ" and "ς"
    def ex_1_3(self, sentence="οι πολιτικες και οικονομικες εξελιξεις διαδραματιζονται γυρω απο τις προσπαθειες, τις βλεψεις και τους αγωνες για τον ελεγχο των φυσικων πορων"):
        #Set of all the capital greek letters
        alphabet = set("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")
        
        #In both cases of 'ς' and 'σ', the upper letter will be the same('Σ'), merging the two different lower symbols
        A = set(sentence.upper())
        
        #Creation of the sets 'A' and 'alphabet' intersection set - common letters
        common_letters = alphabet.intersection(A)
        #Find the letters of the alphabet that are not included in the sentence set
        non_common_letters = alphabet-common_letters

        #Find how many letters are common
        cardinal_number_common_letters = len(common_letters)

        print("\nΠληθικός αριθμός συνόλου γραμμάτων που περιέχονται στη φράση: " + str(cardinal_number_common_letters))
        
        #In order to be a pangram, we need the cardinal number of the common letters set to be exactly 24(greek alphabet)
        if cardinal_number_common_letters is len(alphabet):
            print("\nThe sentence: '%s' is a Pangram of length %d! \n"%(sentence,len(sentence)))
        else:
            print("\nThe sentence: '" + sentence + "' is ΝΟΤ a Pangram ! \n\n( set of missing letters: " + str(non_common_letters) + " )\n")


    def ex_1_4(self):
        print("\nΔε μπορούμε να συμπεράνουμε ότι μια φράση είναι pangram εάν έχει απλά πληθικό αριθμό συνόλου χαρακτήρων 24, καθώς μπορεί να περιέχει και άλλους χαρακτήρες όπως σημεία στίξης (';', '.', ',', κλπ)\n")

    def ex_1_5(self):
        A = [ 'ενα', 'νεα', 'εννεα']
        print("\n3 λέξεις με σύνολο γραμμάτων το {α, ε, ν}: " + str(A) + "\n")

    def ex_1_6(self):
        A = [ 'ΠΡΑΣΟ', 'ΣΠΑΡΟΣ', 'ΠΡΑΟΣ', 'ΑΣΠΡΟΣ']
        print("\nΛέξεις με σύνολο γραμμάτων το {Α, Ο, Π, Ρ, Σ}: " + str(A) + "\n")

    def ex_1_7(self):
        A = [ 'ΠΛΟΙΟ', 'ΠΑΛΙΟΙ', 'ΠΑΛΙΟ', 'ΛΟΙΠΟΙ', 'ΠΟΛΛΟΙ']
        print("\nΛέξεις με σύνολο γραμμάτων το {Π, Ι, Λ, Ο}, με μήκος > 4: " + str(A) + "\n")

    def ex_1_8(self):
        words = ['νερο', 'ποταμι', 'οργη']
        vowels_gr = set('αεηιουω')
        A = set()
        for word in words:
            A.update(word)

        vowels_not_in_words = vowels_gr - A.intersection(vowels_gr)
        print(vowels_not_in_words)

    def ex_1_9(self, phrase1 = 'οι επιστημονες εστιαζουν στην αντιμετωπιση του ιου', phrase2 = 'οι επιστημονες εστιαζουν στην αντιμετωπιση της φτωχιας'):
        phrase1_list = phrase1.split(" ")
        phrase1_set = set(phrase1_list)
        
        phrase2_list = phrase2.split(" ")
        phrase2_set = set(phrase2_list)

        non_significant_words = set(['οι', 'στην', 'του', 'της'])

        significant_non_common_words = phrase1_set.symmetric_difference(phrase2_set)
        significant_non_common_words = significant_non_common_words - non_significant_words
        print("\nPhrases:\n1. '" + str(phrase1) +"'\n2. '" + str(phrase2) + "'\n\nSignificant non common words of 1 & 2: " + str(significant_non_common_words) + "\n")


    def ex_1_10(self):
        f = open ('set_theory_lab/cnn-gr_raw.txt', 'r', encoding='utf-8')
        text_X = f.read()
        f.close()
        
        f = open ('set_theory_lab/news247_raw.txt', 'r', encoding='utf-8')
        text_Y = f.read()
        f.close()
        
        set_X = set(text_X.split(" "))
        set_Y = set(text_Y.split(" "))

        common_words = set_X.intersection(set_Y)
        symm_diff = set_X.symmetric_difference(set_Y)

        com_wor_cardinality = len(common_words)
        ratio_X = com_wor_cardinality/len(set_X)
        ratio_Y = com_wor_cardinality/len(set_Y)

        print("\nCommon words: %d\nSymmetric Difference: %d\nRatio_X ( common_words_cardinality/len(set1) ): %.3f\nRatio_Y ( common_words_cardinality/len(set2) ): %.3f\n\n"%(len(common_words), len(symm_diff), ratio_X, ratio_Y))

        threshold = 0.77
        if (ratio_X > threshold):
            print("\nText X copies text Y ! !\n") 
        elif (ratio_Y > threshold):
            print("\nText Y copies text X ! !\n") 
        else:
            print("\nALL CLEAR ! !\n") 

    


#main
parser = argparse.ArgumentParser()
parser.add_argument("-ex", type=int, help="number of exercise to solve", default=1)
args = parser.parse_args()

if (args.ex > 10) or (args.ex < 1):
    print("\nExercises between 1 - 10 ! !\n")
    exit()

line = ["_" for i in range(100)]
line = "".join(line)

function_to_call_name = "ex_1_" + str(args.ex)
fun_to_call = getattr(Exercises, function_to_call_name)

print("\n"+str(line)+"\n")
fun_to_call(Exercises)
print(str(line)+"\n")