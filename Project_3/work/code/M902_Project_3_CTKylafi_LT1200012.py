# -*- coding: utf-8 -*-
#coding=utf-8
import argparse
from collections import Counter
import numpy as np
from numpy.linalg import norm

#Exercises
class Exercises:
    
    def ex_3_1(self, A=[[2,-3,5],[1,-2,7],[3,8,4]]):
        #Εύρεση υποοριζουσών
        # print()
        return 9

    def ex_3_2(self, sentence="Δεν προλαβαίνω ποτέ δεν προλαβαίνω"):
        #Splitting the sentence to get the set of all the words
        words = sentence.split(" ")
        A = set(words)
        
        #Find the number of words in the set (cardinal number of the word set)
        cardinal_number_A = len(A)
        print("\n A = " + str(A))
        print("\nΠληθικός αριθμός του συνόλου λέξεων (Α) της φράσης '%s' : %d \n" % (sentence, cardinal_number_A))

    #making use of capital letters, in order not to have to deal with the two s 's, "σ" and "ς"
    def ex_3_3(self, sentence="οι πολιτικες και οικονομικες εξελιξεις διαδραματιζονται γυρω απο τις προσπαθειες, τις βλεψεις και τους αγωνες για τον ελεγχο φυσικων πορων"):
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

    

    def ex_3_4(self, sentence="θα ΄ρθεις αποψε να διασκεδάσουμε με τους φίλους μας στην κάτω γειτονια των βλαχερνων;"):
        print("\nΔε μπορούμε να συμπεράνουμε ότι μια φράση είναι pangram εάν απλώς έχει πληθικό αριθμό συνόλου χαρακτήρων τουλάχιστον 24, καθώς μπορεί να περιέχει και άλλους χαρακτήρες (';', '.', ',', '!', κλπ), το τελικό σίγμα ή και τονισμένα φωνήεντα, που θεωρούνται ξεχωριστοί χαρακτήρες.\nΜπορούμε να το ελέγξουμε και με τη χρήση της συνάρτησης που υλοποιήθηκε στο προηγούμενο ερώτημα:")
        is_pangram, card_num = (Exercises.ex_1_3(Exercises, sentence))
        print("\nCardinal number of the sentence's characters: %d > 24 . However, it is NOT a Pangram !\n"%(card_num))

    def ex_3_5(self):
        A = [ 'ενα', 'νεα', 'εννεα']
        counter = 1
        for i in A:
            print("%d. '%s': %s == {'α', 'ε', 'ν'}"%(counter,i,set(i)))
            counter+=1

    def ex_3_6(self):
        A = [ 'ΠΡΑΣΟ', 'ΣΠΑΡΟΣ', 'ΠΡΑΟΣ', 'ΑΣΠΡΟΣ']
        counter = 1
        for i in A:
            print("%d. '%s': %s == {'Α', 'Ο', 'Π', 'Ρ', 'Σ'}"%(counter,i,set(i)))
            counter+=1

    def ex_3_7(self):
        A = [ 'ΠΛΟΙΟ', 'ΛΟΙΠΟΙ', 'ΠΟΛΛΟΙ', 'ΠΟΛΟΙ', 'ΟΠΛΟΠΟΙΟΙ']
        counter = 1
        for i in A:
            print("%d. '%s': %s == {'Π', 'Ι', 'Λ', 'Ο'} -> μήκος λέξης: %d > 4"%(counter,i,set(i),len(i)))
            counter+=1

    def ex_3_8(self):
        words = ['νερο', 'ποταμι', 'ορμη']
        vowels_gr = set('αεηιουω')
        all_chars = set()
        for word in words:
            all_chars.update(word)

        vowels_not_in_words = vowels_gr - all_chars.intersection(vowels_gr)
        print("\nVowels not in the characters set of the words %s: %s\n"%(set(words),vowels_not_in_words))

    def ex_3_9(self ):
        phrase1_list = phrase1.split(" ")
        phrase1_set = set(phrase1_list)
        
        phrase2_list = phrase2.split(" ")
        phrase2_set = set(phrase2_list)

        #αφαιρούνται οι μη σημαντικές(υψίσυχνες) λέξεις
        non_significant_words = set(['οι', 'στην', 'του', 'της'])

        #Δημιουργείται το σύνολο της ένωσης των λέξεων των δύο φράσεων χωρίς την τομή τους και χωρίς 
        # τις μη σημαντικές λέξεις
        significant_non_common_words = phrase1_set.symmetric_difference(phrase2_set) - non_significant_words
        print("\nPhrases:\n1. '" + str(phrase1) +"'\n2. '" + str(phrase2) + "'\n\nSignificant non common words of 1 & 2: " + str(significant_non_common_words) + "\n")


    def ex_3_10(self, d0=[8,6,0], d1=[0,6,8], d2=[6,0,8], d3=[2,3,0], d4=[9,6,0]):
        
        d_vectors = [d0,d1,d2,d3,d4]
        d_vectors_normalised = []
        # print(d_vectors)
        for vect in d_vectors:
            print(norm(vect))
            vect /= norm(vect)
            d_vectors_normalised.append(vect)

        d_vectors_normalised = np.array(d_vectors_normalised)
        d_vectors_normalised_T = d_vectors_normalised.T
        print(d_vectors_normalised)

        similarity_array = d_vectors_normalised @ d_vectors_normalised_T
        print(similarity_array)
        
        corrcoef_vectors = np.corrcoef(d_vectors)
        print("\n%s\n"%(corrcoef_vectors))

        high_threshold = 0.9
        for j in range(similarity_array.shape[1]):
            for i in range(j+1,similarity_array.shape[0]):
                if similarity_array[i,j] >= high_threshold:
                    print("\nDot product d%d • d%d: %.4f (Correlation: %.4f)  ->  Documents %d and %d are similar ! ! \n"%(j+1, i+1, similarity_array[i,j],corrcoef_vectors[i,j], j+1, i+1 ))
                else:
                    print("\nDot product d%d • d%d: %.4f (Correlation: %.4f)\n"%(j+1, i+1, similarity_array[i,j], corrcoef_vectors[i,j]))
        


        return 9


#main
parser = argparse.ArgumentParser()
parser.add_argument("-ex", type=int, help="number of exercise to solve", default=1)
args = parser.parse_args()

if (args.ex > 10) or (args.ex < 1):
    print("\nExercise number must be between 1 - 10 ! !\n")
    exit()

line = ["_" for i in range(100)]
line = "".join(line)

function_to_call_name = "ex_3_" + str(args.ex)
fun_to_call = getattr(Exercises, function_to_call_name)

print("\n--> %s:"%(fun_to_call.__name__))
print(""+str(line)+"\n")
fun_to_call(Exercises)
print(str(line)+"\n")