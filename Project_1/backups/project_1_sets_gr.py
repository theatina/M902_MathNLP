# -*- coding: utf-8 -*-
#coding=utf-8
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

        #Set of the accented vowels
        accented_vowels = set("ΆΈΉΊΌΎΏ")

        #In both cases of 'ς' and 'σ', the upper letter will be the same('Σ'), merging the two different lower symbols into one capital
        input_txt_set = set(sentence.upper())
        sentence_set = set(sentence)

        #cases of accented vowels
        input_txt_acc_vowels = accented_vowels.intersection(input_txt_set)

        #create a tuple with pairs of non-accented and accented vowels
        all_vowels = ( ('Α', 'Ά'), ('Ε', 'Έ'), ('Η', 'Ή'), ('Ι', 'Ί'), ('Ο', 'Ό'), ('Υ', 'Ύ'), ('Ω', 'Ώ') )
        
        acc_vowels_to_remove = []
        vowels_to_add = []
        #remove accents from the accented vowels in the input text set - update the character set of the sentense
        for vowel in input_txt_acc_vowels: 
            for tuple_index,a in enumerate(all_vowels):
                #if an accented vowel is found, it is replaced by the non accented upper case one
                if vowel in a:
                    pos = a.index(vowel)
                    acc_vowels_to_remove.append(vowel)
                    vowel_to_add = all_vowels[tuple_index][pos-1]
                    vowels_to_add.append(vowel_to_add)

        #remove accented vowels
        input_txt_set.difference_update(acc_vowels_to_remove)
        #add - if not in set - the non accented versions of the vowels above
        input_txt_set.update(vowels_to_add)
        
        #Creation of the sets 'input_txt_set' and 'alphabet' intersection set - common letters between the alphabet and the sentence set of characters
        #which is the set of the letters that the sentence includes
        common_letters = alphabet.intersection(input_txt_set)
        #Find the letters of the alphabet that are not included in the sentence set
        non_common_letters = alphabet - common_letters

        #Find how many letters are common
        cardinal_number_common_letters = len(common_letters)

        print("\nΠληθικός αριθμός του συνόλου γραμμάτων που περιέχονται στη φράση: '%s' : %d \n" % (sentence, cardinal_number_common_letters))
        #In order to be a pangram, we need the cardinal number of the common letters set to be exactly 24(greek alphabet)
        if cardinal_number_common_letters is len(alphabet):
            print("\nThe sentence: '%s' is a Pangram of length %d! \n"%(sentence,len(sentence)))
            return True, len(sentence_set)
        else:
            print("\nThe sentence: '" + sentence + "' is ΝΟΤ a Pangram ! \n\n( set of missing letters: " + str(non_common_letters) + " )\n")
            return False, len(sentence_set)

    

    def ex_1_4(self, sentence="θα ΄ρθεις αποψε να διασκεδάσουμε με τους φίλους μας στην κάτω γειτονια των βλαχερνων;"):
        print("\nΔε μπορούμε να συμπεράνουμε ότι μια φράση είναι pangram εάν απλώς έχει πληθικό αριθμό συνόλου χαρακτήρων τουλάχιστον 24, καθώς μπορεί να περιέχει και άλλους χαρακτήρες (';', '.', ',', '!', κλπ)\nΜπορούμε να το ελέγξουμε και με τη χρήση της συνάρτησης που υλοποιήθηκε στο προηγούμενο ερώτημα:")
        is_pangram, card_num = (Exercises.ex_1_3(Exercises, sentence))
        print("\nCardinal number of the sentence's characters: %d > 24 . However, it is NOT a Pangram !\n"%(card_num))

    def ex_1_5(self):
        A = [ 'ενα', 'νεα', 'εννεα']
        counter = 1
        for i in A:
            print("%d. '%s': %s == {'α', 'ε', 'ν'}"%(counter,i,set(i)))
            counter+=1

    def ex_1_6(self):
        A = [ 'ΠΡΑΣΟ', 'ΣΠΑΡΟΣ', 'ΠΡΑΟΣ', 'ΑΣΠΡΟΣ']
        counter = 1
        for i in A:
            print("%d. '%s': %s == {Α, Ο, Π, Ρ, Σ}"%(counter,i,set(i)))
            counter+=1

    def ex_1_7(self):
        A = [ 'ΠΛΟΙΟ', 'ΛΟΙΠΟΙ', 'ΠΟΛΛΟΙ', 'ΠΟΛΟΙ', 'ΟΠΛΟΠΟΙΟΙ']
        counter = 1
        for i in A:
            print("%d. '%s': %s == {Π, Ι, Λ, Ο} -> μήκος λέξης: %d > 4"%(counter,i,set(i),len(i)))
            counter+=1

    def ex_1_8(self):
        words = ['νερο', 'ποταμι', 'οργη']
        vowels_gr = set('αεηιουω')
        all_chars = set()
        for word in words:
            all_chars.update(word)

        vowels_not_in_words = vowels_gr - all_chars.intersection(vowels_gr)
        print("\nVowels not in the characters set of the words %s: %s\n"%(set(words),vowels_not_in_words))

    def ex_1_9(self, phrase1 = 'οι επιστημονες εστιαζουν στην αντιμετωπιση του ιου', phrase2 = 'οι επιστημονες εστιαζουν στην αντιμετωπιση της φτωχιας'):
        phrase1_list = phrase1.split(" ")
        phrase1_set = set(phrase1_list)
        
        phrase2_list = phrase2.split(" ")
        phrase2_set = set(phrase2_list)

        non_significant_words = set(['οι', 'στην', 'του', 'της'])

        significant_non_common_words = phrase1_set.symmetric_difference(phrase2_set) - non_significant_words
        print("\nPhrases:\n1. '" + str(phrase1) +"'\n2. '" + str(phrase2) + "'\n\nSignificant non common words of 1 & 2: " + str(significant_non_common_words) + "\n")


    def ex_1_10(self, textX_path='./set_theory_lab/cnn-gr_raw.txt', textY_path = './set_theory_lab/news247_raw.txt' ):
        #Φόρτωση κειμένου X
        f = open (textX_path, 'r', encoding='utf-8')
        text_X = f.read()
        f.close()

        #Φόρτωση κειμένου Y
        f = open (textY_path, 'r', encoding='utf-8')
        text_Y = f.read()
        f.close()

        textX_name = textX_path.split('/')[-1][:-4]
        textY_name = textY_path.split('/')[-1][:-4]
        
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
        #Λέξεις του κειμένου Χ χωρίς τις κοινές λέξεις με το κείμενο Υ
        text_X_only_words = set_X - set_Y
        #Λέξεις του κειμένου Υ χωρίς τις κοινές λέξεις με το κείμενο Χ
        text_Y_only_words = set_Y - set_X

        #Πληθικός αριθμός εκάστοτε συνόλου
        common_words_cardinality = len(common_words)
        all_words_cardinality = len(all_words)
        non_common_words_cardinality = len(non_common_words)
        set_X_cardinality = len(set_X)
        set_Y_cardinality = len(set_Y)
        text_X_only_words_cardinality = len(text_X_only_words)
        text_Y_only_words_cardinality = len(text_Y_only_words)

        #Παρακάτω, σχηματίζονται κάποιοι λόγοι που αφορούν στη σύγκριση των δύο κειμένων

        #ratio1: Λόγος της τομής των λέξεων των κειμένων προς τις λέξεις κάθε κειμένου. Δηλώνει το ποσοστό της τομής  
        #που αποτελεί το κάθε κείμενο. Όσο μεγαλύτερος είναι αυτός ο λόγος, τόσο μεγαλύτερο ποσοστό του κειμένου εκείνου 
        #αποτελείται από την τομή λέξεων των δύο κειμένων. Συνεπώς, δηλώνει πως το κείμενο Υ με το μεγαλύτερο λόγο, 
        #περιλαμβάνεται στο κείμενο Χ με το μικρότερο λόγο εαν υπάρχει αξιοσημείωτη διαφορά και ιδιαίτερα όταν ο λόγος του  
        #πρώτου(Υ), ξεπερνά ένα προκαθορισμένο threshold, συνήθως >= 0.7/0.75
        ratio1_X = common_words_cardinality/set_X_cardinality
        ratio1_Y = common_words_cardinality/set_Y_cardinality

        #ratio2: Λόγος των συνόλων των λέξεων του κάθε κειμένου προς την ένωσή του. Δηλώνει τη συμβολή του κάθε κειμένου 
        #στο σύνολο της ένωσης των λέξεών τους. Όσο μικρότερος είναι ο λόγος, τόσο μικρότερο ποσοστό των λέξεων του κειμένου 
        #εκείνου αποτελεί την ένωση των λέξεων των δύο. Συνεπώς, δηλώνει πως το κείμενο με το μικρότερο λόγο, περιλαμβάνεται 
        #στο κείμενο με το μεγαλύτερο λόγο, εαν υπάρχει αξιοσημείωτη διαφορά και ιδιαίτερα όταν ο λόγος του δεύτερου, 
        #ξεπερνά ένα προκαθορισμένο threshold, συνήθως >= 0.85/0.9
        ratio2_X = set_X_cardinality/all_words_cardinality
        ratio2_Y = set_Y_cardinality/all_words_cardinality

        #ratio3: Λόγος των μη κοινών λέξεων του εκάστοτε κειμένου προς το σύνολο λέξεών του. Δηλώνει τη συμβολή των 
        #μη κοινών λέξεων του εκάστοτε κειμένου, στο συνολικό κείμενο. Όσο μικρότερος είναι ο λόγος, τόσο μεγαλύτερο 
        #ποσοστό των λέξεων του κειμένου εκείνου αποτελείται από την τομή του με το δεύτερο κείμενο (συμπληρωματικές έννοιες 
        #με το ratio1 παραπάνω). Συνεπώς, δηλώνει πως το κείμενο με το μικρότερο λόγο, περιλαμβάνεται στο κείμενο με το μεγαλύτερο 
        #λόγο, κατά ratio1 = 1-ratio3 ποσοστό, εαν υπάρχει αξιοσημείωτη διαφορά και ιδιαίτερα όταν ο λόγος του δεύτερου, βρίσκεται 
        #κάτω από ένα προκαθορισμένο threshold, συνήθως <= 0.25/0.3
        ratio3_X = text_X_only_words_cardinality/set_X_cardinality
        ratio3_Y = text_Y_only_words_cardinality/set_Y_cardinality

        print("\nCommon words: %d\nNon-common words: %d\nAll words: %d\n\nRatio1_X ( common_words_cardinality/set_X_cardinality ): %.5f\nRatio1_Y ( common_words_cardinality/set_Y_cardinality ): %.5f\n\nRatio2_X ( set_X_cardinality/all_words_cardinality ): %.5f\nRatio2_Y ( set_Y_cardinality/all_words_cardinality ): %.5f\n\nRatio3_X ( text_X_only_words_cardinality/set_X_cardinality ): %.5f\nRatio3_Y ( text_Y_only_words_cardinality/set_Y_cardinality ): %.5f\n"%(common_words_cardinality, non_common_words_cardinality, all_words_cardinality, ratio1_X, ratio1_Y, ratio2_X, ratio2_Y, ratio3_X, ratio3_Y))

        #Χρήση του λόγου ratio3 ως μέτρο σύγκρισης των κειμένων, με τιμή ορίου 0.3 . Κάτω από αυτή την τιμή, ο λόγος δηλώνει πως το αντίστοιχο κείμενο 
        #περιλαμβάνεται 
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
    print("\nExercise number must be between 1 - 10 ! !\n")
    exit()

line = ["_" for i in range(100)]
line = "".join(line)

function_to_call_name = "ex_1_" + str(args.ex)
fun_to_call = getattr(Exercises, function_to_call_name)

print("\n"+str(line)+"\n")
fun_to_call(Exercises)
print(str(line)+"\n")