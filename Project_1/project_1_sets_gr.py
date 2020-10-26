import argparse

#Exercises
class Exercises:
    
    def ex_1_1(self, sentence="Μια παπια, μα ποια παπια; Μια παπια με παπια."):
        #Set of all the characters of the sentence
        A = set(sentence)
        
        #Number of different characters (cardinal number of character set)
        cardinal_number_A = len(A)
        print("\nA = " + str(A))
        print("\nΠληθικός αριθμός του συνόλου χαρακτήρων (Α) της φράσης '%s' : %d \n" % (sentence, cardinal_number_A))
    
    def ex_1_2(self, sentence="Δεν προλαβαίνω ποτέ δεν προλαβαίνω"):
        #Splitting the sentence to get the set of all the words
        words = sentence.split(" ")
        A = set(words)
        
        #Find the number of words in the set (cardinal number of the word set)
        cardinal_number_A = len(A)
        print("\n A = " + str(A))
        print("\nΠληθικός αριθμός του συνόλου λέξεων (Α) της φράσης '%s' : %d \n" % (sentence, cardinal_number_A))

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

        # print("\nΠληθικός αριθμός συνόλου γραμμάτων  " + str(cardinal_number_common_letters))
        print("\nΠληθικός αριθμός του συνόλου γραμμάτων που περιέχονται στη φράση: '%s' : %d \n" % (sentence, cardinal_number_common_letters))
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
        #Φόρτωση κειμένου 'cnn-gr_raw'
        textX_name = 'cnn-gr_raw'
        textX_path = 'set_theory_lab/' + textX_name + '.txt'
        f = open (textX_path, 'r', encoding='utf-8')
        text_X = f.read()
        f.close()

        #Φόρτωση κειμένου 'news247_raw'
        textY_name = 'news247_raw'
        textY_path = 'set_theory_lab/' + textY_name + '.txt'
        f = open (textY_path, 'r', encoding='utf-8')
        text_Y = f.read()
        f.close()
        
        #Δημιουργία συνόλων λέξεων του εκάστοτε κειμένου
        set_X = set(text_X.split(" "))
        set_Y = set(text_Y.split(" "))

        #Δημιουργία συνόλων με διάφορα χαρακτηριστικά
        #Κοινές λέξεις κειμένων
        common_words = set_X.intersection(set_Y)
        #Σύνολο μη κοινών λέξεων ( ένωση συνόλων λέξεων των δύο κειμένων χωρίς την τομή τους )
        non_common_words = set_X.symmetric_difference(set_Y)
        #Σύνολο όλων των λέξεων και από τα δύο κείμενα
        all_words = set_X.union(set_Y)
        #Λέξεις του κειμένου Χ χωρίς τις λέξεις του κειμένου Υ
        text_X_only_words = set_X - set_Y
        #Λέξεις του κειμένου Υ χωρίς τις λέξεις του κειμένου Χ
        text_Y_only_words = set_Y - set_X

        #Πληθικός αριθμός εκάστοτε συνόλου
        common_words_cardinality = len(common_words)
        all_words_cardinality = len(all_words)
        non_common_words_cardinality = len(non_common_words)
        set_X_cardinality = len(set_X)
        set_Y_cardinality = len(set_Y)
        text_X_only_words_cardinality = len(text_X_only_words)
        text_Y_only_words_cardinality = len(text_Y_only_words)
        
        #Παρακάτω, σχηματίζονται όλοι οι λόγοι που αφορούν στη σύγκριση των δύο κειμένων

        #ratio: Λόγος της τομής των κειμένων προς το κάθε κείμενο, δηλώνει το ποσοστό της τομής που αποτελεί 
        #το κάθε κείμενο. Όσο μεγαλύτερος είναι αυτός ο λόγος, τόσο μεγαλύτερο ποσοστό του κειμένου εκείνου 
        #αποτελεί την τομή λέξεων των δύο. Συνεπώς, δηλώνει πως το κείμενο με το μεγαλύτερο λόγο, περιλαμβάνεται 
        #στο κείμενο με το μικρότερο λόγο εαν υπάρχει αξιοσημείωτη διαφορά και ιδιαίτερα όταν ο λόγος του πρώτου, 
        #ξεπερνά ένα προκαθορισμένο threshold, συνήθως >0.7/0.75
        ratio_X = common_words_cardinality/set_X_cardinality
        ratio_Y = common_words_cardinality/set_Y_cardinality

        #ratio2: Λόγος των συνόλων των λέξεων του κάθε κειμένου προς την ένωσή τους, δηλώνει τη συμβολή του κάθε κειμένου 
        #στο σύνολο της ένωσης των λέξεών τους. Όσο μικρότερος είναι ο λόγος, τόσο μικρότερο ποσοστό των λέξεων του κειμένου εκείνου 
        #αποτελεί την ένωση των λέξεων των δύο. Συνεπώς, δηλώνει πως το κείμενο με το μικρότερο λόγο, περιλαμβάνεται 
        #στο κείμενο με το μεγαλύτερο λόγο, εαν υπάρχει αξιοσημείωτη διαφορά και ιδιαίτερα όταν ο λόγος του δεύτερου, 
        #ξεπερνά ένα προκαθορισμένο threshold, συνήθως >0.85/0.9
        ratio2_X = set_X_cardinality/all_words_cardinality
        ratio2_Y = set_Y_cardinality/all_words_cardinality

        ratio3_X = text_X_only_words_cardinality/set_X_cardinality
        ratio3_Y = text_Y_only_words_cardinality/set_Y_cardinality

        print("\nCommon words: %d\nNon-common words: %d\nAll words: %d\n\nRatio_X ( common_words_cardinality/set_X_cardinality ): %.5f\nRatio_Y ( common_words_cardinality/set_Y_cardinality ): %.5f\n\nRatio2_X ( set_X_cardinality/all_words_cardinality ): %.5f\nRatio2_Y ( set_Y_cardinality/all_words_cardinality ): %.5f\n\nRatio3_X ( text_X_only_words_cardinality/set_X_cardinality ): %.5f\nRatio3_Y ( text_Y_only_words_cardinality/set_Y_cardinality ): %.5f\n"%(common_words_cardinality, non_common_words_cardinality, all_words_cardinality, ratio_X, ratio_Y, ratio2_X, ratio2_Y, ratio3_X, ratio3_Y))

        #Χρήση του λόγου ratio3 ως μέτρο σύγκρισης των κειμένων
        threshold = 0.3
        if (ratio3_X < threshold):
            print("\nText '%s' is included in text '%s' ! !\n"%(textX_name, textY_name)) 
        elif (ratio3_Y < threshold):
            print("\nText '%s' is included in text '%s' ! !\n"%(textY_name, textX_name)) 
        else:
            print("\nTexts are far from duplicates ! !\n") 


    


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